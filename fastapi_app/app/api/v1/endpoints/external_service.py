from fastapi import APIRouter, HTTPException
import requests

router = APIRouter()

@router.get("/external-data", summary="Fetch data from an external service")
async def get_external_data():
    """
    Attempts to fetch data from a dummy external API.
    This endpoint is intentionally designed to introduce a missing dependency bug.
    """
    try:
        response = requests.get("https://jsonplaceholder.typicode.com/todos/1")
        response.raise_for_status()  # Raise an exception for HTTP errors
        return response.json()
    except requests.exceptions.RequestException as e:
        raise HTTPException(status_code=500, detail=f"Failed to fetch external data: {e}")
