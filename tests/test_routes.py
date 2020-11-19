import urllib

import pytest

import config


@pytest.mark.usefixtures("test_client")
def test_authenticate(test_client):
    client_id = config.CONFIG['CLIENT_ID']
    redirect_uri = config.CONFIG['REDIRECT_URI']

    url_parameters = urllib.parse.urlencode({
        'response_type': 'code',
        'response_mode': 'form_post',
        'client_id': client_id,
        'scope': 'accounts transactions',
        'redirect_uri': redirect_uri,
        'providers': 'uk-cs-mock'
    })

    authentication_link = f'https://auth.truelayer-sandbox.com/?{url_parameters}'

    with test_client:
        response = test_client.get('/authenticate')
        assert response.status_code == 302
        assert response.location == authentication_link
