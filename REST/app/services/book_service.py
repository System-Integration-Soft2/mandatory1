from fastapi import HTTPException
from app.utils.db import get_db
from app.models import Book, BookCreate, BookUpdate


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
        raise HTTPException(
            status_code=422, detail=f"Author with id {author_id} does not exist"
        )
    publisher = conn.execute(
        "SELECT nPublishingCompanyID FROM tpublishingcompany WHERE nPublishingCompanyID = ?",
        (publisher_id,),
    ).fetchone()
    if not publisher:
        raise HTTPException(
            status_code=422,
            detail=f"Publisher with id {publisher_id} does not exist",
        )


def create(body: BookCreate) -> Book:
    with get_db() as conn:
        _validate_references(conn, body.author_id, body.publisher_id)
        cursor = conn.execute(
            "INSERT INTO tbook (cTitle, nAuthorID, nPublishingCompanyID, nPublishingYear) VALUES (?, ?, ?, ?)",
            (body.title, body.author_id, body.publisher_id, body.publishing_year),
        )
        return Book(
            id=cursor.lastrowid,
            title=body.title,
            author_id=body.author_id,
            publisher_id=body.publisher_id,
            publishing_year=body.publishing_year,
        )


def get_by_id(book_id: int) -> Book:
    with get_db() as conn:
        row = conn.execute(
            "SELECT nBookID, cTitle, nAuthorID, nPublishingCompanyID, nPublishingYear FROM tbook WHERE nBookID = ?",
            (book_id,),
        ).fetchone()
    if not row:
        raise HTTPException(status_code=404, detail="Book not found")
    return _row_to_book(row)


def get_all(limit: int, offset: int) -> list[Book]:
    with get_db() as conn:
        rows = conn.execute(
            "SELECT nBookID, cTitle, nAuthorID, nPublishingCompanyID, nPublishingYear FROM tbook ORDER BY nBookID LIMIT ? OFFSET ?",
            (limit, offset),
        ).fetchall()
    return [_row_to_book(r) for r in rows]


def update(book_id: int, body: BookUpdate) -> Book:
    with get_db() as conn:
        existing = conn.execute(
            "SELECT nBookID FROM tbook WHERE nBookID = ?", (book_id,)
        ).fetchone()
        if not existing:
            raise HTTPException(status_code=404, detail="Book not found")
        _validate_references(conn, body.author_id, body.publisher_id)
        conn.execute(
            "UPDATE tbook SET cTitle = ?, nAuthorID = ?, nPublishingCompanyID = ?, nPublishingYear = ? WHERE nBookID = ?",
            (body.title, body.author_id, body.publisher_id, body.publishing_year, book_id),
        )
    return Book(
        id=book_id,
        title=body.title,
        author_id=body.author_id,
        publisher_id=body.publisher_id,
        publishing_year=body.publishing_year,
    )


def delete(book_id: int) -> None:
    with get_db() as conn:
        existing = conn.execute(
            "SELECT nBookID FROM tbook WHERE nBookID = ?", (book_id,)
        ).fetchone()
        if not existing:
            raise HTTPException(status_code=404, detail="Book not found")
        conn.execute("DELETE FROM tbook WHERE nBookID = ?", (book_id,))
