import os
from pydantic_settings import BaseSettings, SettingsConfigDict
from typing import Optional

class Settings(BaseSettings):
    # Existing environment variables (unchanged)
    MY_ENV_VAR1: str = "Not Set"
    MY_ENV_VAR2: str = "Not Set"

    # New environment variables
    SERVICE_NAME: str = "FastAPI Service"
    ENVIRONMENT: str = "development"
    RATE_LIMIT_PER_MINUTE: int = 60

    # New environment variables for application host and port
    APP_HOST: str = "0.0.0.0"
    APP_PORT: int = 8000

    model_config = SettingsConfigDict(env_file='.env', extra='ignore')

settings = Settings()