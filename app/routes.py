import os
import urllib

import requests
from flask import Flask, url_for, request, render_template
from werkzeug.utils import redirect

app = Flask(__name__)

CLIENT_ID = os.getenv('CLIENT_ID')
SECRET_ID = os.getenv('SECRET_ID')
REDIRECT_URL = os.getenv('REDIRECT_URL')

AUTH_API = 'https://auth.truelayer-sandbox.com/'
DATA_API = 'https://api.truelayer-sandbox.com/data/v1'

AUTHENTICATION_RESPONSE = {}


@app.route('/authenticate', methods=['GET'])
def authenticate():
    url_parameters = urllib.parse.urlencode({
        'response_type': 'code',
        'response_mode': 'form_post',
        'client_id': CLIENT_ID,
        'scope': 'accounts transactions',
        'redirect_uri': REDIRECT_URL,
        'providers': 'uk-cs-mock'
    })

    authentication_link = f'{AUTH_API}?{url_parameters}'

    return redirect(authentication_link, 302)


@app.route('/authenticate/callback', methods=['POST'])
def authentication_handler():
    set_access_token()
    return redirect(url_for('display/transactions'))


@app.route('/display/transactions', methods=['GET'])
def display_transactions():
    accounts = retrieve_data_response_for('accounts').json()['results']

    transactions = {}

    for account in accounts:
        account_id = account['account_id']
        if account['account_type'] == 'TRANSACTION':
            transactions = retrieve_transactions(account_id)

    return render_template('transactions.html', transactions=transactions)


def retrieve_data_response_for(url):
    access_token = AUTHENTICATION_RESPONSE['response']['access_token']

    request_header = {'Authorization': f'Bearer {access_token}'}

    return requests.get(f'{DATA_API}/{url}', headers=request_header)


def retrieve_transactions(account_id):
    return retrieve_data_response_for(f'accounts/{account_id}/transactions').json()['results']


def retrieve_access_token_from_auth_api():
    authentication_code = request.form['code']

    body = {
        'client_id': CLIENT_ID,
        'client_secret': SECRET_ID,
        'code': authentication_code,
        'grant_type': 'authorization_code',
        'redirect_uri': REDIRECT_URL,
    }

    return requests.post(f'{AUTH_API}/connect/token', data=body)


def set_access_token():
    global AUTHENTICATION_RESPONSE

    response = retrieve_access_token_from_auth_api()

    AUTHENTICATION_RESPONSE['response'] = response.json()
