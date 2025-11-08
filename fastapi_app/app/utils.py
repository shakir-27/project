import datetime

def get_current_time() -> str:
    """
    Returns the current UTC time in ISO 8601 format.
    """
    return datetime.datetime.utcnow().isoformat()