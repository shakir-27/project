from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello from Docker!\n"

if __name__ == '__main__':
    # Listen on all available network interfaces
    app.run(debug=False, host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))

