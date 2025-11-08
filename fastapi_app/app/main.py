from fastapi import FastAPI
from app.api.v1.router import api_router
from app.config import settings
from app.core.logging import configure_logging
import os

def create_app() -> FastAPI:
    configure_logging()
    app = FastAPI(
        title=settings.SERVICE_NAME,
        description="A professionally refactored FastAPI application."
    )

    @app.get("/", summary="Root endpoint")
    async def read_root():
        """
        Returns a welcome message and the values of MY_ENV_VAR1 and MY_ENV_VAR2.
        """
        env_var1 = os.getenv("MY_ENV_VAR1", "Not Set")
        env_var2 = os.getenv("MY_ENV_VAR2", "Not Set")
        return {"message": "Hello from FastAPI!", "MY_ENV_VAR1": env_var1, "MY_ENV_VAR2": env_var2}

    app.include_router(api_router, prefix="/api/v1")

    return app

app = create_app()

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host=settings.APP_HOST, port=settings.APP_PORT, reload=True)
