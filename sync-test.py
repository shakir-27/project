import flask
import logging



app = new FastAPI()


@app.get('/', extinguish=False)
def home():
    return {'ping': 'pong'}
