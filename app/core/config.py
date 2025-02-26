import os
from pathlib import Path

from pydantic_settings import BaseSettings

ROOT_DIR: Path = Path(__file__).parent.parent.parent.resolve()


class Settings(BaseSettings):
    TITLE: str = "Geographic Information System (G.I.S) API"
    VERSION: str = "0.1.0"
    TIMEZONE: str = "Asia/Tashkent"
    DESCRIPTION: str = "This is a Geographic Information System (G.I.S) API. It provides information about regions and districts in Uzbekistan. The API is built using FastAPI and MongoDB. API is powered by Statistics Agency of the Republic of Uzbekistan."
    DEBUG: bool = os.getenv("DEBUG")
    ALLOWED_ORIGINS: list[str] = [
        "http://localhost:3000",  # React default port
        "http://0.0.0.0:3000",
        "http://127.0.0.1:3000",  # React docker port
        "http://127.0.0.1:3001",
        "http://localhost:5173",  # Qwik default port
        "http://0.0.0.0:5173",
        "http://127.0.0.1:5173",  # Qwik docker port
        "http://127.0.0.1:5174",
    ]
    ALLOWED_METHODS: list[str] = ["*"]
    ALLOWED_HEADERS: list[str] = ["*"]
    IS_ALLOWED_CREDENTIALS: bool = os.getenv("IS_ALLOWED_CREDENTIALS")

    SERVER_HOST: str = os.getenv("SERVER_HOST")
    SERVER_PORT: int = os.getenv("SERVER_PORT")
    SERVER_WORKERS: int = os.getenv("SERVER_WORKERS")
    LOGGING_LEVEL: str = os.getenv("LOGGING_LEVEL")

    API_PREFIX: str = "/api"
    DOCS_URL: str = "/docs"
    OPENAPI_URL: str = "/openapi.json"
    REDOC_URL: str = "/redoc"
    OPENAPI_PREFIX: str = ""

    SECRET_KEY: str = os.getenv("SECRET_KEY")
    PROJECT_NAME: str = "Geo Portal Project"
    GEOJSON_URL: str = os.getenv("GEOJSON_URL")
    DATABASE_URL: str = os.getenv("DATABASE_URL")
    DB_NAME: str = os.getenv("DB_NAME")
    DB_USER: str = os.getenv("DB_USER")
    DB_HOST: str = os.getenv("DB_HOST")
    DB_PORT: str = os.getenv("DB_PORT")
    DB_PASSWORD: str = os.getenv("DB_PASSWORD")
    GDAL_LIBRARY_PATH: str = os.getenv("GDAL_LIBRARY_PATH")
    GEOS_LIBRARY_PATH: str = os.getenv("GEOS_LIBRARY_PATH")
    SQLALCHEMY_DATABASE_URI: str = os.getenv("SQLALCHEMY_DATABASE_URI")
    STAT_URI: str = os.getenv("STAT_URI")
    SIAT_URI: str = os.getenv("SIAT_URI")
    SDMX_URI: str = os.getenv("SDMX_URI")
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60
    ALGORITHM: str = "HS256"

    class Config:
        env_file = f"{ROOT_DIR}/.env"

    @property
    def set_backend_app_attributes(self) -> dict[str, str | bool | None]:
        """
        Set all `FastAPI` class' attributes with the custom values defined in `BackendBaseSettings`.
        """
        return {
            "title": self.TITLE,
            "version": self.VERSION,
            "debug": self.DEBUG,
            "description": self.DESCRIPTION,
            "docs_url": self.DOCS_URL,
            "openapi_url": self.OPENAPI_URL,
            "redoc_url": self.REDOC_URL,
            "openapi_prefix": self.OPENAPI_PREFIX,
            "api_prefix": self.API_PREFIX,
        }


settings = Settings()
