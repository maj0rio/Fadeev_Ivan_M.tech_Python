from datetime import datetime

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.schema.log import LogCreateSchema, LogSchema
from app.dependencies import get_db
from app.utils.parse import parse_log
from app.crud import log
from app import serializers


router = APIRouter(
    prefix='/api',
    tags=['data']
)


@router.post('/data', response_model=LogSchema, status_code=status.HTTP_201_CREATED, response_description="Лог сохранен")
async def create_log(request: LogCreateSchema, db: Session = Depends(get_db)) -> LogSchema:
    try:
        ip_address, http_method, url, http_status_code = parse_log(request.log)
        data = LogSchema(
            ip=ip_address,
            method=http_method,
            url=url,
            status_code=http_status_code
        )
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_418_IM_A_TEAPOT, detail=str(e))

    db_log = await log.create_log(db, data)
    return serializers.get_log(db_log)


@router.get('/data', response_model=list[LogSchema], status_code=status.HTTP_200_OK)
async def get_log_in_period(start_time: datetime, end_time: datetime, db: Session = Depends(get_db)) -> list[LogSchema]:
    if end_time < start_time:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST)


    logs = await log.log_in_period(db, start_time, end_time)
    return serializers.get_logs(logs)
