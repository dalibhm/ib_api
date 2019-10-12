from flask import Response

from tests.test_client import *



def test_getting_contracts(client):
    # response = client.get('/')
    response: Response = client.get('/api/contracts')

    assert response.status_code == 200
