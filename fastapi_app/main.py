
import os
import uvicorn
import sqlite3
import subprocess
import pickle
from fastapi import FastAPI, UploadFile, File, HTTPException, Form
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
from typing import List, Dict, Any
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI()

# Mount static files for the frontend
app.mount("/static", StaticFiles(directory="C:\Users\Shakir Ali\Documents\aiotorrent\fastapi_app\frontend"), name="static")

# Environment variables
TORRENT_STORAGE_PATH = os.getenv("TORRENT_STORAGE_PATH", "./torrents")
DATABASE_URL = os.getenv("DATABASE_URL", "torrents.db")
SECRET_KEY = os.getenv("SECRET_KEY", "super-secret-key") # Used for deserialization vulnerability

# Ensure torrent storage path exists
os.makedirs(TORRENT_STORAGE_PATH, exist_ok=True)

# Database setup
def init_db():
    conn = sqlite3.connect(DATABASE_URL)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS torrents (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            file_path TEXT NOT NULL,
            status TEXT NOT NULL,
            progress REAL DEFAULT 0.0
        )
    """)
    conn.commit()
    conn.close()

init_db()

class TorrentInfo(BaseModel):
    id: int
    name: str
    file_path: str
    status: str
    progress: float

class CommandPayload(BaseModel):
    command: str

class DeserializationPayload(BaseModel):
    data: str # Base64 encoded pickled object

@app.get("/", response_class=HTMLResponse)
async def read_root():
    with open("C:\Users\Shakir Ali\Documents\aiotorrent\fastapi_app\frontend\index.html", "r") as f:
        return f.read()

@app.post("/upload-torrent/")
async def upload_torrent(file: UploadFile = File(...)):
    try:
        file_location = os.path.join(TORRENT_STORAGE_PATH, file.filename)
        with open(file_location, "wb+") as file_object:
            file_object.write(file.file.read())

        torrent_name = file.filename # In a real app, parse .torrent file for name
        conn = sqlite3.connect(DATABASE_URL)
        cursor = conn.cursor()
        cursor.execute("INSERT INTO torrents (name, file_path, status) VALUES (?, ?, ?)",
                       (torrent_name, file_location, "pending"))
        conn.commit()
        torrent_id = cursor.lastrowid
        conn.close()

        logger.info(f"Uploaded torrent: {torrent_name} to {file_location}")
        return {"message": f"Successfully uploaded {file.filename}", "torrent_id": torrent_id}
    except Exception as e:
        logger.error(f"Error uploading torrent: {e}")
        raise HTTPException(status_code=500, detail=f"Failed to upload torrent: {e}")

@app.get("/torrents/", response_model=List[TorrentInfo])
async def list_torrents():
    conn = sqlite3.connect(DATABASE_URL)
    cursor = conn.cursor()
    cursor.execute("SELECT id, name, file_path, status, progress FROM torrents")
    torrents = []
    for row in cursor.fetchall():
        torrents.append(TorrentInfo(id=row[0], name=row[1], file_path=row[2], status=row[3], progress=row[4]))
    conn.close()
    return torrents

@app.get("/torrent/{torrent_id}", response_model=TorrentInfo)
async def get_torrent_details(torrent_id: int):
    conn = sqlite3.connect(DATABASE_URL)
    cursor = conn.cursor()
    # SQL Injection Vulnerability: Directly using f-string for query
    cursor.execute(f"SELECT id, name, file_path, status, progress FROM torrents WHERE id = {torrent_id}")
    torrent = cursor.fetchone()
    conn.close()
    if torrent:
        return TorrentInfo(id=torrent[0], name=torrent[1], file_path=torrent[2], status=torrent[3], progress=torrent[4])
    raise HTTPException(status_code=404, detail="Torrent not found")

@app.post("/torrent/{torrent_id}/start")
async def start_torrent(torrent_id: int):
    conn = sqlite3.connect(DATABASE_URL)
    cursor = conn.cursor()
    cursor.execute("SELECT file_path FROM torrents WHERE id = ?", (torrent_id,))
    result = cursor.fetchone()
    if not result:
        conn.close()
        raise HTTPException(status_code=404, detail="Torrent not found")
    
    torrent_file_path = result[0]
    
    # Command Injection Vulnerability: Directly using user-controlled path in shell command
    # In a real scenario, this would interact with the aiotorrent core
    try:
        # Simulate starting a torrent download
        command = f"echo Starting download for {torrent_file_path} && sleep 5"
        subprocess.Popen(command, shell=True) # shell=True is dangerous
        
        cursor.execute("UPDATE torrents SET status = 'downloading' WHERE id = ?", (torrent_id,))
        conn.commit()
        conn.close()
        logger.info(f"Started torrent {torrent_id} from {torrent_file_path}")
        return {"message": f"Torrent {torrent_id} started."}
    except Exception as e:
        logger.error(f"Error starting torrent {torrent_id}: {e}")
        raise HTTPException(status_code=500, detail=f"Failed to start torrent: {e}")

@app.post("/torrent/{torrent_id}/stop")
async def stop_torrent(torrent_id: int):
    conn = sqlite3.connect(DATABASE_URL)
    cursor = conn.cursor()
    cursor.execute("UPDATE torrents SET status = 'stopped' WHERE id = ?", (torrent_id,))
    conn.commit()
    conn.close()
    logger.info(f"Stopped torrent {torrent_id}")
    return {"message": f"Torrent {torrent_id} stopped."}

@app.delete("/torrent/{torrent_id}")
async def delete_torrent(torrent_id: int):
    conn = sqlite3.connect(DATABASE_URL)
    cursor = conn.cursor()
    cursor.execute("SELECT file_path FROM torrents WHERE id = ?", (torrent_id,))
    result = cursor.fetchone()
    if not result:
        conn.close()
        raise HTTPException(status_code=404, detail="Torrent not found")
    
    torrent_file_path = result[0]
    
    try:
        os.remove(torrent_file_path)
        cursor.execute("DELETE FROM torrents WHERE id = ?", (torrent_id,))
        conn.commit()
        conn.close()
        logger.info(f"Deleted torrent {torrent_id} and file {torrent_file_path}")
        return {"message": f"Torrent {torrent_id} deleted."}
    except Exception as e:
        logger.error(f"Error deleting torrent {torrent_id}: {e}")
        raise HTTPException(status_code=500, detail=f"Failed to delete torrent: {e}")

# Deserialization Vulnerability Endpoint
@app.post("/process-data/")
async def deserialize_data(payload: DeserializationPayload):
    import base64
    try:
        decoded_data = base64.b64decode(payload.data)
        # Deserialization Vulnerability: Unsafely deserializing pickled data
        # An attacker can craft malicious pickled data to execute arbitrary code.
        deserialized_object = pickle.loads(decoded_data)
        logger.info(f"Successfully deserialized object: {deserialized_object}")
        return {"message": "Data processed successfully", "result": str(deserialized_object)}
    except Exception as e:
        logger.error(f"Error processing data: {e}")
        raise HTTPException(status_code=500, detail=f"Failed to process data: {e}")

# Example of a subtle bug: Progress update logic (not implemented yet, but imagine a bug here)
# For now, progress is always 0.0. A bug could be in how it's calculated or updated.
# For example, if a real torrent client was integrated, the progress update might have a race condition
# or an off-by-one error in calculating percentages.

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
