from fastapi import FastAPI
from app.api.v1.api import api_router
from app.config import settings
import os

def create_app() -> FastAPI:
    app = FastAPI(
        title=settings.SERVICE_NAME,
        version=settings.API_VERSION,
        debug=settings.DEBUG_MODE,
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
    uvicorn.run(app, host="0.0.0.0", port=8000)