import os

from flask import Flask

app = Flask(__name__)

CLIENT_ID = os.getenv('CLIENT_ID')


@app.route('/authenticate', methods=['GET'])
def authenticate():
    authentication_link = f'https://auth.truelayer-sandbox.com/?' \
        f'response_type=code&' \
        f'client_id={CLIENT_ID}' \
        f'scope=info%20accounts%20balance%20cards%20transactions%20direct_debits%20standing_orders%20offline_access' \
        f'&redirect_uri=https://console.truelayer.com/redirect-page' \
        f'&providers=uk-ob-all%20uk-oauth-all'

    return f'<a href="{authentication_link}">Authenticate</a>'
