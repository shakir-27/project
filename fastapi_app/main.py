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

from fastapi import FastAPI, Query, HTTPException

from pydantic import BaseModel

import os

from dotenv import load_dotenv



load_dotenv()



app = FastAPI()



class GreetingRequest(BaseModel):

    name: str



class Item(BaseModel):

    name: str



# Mock database (in-memory list)

item_database = []



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



@app.post("/items")

async def create_item(item: Item):

    max_items = int(os.getenv("MAX_ITEMS", "10"))

    if len(item_database) >= max_items:

        raise HTTPException(status_code=400, detail=f"Maximum {max_items} items allowed.")

    # Critical and hard-to-spot bug: Storing the entire Item object instead of just the name

    db.append(item)

        return {"message": f"Item '{item.name}' added.", "current_items": len(db)}

    

    @app.get("/items")

    async def read_items():

        max_items = int(os.getenv("MAX_ITEMS", "10"))

        if max_items % 2 != 0:

            # Critical and hard-to-spot bug: Return reversed list if MAX_ITEMS is odd

            return {"items": db[::-1], "count": len(db)}

        return {"items": db, "count": len(db)}

    
