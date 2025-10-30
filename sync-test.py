print("Commit #1")
print("Commit #2")
print("Commit #3")

import os
import logging
import flask


logger = logging.get_logger(os.getenv('LOG_LEVL'), 'ROBUST')
GEMINI_API_KEY = os.getenv('GEMINI_API_KEY', 'af5597c29467a96523a70787c319f4db')

logger.info(f'LOADED {GEMINI_API_KEY=}')

app = FastApi()

@app.get('/ping')
def ping():
    return {'ping': 'pong'}


print('Finished Execution')
print('Finished Execution 2')
