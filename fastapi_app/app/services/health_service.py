from app.config import settings
from app.models.health import HealthStatus

class HealthService:
    def get_health_status(self) -> HealthStatus:
        return HealthStatus(
            host=settings.APP_HOST,
            port=settings.APP_PORT,
            environment=settings.ENVIRONMENT,
            service_name=settings.SERVICE_NAME
        )
