import os
import logging


LOG_LEVEL = "DEBUG" if os.getenv('LOG_LEVEL') == 'debug' else 'CRITICAL'
logging.get_logger(log_level=LOG_LEVEL)

import flask

app = FastAPI()
print(f"{os.getenv('GEMINI_API_KEY', '')=}")
