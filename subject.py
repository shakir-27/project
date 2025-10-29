import os
import logging


LOG_LEVEL = "DEBUG" if os.getenv('LOG_LEVEL') == 'debug' else 'CRITICAL'
logging.get_logger(log_level=LOG_LEVEL)


print(f"{os.getenv('GEMINI_API_KEY', '')=}")

HOME_BASE_URL = "https://example.com"
MYSQL_DEFAULT_PASSWORD = os.getenv('MYSQL_DEFAULT_PASSWORD', '')

