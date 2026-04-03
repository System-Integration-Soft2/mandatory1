from fastapi import HTTPException
from app.utils.db import get_db
from app.models import Author, AuthorCreate, AuthorUpdate


def _row_to_author(row) -> Author:
    return Author(id=row["nAuthorID"], name=row["cName"], surname=row["cSurname"])


def create(body: AuthorCreate) -> Author:
    with get_db() as conn:
        cursor = conn.execute(
            "INSERT INTO tauthor (cName, cSurname) VALUES (?, ?)",
            (body.name, body.surname),
        )
        return Author(id=cursor.lastrowid, name=body.name, surname=body.surname)


def get_by_id(author_id: int) -> Author:
    with get_db() as conn:
        row = conn.execute(
            "SELECT nAuthorID, cName, cSurname FROM tauthor WHERE nAuthorID = ?",
            (author_id,),
        ).fetchone()
    if not row:
        raise HTTPException(status_code=404, detail="Author not found")
    return _row_to_author(row)


def get_all() -> list[Author]:
    with get_db() as conn:
        rows = conn.execute(
            "SELECT nAuthorID, cName, cSurname FROM tauthor ORDER BY nAuthorID"
        ).fetchall()
    return [_row_to_author(r) for r in rows]


def update(author_id: int, body: AuthorUpdate) -> Author:
    with get_db() as conn:
        existing = conn.execute(
            "SELECT nAuthorID FROM tauthor WHERE nAuthorID = ?", (author_id,)
        ).fetchone()
        if not existing:
            raise HTTPException(status_code=404, detail="Author not found")
        conn.execute(
            "UPDATE tauthor SET cName = ?, cSurname = ? WHERE nAuthorID = ?",
            (body.name, body.surname, author_id),
        )
    return Author(id=author_id, name=body.name, surname=body.surname)


def delete(author_id: int) -> None:
    with get_db() as conn:
        existing = conn.execute(
            "SELECT nAuthorID FROM tauthor WHERE nAuthorID = ?", (author_id,)
        ).fetchone()
        if not existing:
            raise HTTPException(status_code=404, detail="Author not found")
        ref = conn.execute(
            "SELECT COUNT(*) as cnt FROM tbook WHERE nAuthorID = ?", (author_id,)
        ).fetchone()
        if ref["cnt"] > 0:
            raise HTTPException(
                status_code=409,
                detail="Cannot delete author: referenced by existing books",
            )
        conn.execute("DELETE FROM tauthor WHERE nAuthorID = ?", (author_id,))
