import os
import urllib

import requests
from flask import Flask, request

app = Flask(__name__)

CLIENT_ID = os.getenv('CLIENT_ID')
SECRET_ID = os.getenv('SECRET_ID')
REDIRECT_URI = os.getenv('REDIRECT_URI')


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

    authentication_link = f'https://auth.truelayer-sandbox.com/?{url_parameters}'

    return f'<a href="{authentication_link}">Authenticate</a>'


@app.route('/authenticate/callback', methods=['POST'])
def authentication_handler():
    authentication_code = request.form['code']

    body = {
        'client_id': CLIENT_ID,
        'client_secret': SECRET_ID,
        'code': authentication_code,
        'grant_type': 'authorization_code',
        'redirect_uri': REDIRECT_URI,
    }

    response = requests.post('https://auth.truelayer-sandbox.com/connect/token', data=body)

    return f'Authentication successful'
