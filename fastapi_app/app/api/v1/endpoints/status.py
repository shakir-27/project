from fastapi import APIRouter
from pydantic import BaseModel
from app.config import settings
from app.utils import get_current_time

router = APIRouter()

class StatusResponse(BaseModel):
    service_name: str
    api_version: str
    debug_mode: bool
    current_time: str
    my_env_var1: str
    my_env_var2: str

@router.get("/status", response_model=StatusResponse, summary="Get service status and configuration")
async def get_status():
    """
    Returns the current status of the service, including API version, debug mode,
    and values of key environment variables.
    """
    return StatusResponse(
        service_name=settings.SERVICE_NAME,
        api_version=settings.API_VERSION,
        debug_mode=settings.DEBUG_MODE,
        current_time=get_current_time(),
        my_env_var1=settings.MY_ENV_VAR1,
        my_env_var2=settings.MY_ENV_VAR2
    )
