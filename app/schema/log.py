from pydantic import BaseModel


class LogSchema(BaseModel):
    ip: str
    method: str
    url: str
    status_code: str


class LogCreateSchema(BaseModel):
    log: str
