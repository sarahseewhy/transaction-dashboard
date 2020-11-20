import urllib

import pytest

import config


@pytest.mark.usefixtures("test_client")
def test_authenticate_route_redirects_to_authentication_uri(test_client):
    client_id = config.CONFIG['CLIENT_ID']
    redirect_url = config.CONFIG['REDIRECT_URL']

    url_parameters = urllib.parse.urlencode({
        'response_type': 'code',
        'response_mode': 'form_post',
        'client_id': client_id,
        'scope': 'accounts transactions',
        'redirect_uri': redirect_url,
        'providers': 'uk-cs-mock'
    })

    authentication_link = f'https://auth.truelayer-sandbox.com/?{url_parameters}'

    with test_client:
        response = test_client.get('/authenticate')
        assert response.status_code == 302
        assert response.location == authentication_link


@pytest.mark.skip(reason="Method also calls the TrueLayer API and I can't figure out how to mock it.")
@pytest.mark.usefixtures("test_client")
def test_authenticate_handler_redirects_to_transaction_route(test_client):
    display_transactions_route = 'http://localhost:5000/display_transactions'

    with test_client:
        response = test_client.post('/authenticate/callback')
        assert response.status_code == 302
        assert response.location == display_transactions_route
