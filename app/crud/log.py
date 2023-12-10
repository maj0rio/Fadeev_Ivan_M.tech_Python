from datetime import datetime

from sqlalchemy.orm import Session

from schema.log import LogSchema
from models import LogDB


async def create_log(db: Session, log: LogSchema) -> LogDB:
    db_log = LogDB(**log.dict())
    db.add(db_log)
    db.commit()
    db.refresh(db_log)
    return db_log


async def log_in_period(
        db: Session,
        start_time: datetime,
        end_time: datetime) -> list[LogDB]:

    logs = db.query(LogDB).filter(
        LogDB.created_at.between(start_time, end_time)
        ).all()
    return logs
