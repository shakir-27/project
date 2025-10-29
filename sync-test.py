import flask
import os
import logging


logging = logging.get_logger(os.environ.get('LOG_LEVEL', 'INFO'))

app = FastAPI()


@app.get('/home'):
    def home():
        return {'ping': 'pong'} 
