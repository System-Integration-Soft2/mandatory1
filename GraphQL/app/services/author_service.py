from app.utils.db import get_db
from app.schema.types import Author, CreateAuthorInput, UpdateAuthorInput


def _row_to_author(row) -> Author:
    return Author(id=row["nAuthorID"], name=row["cName"], surname=row["cSurname"])


def get_by_id(author_id: int) -> Author | None:
    with get_db() as conn:
        row = conn.execute(
            "SELECT nAuthorID, cName, cSurname FROM tauthor WHERE nAuthorID = ?",
            (author_id,),
        ).fetchone()
    return _row_to_author(row) if row else None


def get_all() -> list[Author]:
    with get_db() as conn:
        rows = conn.execute(
            "SELECT nAuthorID, cName, cSurname FROM tauthor ORDER BY nAuthorID"
        ).fetchall()
    return [_row_to_author(r) for r in rows]


def create(data: CreateAuthorInput) -> Author:
    with get_db() as conn:
        cursor = conn.execute(
            "INSERT INTO tauthor (cName, cSurname) VALUES (?, ?)",
            (data.name, data.surname),
        )
        return Author(id=cursor.lastrowid, name=data.name, surname=data.surname)


def update(author_id: int, data: UpdateAuthorInput) -> Author | None:
    with get_db() as conn:
        existing = conn.execute(
            "SELECT nAuthorID FROM tauthor WHERE nAuthorID = ?", (author_id,)
        ).fetchone()
        if not existing:
            return None
        conn.execute(
            "UPDATE tauthor SET cName = ?, cSurname = ? WHERE nAuthorID = ?",
            (data.name, data.surname, author_id),
        )
    return Author(id=author_id, name=data.name, surname=data.surname)


def delete(author_id: int) -> bool:
    with get_db() as conn:
        existing = conn.execute(
            "SELECT nAuthorID FROM tauthor WHERE nAuthorID = ?", (author_id,)
        ).fetchone()
        if not existing:
            return False
        ref = conn.execute(
            "SELECT COUNT(*) as cnt FROM tbook WHERE nAuthorID = ?", (author_id,)
        ).fetchone()
        if ref["cnt"] > 0:
            raise ValueError("Cannot delete author: referenced by existing books")
        conn.execute("DELETE FROM tauthor WHERE nAuthorID = ?", (author_id,))
    return True
