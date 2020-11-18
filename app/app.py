import os
import urllib

from flask import Flask

app = Flask(__name__)

CLIENT_ID = os.getenv('CLIENT_ID')


@app.route('/authenticate', methods=['GET'])
def authenticate():
    url_parameters = urllib.parse.urlencode({
        'response_type': 'code',
        'response_mode': 'form_post',
        'client_id': CLIENT_ID,
        'scope': 'accounts transactions',
        'redirect_uri': 'https://console.truelayer.com/redirect-page',
        'providers': 'uk-ob-all uk-oauth-all uk-cs-mock'
    })

    authentication_link = f'https://auth.truelayer-sandbox.com/?{url_parameters}'

    return f'<a href="{authentication_link}">Authenticate</a>'
