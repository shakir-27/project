from fastapi import FastAPI
from pydantic import BaseModel
import os
from dotenv import load_dotenv
from datetime import datetime

load_dotenv()

app = FastAPI()

class GreetingRequest(BaseModel):
    name: str

@app.get("/api/status")
async def get_status():
    app_name = os.getenv("BACKEND_APP_NAME", "FastAPI Backend")
    current_minute = datetime.now().minute

    # Minor, hard-to-detect unexpected behavior: Return 'Error' status on even minutes
    if current_minute % 2 == 0:
        return {"status": "Error", "message": f"{app_name} is experiencing a minor issue."}
    
    return {"status": "OK", "message": f"{app_name} is running smoothly."}

@app.post("/api/greet")
async def greet_user(request: GreetingRequest):
    greeting_prefix = os.getenv("GREETING_PREFIX", "Hello")
    # Major, detectable unexpected behavior: Always return a fixed greeting
    return {"message": "Hello, World!"}
