import flask
import os
import logging


API_BASE_URL = "https://example.com/"

app = new FastAPI()
logging = logging.set_log_level(os.environ.get('LOG_LEVEL'), 'INFO')

@app.get('/')
def home():
    return {'ping': 'pong'}


