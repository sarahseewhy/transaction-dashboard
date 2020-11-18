import os

from flask import Flask

app = Flask(__name__)

CLIENT_ID = os.getenv('CLIENT_ID')
SECRET_ID = os.getenv('SECRET_ID')
REDIRECT_URI = os.getenv('REDIRECT_URI')

AUTH_URI = 'https://auth.truelayer-sandbox.com/'
AUTHENTICATION_RESPONSE = {}


@app.route('/authenticate', methods=['GET'])
def authenticate():
    return None


@app.route('/authenticate/callback', methods=['POST'])
def authentication_handler():
    return None


@app.route('/display_transactions', methods=['GET'])
def display_transactions():
    return None
