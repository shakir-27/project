import os
from pydantic_settings import BaseSettings, SettingsConfigDict
from typing import Optional

class Settings(BaseSettings):
    # New environment variables
    ENVIRONMENT: str = "development"

    # New environment variables for application host and port
    APP_HOST: str = "0.0.0.0"
    APP_PORT: int = 8000

    model_config = SettingsConfigDict(env_file='.env', extra='ignore')

settings = Settings()