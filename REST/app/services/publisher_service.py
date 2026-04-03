from fastapi import HTTPException
from app.utils.db import get_db
from app.models import Publisher, PublisherCreate, PublisherUpdate


def _row_to_publisher(row) -> Publisher:
    return Publisher(id=row["nPublishingCompanyID"], name=row["cName"])


def create(body: PublisherCreate) -> Publisher:
    with get_db() as conn:
        cursor = conn.execute(
            "INSERT INTO tpublishingcompany (cName) VALUES (?)",
            (body.name,),
        )
        return Publisher(id=cursor.lastrowid, name=body.name)


def get_by_id(publisher_id: int) -> Publisher:
    with get_db() as conn:
        row = conn.execute(
            "SELECT nPublishingCompanyID, cName FROM tpublishingcompany WHERE nPublishingCompanyID = ?",
            (publisher_id,),
        ).fetchone()
    if not row:
        raise HTTPException(status_code=404, detail="Publisher not found")
    return _row_to_publisher(row)


def get_all() -> list[Publisher]:
    with get_db() as conn:
        rows = conn.execute(
            "SELECT nPublishingCompanyID, cName FROM tpublishingcompany ORDER BY nPublishingCompanyID"
        ).fetchall()
    return [_row_to_publisher(r) for r in rows]


def update(publisher_id: int, body: PublisherUpdate) -> Publisher:
    with get_db() as conn:
        existing = conn.execute(
            "SELECT nPublishingCompanyID FROM tpublishingcompany WHERE nPublishingCompanyID = ?",
            (publisher_id,),
        ).fetchone()
        if not existing:
            raise HTTPException(status_code=404, detail="Publisher not found")
        conn.execute(
            "UPDATE tpublishingcompany SET cName = ? WHERE nPublishingCompanyID = ?",
            (body.name, publisher_id),
        )
    return Publisher(id=publisher_id, name=body.name)


def delete(publisher_id: int) -> None:
    with get_db() as conn:
        existing = conn.execute(
            "SELECT nPublishingCompanyID FROM tpublishingcompany WHERE nPublishingCompanyID = ?",
            (publisher_id,),
        ).fetchone()
        if not existing:
            raise HTTPException(status_code=404, detail="Publisher not found")
        ref = conn.execute(
            "SELECT COUNT(*) as cnt FROM tbook WHERE nPublishingCompanyID = ?",
            (publisher_id,),
        ).fetchone()
        if ref["cnt"] > 0:
            raise HTTPException(
                status_code=409,
                detail="Cannot delete publisher: referenced by existing books",
            )
        conn.execute(
            "DELETE FROM tpublishingcompany WHERE nPublishingCompanyID = ?",
            (publisher_id,),
        )
