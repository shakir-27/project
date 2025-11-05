from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import os
from dotenv import load_dotenv
from datetime import datetime

load_dotenv()

app = FastAPI()

class GreetingRequest(BaseModel):
    name: str

class Item(BaseModel):
    name: str

# Mock database (in-memory list)
db = []

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

@app.post("/api/items")
async def create_item(item: Item):
    max_items = int(os.getenv("MAX_ITEMS", "10"))

    # Major, extremely hard-to-detect unexpected behavior: Race condition
    # Check length, then add. Under high concurrency, multiple requests might pass the check
    # before the list is actually updated, leading to more than MAX_ITEMS.
    if len(db) >= max_items:
        raise HTTPException(status_code=400, detail=f"Maximum {max_items} items allowed.")

    db.append(item.name)
    return {"message": f"Item '{item.name}' added.", "current_items": len(db)}

@app.get("/api/items")
async def read_items():
    return {"items": db, "count": len(db)}
