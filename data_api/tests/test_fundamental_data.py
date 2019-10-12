import json
import os
import sys

import pytest
from flask import Response
from pytest import skip

from app import create_app


# container_folder = os.path.abspath(os.path.join(
#     os.path.dirname(__file__), '..'
# ))
# sys.path.insert(0, container_folder)


@pytest.fixture
def client():
    app = create_app('testing')
    app_context = app.app_context()
    app_context.push()

    client = app.test_client()

    yield client


@pytest.fixture
def financial_report_xml():
    file = os.path.join('.', 'tests', 'financial_data', 'financial_reports', 'A.ReportsFinStatements_0.xml')
    with open(file, 'r') as file_reader:
        xml = file_reader.read()

    yield xml


# @pytest.mark.skip()
def test_getting_financial_report(client):
    # response = client.get('/')
    response: Response = client.get('/api/fundamental_data/financial_reports')

    assert response.status_code == 200


def test_post_financial_report(client, financial_report_xml):
    response: Response = client.post('/api/fundamental_data/financial_reports',
                                     data=json.dumps(dict(symbol='A',
                                                          xml=financial_report_xml,
                                                          report_date='18990101')),
                                     content_type='application/json')

    assert response.status_code == 201


@pytest.mark.skip()
def test_post_all_financial_reports(client):
    directory = os.path.join('.', 'financial_data', 'financial_reports')
    files = os.listdir(directory)
    for file in files:
        full_path = os.path.join(directory, file)
        with open(full_path, 'r') as file_reader:
            xml = file_reader.read()
            symbol = file.split('.')[0]
        response: Response = client.post('/api/fundamental_data/financial_reports',
                                         data=json.dumps(dict(symbol=symbol,
                                                              xml=xml,
                                                              report_date='18990101')),
                                         content_type='application/json')

        assert response.status_code == 201
