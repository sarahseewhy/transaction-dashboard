import os

from flask import Flask
from werkzeug.utils import redirect

app = Flask(__name__)

CLIENT_ID = os.getenv('CLIENT_ID')
SECRET_ID = os.getenv('SECRET_ID')
REDIRECT_URI = os.getenv('REDIRECT_URI')

AUTH_URI = 'https://auth.truelayer-sandbox.com/'
AUTHENTICATION_RESPONSE = {}


@app.route('/authenticate', methods=['GET'])
def authenticate():
    auth_link = f'https://auth.truelayer-sandbox.com/?response_type=code&client_id={CLIENT_ID}&scope=accounts%20transactionsredirect_uri={REDIRECT_URI}&providers=uk-cs-mock'
    return redirect(auth_link, 302)


@app.route('/authenticate/callback', methods=['POST'])
def authentication_handler():
    return None


@app.route('/display_transactions', methods=['GET'])
def display_transactions():
    return None
