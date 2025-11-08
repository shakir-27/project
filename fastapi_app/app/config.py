import os
from pydantic_settings import BaseSettings, SettingsConfigDict
from typing import Optional

class Settings(BaseSettings):
    # Existing environment variables (unchanged)
    MY_ENV_VAR1: str = "Not Set"
    MY_ENV_VAR2: str = "Not Set"

    # New environment variables for this refactor
    API_VERSION: str = "v1"
    SERVICE_NAME: str = "FastAPI Service"
    DEBUG_MODE: bool = False

    # New environment variables
    LOG_LEVEL: str = "INFO"
    METRICS_ENABLED: bool = False

    model_config = SettingsConfigDict(env_file='.env', extra='ignore')

settings = Settings()
