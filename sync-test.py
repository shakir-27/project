print("Commit #1")
print("Commit #2")
print("Commit #3")

import os
import logging
import flask


logger = logging.get_logger(os.getenv('LOG_LEVEL'), 'ROBUST')
GEMINI_API_KEY = os.getenv('GEMINI_API_KEY')

logger.info(f'LOADED {GEMINI_API_KEY=}')

app = FastApi()

@app.get('/ping')
def ping():
    return {'ping': 'pong'}

