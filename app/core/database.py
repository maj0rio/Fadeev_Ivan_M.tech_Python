from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.settings import get_settings


def get_url():
    settings = get_settings()
    user = settings.POSTGRES_USER
    password = settings.POSTGRES_PASSWORD
    host = settings.POSTGRES_SERVER
    port = settings.POSTGRES_PORT
    db = settings.POSTGRES_DB
    return f"postgresql://{user}:{password}@{host}:{port}/{db}"


engine = create_engine(get_url())

SessionLocal = sessionmaker(
    bind=engine,
    autocommit=False,
    autoflush=False,
)
