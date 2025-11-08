from pydantic import BaseModel

class HealthStatus(BaseModel):
    status: str = "ok"
    host: str
    port: int
    environment: str
