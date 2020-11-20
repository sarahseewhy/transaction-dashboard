import os
import urllib

import requests
from flask import Flask, url_for, request, render_template
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
    if has_authentication_code():
        return redirect(url_for('display_transactions'))


@app.route('/display_transactions', methods=['GET'])
def display_transactions():

    access_token = AUTHENTICATION_RESPONSE['response']['access_token']

    request_header = {'Authorization': f'Bearer {access_token}'}

    response = requests.get('https://api.truelayer-sandbox.com/data/v1/accounts', headers=request_header)

    accounts = response.json()['results']

    transactions = {}

    for account in accounts:
        account_id = account['account_id']
        if account['account_type'] == 'TRANSACTION':
            transactions = retrieve_transactions(account_id)

    return render_template('transactions.html', transactions=transactions)


def retrieve_transactions(account_id):
    access_token = AUTHENTICATION_RESPONSE['response']['access_token']

    request_header = {'Authorization': f'Bearer {access_token}'}

    response = requests.get(f'https://api.truelayer-sandbox.com/data/v1/accounts/{account_id}/transactions', headers=request_header)

    transactions = response.json()['results']

    return transactions


def has_authentication_code():
    global AUTHENTICATION_RESPONSE

    authentication_code = request.form['code']

    body = {
        'client_id': CLIENT_ID,
        'client_secret': SECRET_ID,
        'code': authentication_code,
        'grant_type': 'authorization_code',
        'redirect_uri': REDIRECT_URI,
    }

    try:
        response = requests.post(f'{TRUELAYER_AUTH_URI}/connect/token', data=body)
        AUTHENTICATION_RESPONSE['response'] = response.json()
        return True
    except urllib.error.HTTPError as exception:
        print(exception)
