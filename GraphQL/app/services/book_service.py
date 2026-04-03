from app.utils.db import get_db
from app.schema.types import Book, CreateBookInput, UpdateBookInput


def _row_to_book(row) -> Book:
    return Book(
        id=row["nBookID"],
        title=row["cTitle"],
        author_id=row["nAuthorID"],
        publisher_id=row["nPublishingCompanyID"],
        publishing_year=row["nPublishingYear"],
    )


def _validate_references(conn, author_id: int, publisher_id: int):
    author = conn.execute(
        "SELECT nAuthorID FROM tauthor WHERE nAuthorID = ?", (author_id,)
    ).fetchone()
    if not author:
        raise ValueError(f"Author with id {author_id} does not exist")
    publisher = conn.execute(
        "SELECT nPublishingCompanyID FROM tpublishingcompany WHERE nPublishingCompanyID = ?",
        (publisher_id,),
    ).fetchone()
    if not publisher:
        raise ValueError(f"Publisher with id {publisher_id} does not exist")


def get_by_id(book_id: int) -> Book | None:
    with get_db() as conn:
        row = conn.execute(
            "SELECT nBookID, cTitle, nAuthorID, nPublishingCompanyID, nPublishingYear FROM tbook WHERE nBookID = ?",
            (book_id,),
        ).fetchone()
    return _row_to_book(row) if row else None


def get_all() -> list[Book]:
    with get_db() as conn:
        rows = conn.execute(
            "SELECT nBookID, cTitle, nAuthorID, nPublishingCompanyID, nPublishingYear FROM tbook ORDER BY nBookID"
        ).fetchall()
    return [_row_to_book(r) for r in rows]


def create(data: CreateBookInput) -> Book:
    if data.publishing_year < 1900:
        raise ValueError("Publishing year must be >= 1900")
    with get_db() as conn:
        _validate_references(conn, data.author_id, data.publisher_id)
        cursor = conn.execute(
            "INSERT INTO tbook (cTitle, nAuthorID, nPublishingCompanyID, nPublishingYear) VALUES (?, ?, ?, ?)",
            (data.title, data.author_id, data.publisher_id, data.publishing_year),
        )
        return Book(
            id=cursor.lastrowid,
            title=data.title,
            author_id=data.author_id,
            publisher_id=data.publisher_id,
            publishing_year=data.publishing_year,
        )


def update(book_id: int, data: UpdateBookInput) -> Book | None:
    if data.publishing_year < 1900:
        raise ValueError("Publishing year must be >= 1900")
    with get_db() as conn:
        existing = conn.execute(
            "SELECT nBookID FROM tbook WHERE nBookID = ?", (book_id,)
        ).fetchone()
        if not existing:
            return None
        _validate_references(conn, data.author_id, data.publisher_id)
        conn.execute(
            "UPDATE tbook SET cTitle = ?, nAuthorID = ?, nPublishingCompanyID = ?, nPublishingYear = ? WHERE nBookID = ?",
            (data.title, data.author_id, data.publisher_id, data.publishing_year, book_id),
        )
    return Book(
        id=book_id,
        title=data.title,
        author_id=data.author_id,
        publisher_id=data.publisher_id,
        publishing_year=data.publishing_year,
    )


def delete(book_id: int) -> bool:
    with get_db() as conn:
        existing = conn.execute(
            "SELECT nBookID FROM tbook WHERE nBookID = ?", (book_id,)
        ).fetchone()
        if not existing:
            return False
        conn.execute("DELETE FROM tbook WHERE nBookID = ?", (book_id,))
    return True
