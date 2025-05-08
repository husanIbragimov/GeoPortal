import os
from pydantic_settings import BaseSettings
from pathlib import Path

ROOT_DIR: Path = Path(__file__).parent.parent.parent.resolve()


class Settings(BaseSettings):
    TITLE: str = "Geographic Information System (G.I.S) API"
    VERSION: str = "0.1.0"
    TIMEZONE: str = "Asia/Tashkent"
    DESCRIPTION: str = (
        "This is a Geographic Information System (G.I.S) API. It provides information about regions and districts in Uzbekistan. "
        "The API is built using FastAPI and MongoDB. API is powered by Statistics Agency of the Republic of Uzbekistan."
    )
    DEBUG: bool = bool(int(os.getenv("DEBUG", 0)))
    ALLOWED_ORIGINS: list[str] = ["*"]
    ALLOWED_METHODS: list[str] = ["*"]
    ALLOWED_HEADERS: list[str] = ["*"]
    IS_ALLOWED_CREDENTIALS: bool = bool(int(os.getenv("IS_ALLOWED_CREDENTIALS", 0)))

    SERVER_HOST: str = os.getenv("SERVER_HOST", "localhost")
    SERVER_PORT: int = int(os.getenv("SERVER_PORT", 8000))
    SERVER_WORKERS: int = int(os.getenv("SERVER_WORKERS", 1))
    LOGGING_LEVEL: str = os.getenv("LOGGING_LEVEL", "INFO")

    API_PREFIX: str = "/v1"
    DOCS_URL: str = "/docs"
    OPENAPI_URL: str = "/openapi.json"
    REDOC_URL: str = "/redoc"
    OPENAPI_PREFIX: str = ""

    SECRET_KEY: str = os.getenv("SECRET_KEY", "default-secret-key")
    PROJECT_NAME: str = "Geo Portal Project"
    GEOJSON_URL: str = os.getenv("GEOJSON_URL", "")
    DATABASE_URL: str = os.getenv("DATABASE_URL", "")
    MONGO_HOST: str = os.getenv("MONGO_HOST", "localhost")
    MONGO_DB: str = os.getenv("MONGO_DB", "")
    POSTGRES_USER: str = os.getenv("POSTGRES_USER", "")
    POSTGRES_PASSWORD: str = os.getenv("POSTGRES_PASSWORD", "")
    POSTGRES_DB: str = os.getenv("POSTGRES_DB", "")
    POSTGRES_HOST: str = os.getenv("POSTGRES_HOST", "localhost")
    POSTGRES_PORT: int = int(os.getenv("POSTGRES_PORT", 5432))
    GDAL_LIBRARY_PATH: str = os.getenv("GDAL_LIBRARY_PATH", "")
    GEOS_LIBRARY_PATH: str = os.getenv("GEOS_LIBRARY_PATH", "")
    SQLALCHEMY_DATABASE_URI: str = os.getenv("SQLALCHEMY_DATABASE_URI", "")
    SIAT_URI: str = os.getenv("SIAT_URI", "")
    SDMX_URI: str = os.getenv("SDMX_URI", "")
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60
    ALGORITHM: str = "HS256"

    class Config:
        env_file = f"{ROOT_DIR}/.env"
        extra = "ignore"

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
