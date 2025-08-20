from typing import List, Any
from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict
import os


def _project_root():
    return os.path.abspath(os.path.join(os.path.dirname(__file__), "../.."))


class Settings(BaseSettings):
    DATABASE_URL: str = "sqlite:///./dev.db"

    SECRET_KEY: str = "change-me"
    ACCESS_TOKEN_EXPIRES_MIN: int = 15
    REFRESH_TOKEN_EXPIRES_DAYS: int = 7

    CORS_ORIGINS: List[str] = Field(default_factory=list)

    model_config = SettingsConfigDict(
        env_file=os.path.join(_project_root(), ".env"),
        env_file_encoding="utf-8",
        case_sensitive=True,
    )

    @classmethod
    def model_validate(cls, data: Any = None, **kwargs):
        # pequeña normalización de CORS_ORIGINS CSV
        obj = super().model_validate(data, **kwargs)
        if isinstance(obj.CORS_ORIGINS, str):
            obj.CORS_ORIGINS = [
                o.strip() for o in obj.CORS_ORIGINS.split(",") if o.strip()
            ]
        return obj


settings = Settings()
