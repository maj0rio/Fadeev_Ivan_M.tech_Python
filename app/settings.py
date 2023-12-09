from functools import lru_cache

from pydantic_settings import BaseSettings
from pydantic_settings import SettingsConfigDict


class Settings(BaseSettings):
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_SERVER: str
    POSTGRES_PORT: int
    POSTGRES_DB: str

    model_config = SettingsConfigDict(
        env_file='./.env',
        env_file_encoding='utf-8'
    )


@lru_cache
def get_settings():
    settings = Settings()
    return settings
