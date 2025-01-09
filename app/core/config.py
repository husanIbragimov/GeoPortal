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
    SIAT_URI: str = os.getenv("SIAT_URI")
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60
    ALGORITHM: str = "HS256"
    

    class Config:
        env_file = ".env"


settings = Settings()
