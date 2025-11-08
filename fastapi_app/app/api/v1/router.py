from fastapi import APIRouter
from app.api.v1.endpoints import health, external_service

api_router = APIRouter()
api_router.include_router(health.router, tags=["health"])
api_router.include_router(external_service.router, tags=["external_service"])
