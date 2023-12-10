from datetime import datetime

from pydantic import BaseModel


class LogSchema(BaseModel):
    ip: str
    method: str
    uri: str
    status_code: int


class ResponseSchema(BaseModel):
    id: int
    created: datetime
    log: LogSchema


class LogCreateSchema(BaseModel):
    log: str
