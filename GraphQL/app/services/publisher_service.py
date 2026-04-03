from app.utils.db import get_db
from app.schema.types import Publisher, CreatePublisherInput, UpdatePublisherInput


def _row_to_publisher(row) -> Publisher:
    return Publisher(id=row["nPublishingCompanyID"], name=row["cName"])


def get_by_id(publisher_id: int) -> Publisher | None:
    with get_db() as conn:
        row = conn.execute(
            "SELECT nPublishingCompanyID, cName FROM tpublishingcompany WHERE nPublishingCompanyID = ?",
            (publisher_id,),
        ).fetchone()
    return _row_to_publisher(row) if row else None


def get_all() -> list[Publisher]:
    with get_db() as conn:
        rows = conn.execute(
            "SELECT nPublishingCompanyID, cName FROM tpublishingcompany ORDER BY nPublishingCompanyID"
        ).fetchall()
    return [_row_to_publisher(r) for r in rows]


def create(data: CreatePublisherInput) -> Publisher:
    with get_db() as conn:
        cursor = conn.execute(
            "INSERT INTO tpublishingcompany (cName) VALUES (?)",
            (data.name,),
        )
        return Publisher(id=cursor.lastrowid, name=data.name)


def update(publisher_id: int, data: UpdatePublisherInput) -> Publisher | None:
    with get_db() as conn:
        existing = conn.execute(
            "SELECT nPublishingCompanyID FROM tpublishingcompany WHERE nPublishingCompanyID = ?",
            (publisher_id,),
        ).fetchone()
        if not existing:
            return None
        conn.execute(
            "UPDATE tpublishingcompany SET cName = ? WHERE nPublishingCompanyID = ?",
            (data.name, publisher_id),
        )
    return Publisher(id=publisher_id, name=data.name)


def delete(publisher_id: int) -> bool:
    with get_db() as conn:
        existing = conn.execute(
            "SELECT nPublishingCompanyID FROM tpublishingcompany WHERE nPublishingCompanyID = ?",
            (publisher_id,),
        ).fetchone()
        if not existing:
            return False
        ref = conn.execute(
            "SELECT COUNT(*) as cnt FROM tbook WHERE nPublishingCompanyID = ?",
            (publisher_id,),
        ).fetchone()
        if ref["cnt"] > 0:
            raise ValueError("Cannot delete publisher: referenced by existing books")
        conn.execute(
            "DELETE FROM tpublishingcompany WHERE nPublishingCompanyID = ?",
            (publisher_id,),
        )
    return True
