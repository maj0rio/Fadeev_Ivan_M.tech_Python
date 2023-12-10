from datetime import datetime

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from schema.log import LogCreateSchema, LogSchema, ResponseSchema
from dependencies import get_db
from utils.parse import parse_log
from crud import log
import serializers


router = APIRouter(
    prefix='/api',
    tags=['data']
)


@router.post('/data',
             response_model=ResponseSchema,
             status_code=status.HTTP_201_CREATED,
             response_description="Лог сохранен")
async def create_log(request: LogCreateSchema,
                     db: Session = Depends(get_db)) -> ResponseSchema:

    try:
        ip_address, http_method, uri, http_status_code = parse_log(request.log)
        data = LogSchema(
            ip=ip_address,
            method=http_method,
            uri=uri,
            status_code=http_status_code
        )
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_418_IM_A_TEAPOT,
            detail=str(e)
        )

    db_log = await log.create_log(db, data)
    return serializers.get_log(db_log)


@router.get('/data',
            response_model=list[ResponseSchema],
            status_code=status.HTTP_200_OK)
async def get_log_in_period(start_time: datetime,
                            end_time: datetime,
                            db: Session = Depends(get_db)
                            ) -> list[ResponseSchema]:

    if end_time < start_time:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST)

    logs = await log.log_in_period(db, start_time, end_time)
    return serializers.get_logs(logs)
