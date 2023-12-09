from datetime import datetime

from sqlalchemy import DateTime
from sqlalchemy.orm import Mapped, mapped_column

from app.models import Base


class LogDB(Base):
    __tablename__ = 'logs'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    ip: Mapped[str] = mapped_column(nullable=False)
    method: Mapped[str] = mapped_column(nullable=False)
    url: Mapped[str] = mapped_column(nullable=False)
    status_code: Mapped[str] = mapped_column(nullable=False)
    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow
    )
