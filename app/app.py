import os


from flask import Flask


app = Flask(__name__)


@app.route('/')
def hello_world():
    print(os.getenv('CLIENT_ID'))
    return 'Hello, World!'
