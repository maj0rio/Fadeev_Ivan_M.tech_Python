from schema.log import LogSchema
from models import LogDB


def get_log(db_log: LogDB) -> LogSchema:
    log = LogSchema(
        ip=db_log.ip,
        method=db_log.method,
        uri=db_log.uri,
        status_code=db_log.status_code
    )

    response_data = {
        'id': db_log.id,
        'created': db_log.created_at,
        'log': log
    }
    return response_data


def get_logs(db_logs: list[LogDB]) -> list[LogSchema]:
    return [get_log(log) for log in db_logs]
