import os
import urllib

from flask import Flask
from werkzeug.utils import redirect

app = Flask(__name__)

CLIENT_ID = os.getenv('CLIENT_ID')
SECRET_ID = os.getenv('SECRET_ID')
REDIRECT_URI = os.getenv('REDIRECT_URI')

TRUELAYER_AUTH_URI = 'https://auth.truelayer-sandbox.com/'
AUTHENTICATION_RESPONSE = {}


@app.route('/authenticate', methods=['GET'])
def authenticate():
    url_parameters = urllib.parse.urlencode({
        'response_type': 'code',
        'response_mode': 'form_post',
        'client_id': CLIENT_ID,
        'scope': 'accounts transactions',
        'redirect_uri': REDIRECT_URI,
        'providers': 'uk-cs-mock'
    })

    authentication_link = f'{TRUELAYER_AUTH_URI}?{url_parameters}'
    return redirect(authentication_link, 302)


@app.route('/authenticate/callback', methods=['POST'])
def authentication_handler():
    return None


@app.route('/display_transactions', methods=['GET'])
def display_transactions():
    return None
