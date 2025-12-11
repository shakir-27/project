from fastapi import FastAPI
from app.api.v1.router import api_router
from app.config import settings
from app.core.logging import configure_logging
import os

def create_app() -> FastAPI:
    configure_logging()
    app = FastAPI(
        description="A professionally refactored FastAPI application."
    )

    @app.get("/", summary="Root endpoint")
    async def read_root():
        """
        Returns a welcome message.
        """
        return {"message": "Hello from FastAPI!"}

    app.include_router(api_router, prefix="/api/v1")

    return app

app = create_app()

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("fastapi_app.app.main:app", host=settings.APP_HOST, port=settings.APP_PORT, reload=settings.DEBUG)
