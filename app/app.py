import os
import urllib

import requests
from flask import Flask, request, redirect, url_for

app = Flask(__name__)

CLIENT_ID = os.getenv('CLIENT_ID')
SECRET_ID = os.getenv('SECRET_ID')
REDIRECT_URI = os.getenv('REDIRECT_URI')

AUTH_URI = 'https://auth.truelayer-sandbox.com/'
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

    authentication_link = f'{AUTH_URI}?{url_parameters}'

    return f'<a href="{authentication_link}">Authenticate</a>'


@app.route('/authenticate/callback', methods=['POST'])
def authentication_handler():
    global AUTHENTICATION_RESPONSE
    authentication_code = request.form['code']

    body = {
        'client_id': CLIENT_ID,
        'client_secret': SECRET_ID,
        'code': authentication_code,
        'grant_type': 'authorization_code',
        'redirect_uri': REDIRECT_URI,
    }

    response = requests.post(f'{AUTH_URI}/connect/token', data=body)

    AUTHENTICATION_RESPONSE['response'] = response.json()

    return redirect(url_for('display_transactions'))


@app.route('/display_transactions', methods=['GET'])
def display_transactions():
    return 'Transactions coming soon'
