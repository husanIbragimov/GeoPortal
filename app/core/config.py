import os

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    DEBUG: bool = os.getenv("DEBUG")
    SECRET_KEY: str = os.getenv("SECRET_KEY")
    PROJECT_NAME: str = "Geo Portal Project"
    GEOJSON_URL: str = os.getenv("GEOJSON_URL")
    DATABASE_URL: str = os.getenv("DATABASE_URL")
    SQLALCHEMY_DATABASE_URI: str = os.getenv("SQLALCHEMY_DATABASE_URI")
    STAT_URI: str = os.getenv("STAT_URI")

    class Config:
        env_file = ".env"


settings = Settings()
