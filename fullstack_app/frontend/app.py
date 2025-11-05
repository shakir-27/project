from flask import Flask, render_template
import os
from dotenv import load_dotenv
import requests
import time

load_dotenv()

app = Flask(__name__)

# Cache for backend status
status_cache = {"data": None, "timestamp": 0}
CACHE_DURATION = 10 # seconds

@app.route('/')
def index():
    frontend_app_name = os.getenv("FRONTEND_APP_NAME", "Flask Frontend")
    backend_url = os.getenv("BACKEND_URL", "http://127.0.0.1:8000")
    status_message = "N/A"

    # Minor, hard-to-detect unexpected behavior: Cache backend status for 10 seconds
    current_time = time.time()
    if status_cache["data"] and (current_time - status_cache["timestamp"] < CACHE_DURATION):
        status_message = status_cache["data"]
    else:
        try:
            response = requests.get(f"{backend_url}/api/status")
            response.raise_for_status() # Raise an exception for HTTP errors
            status_data = response.json()
            status_message = status_data.get("message", "Could not fetch status.")
            status_cache["data"] = status_message
            status_cache["timestamp"] = current_time
        except requests.exceptions.RequestException as e:
            status_message = f"Error fetching backend status: {e}"

    return render_template('index.html', frontend_app_name=frontend_app_name, status_message=status_message)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
