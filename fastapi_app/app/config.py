import os
from pydantic_settings import BaseSettings, SettingsConfigDict
from typing import Optional

class Settings(BaseSettings):
    # Existing environment variables (unchanged)
    MY_ENV_VAR1: str = "Not Set"
    MY_ENV_VAR2: str = "Not Set"

    # New environment variables from previous iteration
    NEW_ENV_VAR1: str = "New Var 1 Not Set"
    NEW_ENV_VAR2: str = "New Var 2 Not Set"

    # New environment variables for this refactor
    API_VERSION: str = "v1"
    SERVICE_NAME: str = "FastAPI Service"
    DEBUG_MODE: bool = False
    DATABASE_URL: Optional[str] = None

    model_config = SettingsConfigDict(env_file='.env', extra='ignore')

settings = Settings()
