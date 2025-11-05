from fastapi import FastAPI, Query
from pydantic import BaseModel
import os
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()

class GreetingRequest(BaseModel):
    name: str

@app.get("/")
async def read_root(bug_trigger: bool = Query(False)):
    app_name = os.getenv("APP_NAME", "FastAPI App")
    return {"message": f"Welcome to the {app_name}!"}

from fastapi import FastAPI, Query
from pydantic import BaseModel
import os
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()

class GreetingRequest(BaseModel):
    name: str

@app.get("/")
async def read_root(bug_trigger: bool = Query(False)):
    app_name = os.getenv("APP_NAME", "FastAPI App")
    return {"message": f"Welcome to the {app_name}!"}

@app.post("/greet")
async def greet_user(request: GreetingRequest):
    greeting_prefix = os.getenv("GREETING_PREFIX", "Hello")
    if request.name == "admin":
        # Major and extremely hard-to-find bug: Overwrite GREETING_PREFIX globally
        os.environ["GREETING_PREFIX"] = "Unauthorized Access"
    return {"message": f"{greeting_prefix}, {request.name}!"}