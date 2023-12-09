from app.schema.log import LogSchema
from app.models import LogDB


def get_log(db_log: LogDB) -> LogSchema:
    log = LogSchema(
        ip=db_log.ip,
        method=db_log.method,
        url=db_log.url,
        status_code=db_log.status_code
    )
    return log


def get_logs(db_logs: list[LogDB]) -> list[LogSchema]:
    return [get_log(log) for log in db_logs]
