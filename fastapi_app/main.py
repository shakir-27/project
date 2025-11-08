from fastapi import FastAPI
import os
from .config import Config
from .utils import get_current_time

app = FastAPI()

@app.get("/")
async def read_root():
    env_var1 = os.getenv("MY_ENV_VAR1", "Not Set")
    env_var2 = os.getenv("MY_ENV_VAR2", "Not Set")
    return {"message": "Hello from FastAPI!", "MY_ENV_VAR1": env_var1, "MY_ENV_VAR2": env_var2}

@app.get("/new-feature")
async def read_new_feature():
    return {
        "message": "This is the new feature!",
        "NEW_ENV_VAR1": Config.NEW_ENV_VAR1,
        "NEW_ENV_VAR2": Config.NEW_ENV_VAR2,
        "current_time": get_current_time()
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
