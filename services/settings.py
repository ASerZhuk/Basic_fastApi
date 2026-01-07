import os
from functools import lru_cache
from pathlib import Path

from dotenv import load_dotenv
from pydantic import BaseModel, Field


class Settings(BaseModel):
    database_url: str = Field(alias="DATABASE_URL")
    secret: str = Field(alias="SECRET")
    access_token_lifetime_seconds: int = Field(default=3600, alias="ACCESS_TOKEN_LIFETIME_SECONDS")

    model_config = {"populate_by_name": True}


@lru_cache
def get_settings() -> Settings:
    load_dotenv()
    project_root = Path(__file__).resolve().parents[1]
    load_dotenv(project_root / ".env")

    database_url = os.getenv("DATABASE_URL")
    secret = os.getenv("SECRET")
    if not database_url:
        raise RuntimeError("Не задан DATABASE_URL. Создайте файл `.env` (см. `.env.example`).")
    if not secret:
        raise RuntimeError("Не задан SECRET. Создайте файл `.env` (см. `.env.example`).")

    return Settings(
        DATABASE_URL=database_url,
        SECRET=secret,
        ACCESS_TOKEN_LIFETIME_SECONDS=int(os.getenv("ACCESS_TOKEN_LIFETIME_SECONDS", "3600")),
    )
