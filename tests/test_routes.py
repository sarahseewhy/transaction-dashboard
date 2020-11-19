import pytest

import config


@pytest.mark.usefixtures("test_client")
def test_authenticate(test_client):
    client_id = config.CONFIG['CLIENT_ID']
    redirect_uri = config.CONFIG['REDIRECT_URI']

    auth_link = f'https://auth.truelayer-sandbox.com/?response_type=code&client_id={client_id}&scope=accounts%20transactionsredirect_uri={redirect_uri}&providers=uk-cs-mock'

    with test_client:
        response = test_client.get('/authenticate')
        assert response.status_code == 302
        assert response.location == auth_link
