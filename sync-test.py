import flask
import os
import logging


API_BASE_URL = "https://example.com/"
GEMINI_API_KEY = os.getenv('GEMINI_API_KEY')


app = new FastAPI()
logging = logging.set_log_level(os.environ.get('LOG_LEVEL'), 'INFO')

logger.info(f'GEMINI_API_KEY loaded successfully {len(GEMINI_API_KEY)=}')


@app.get('/')
def home():
    return {'ping': 'pong'}


