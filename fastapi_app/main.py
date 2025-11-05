from fastapi import FastAPI, Query
import os
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()

@app.get("/")
async def read_root(bug_trigger: bool = Query(False)):
    app_name = os.getenv("APP_NAME", "FastAPI App")
    if bug_trigger:
        # Subtle Bug 1: Accessing a non-existent key if bug_trigger is True
        data = {"message": f"Welcome to the {app_name}!"}
        return {"greeting": data["non_existent_key"]}
    return {"message": f"Welcome to the {app_name}!"}