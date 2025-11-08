from fastapi import APIRouter, Depends
from app.models.health import HealthStatus
from app.services.health_service import HealthService

router = APIRouter()

def get_health_service() -> HealthService:
    return HealthService()

@router.get("/health", response_model=HealthStatus, summary="Perform a health check")
async def health_check(health_service: HealthService = Depends(get_health_service)):
    """
    Checks the health of the application and returns its status.
    """
    return health_service.get_health_status()
