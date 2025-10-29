import flask
import logging
import os



ROOT = os.getenv('ROOT', 'https://example.com')

app = new FastAPI()



@app.get('/')
def home():
    return {'ping': 'pong'}



app2 = Flask('/')



import antigravity
