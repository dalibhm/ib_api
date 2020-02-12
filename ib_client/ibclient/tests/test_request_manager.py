import os
import sys
from unittest.mock import Mock, MagicMock

import pytest

from ibclient.api.impl.ib_client_impl import IbClientImpl
from ibclient.connection_manager.connection_manager import ConnectionManager
from ibclient.enums.request_type import RequestType
from ibclient.tests import read_stocks, historical_request, fundamental_request

module_dir = os.path.dirname(__file__)
sys.path.append(os.path.join(module_dir, '..'))

from ibclient.requestmanager.requestmanager import RequestManager


@pytest.fixture()
def request_manager():
    test_conn_manager = Mock(ConnectionManager)
    test_conn_manager.hold_on_requests = False

    mock_ib_client = Mock(IbClientImpl)

    rm = RequestManager(request_id_gen=Mock(),
                        connection_manager=test_conn_manager,
                        response_manager=Mock(),
                        ib_client=mock_ib_client)

    # mock_ib_client.reqHistoricalData = Mock(side_effect=rm.process_data)

    return rm


@pytest.fixture()
def sample_historical_request():
    contracts = read_stocks()
    request = historical_request(contracts[0])
    return request


@pytest.fixture()
def sample_fundamental_request():
    contracts = read_stocks()
    request = fundamental_request(contracts[0])
    return request


def test_request_manager_add_request(request_manager):
    request_manager.cache.register_request(123, 'test.request')
    request = request_manager.cache.get_request_by_id(123)
    assert 'test.request' == request
    #assert request['created']


def test_register_historical_request_started(request_manager):
    request_manager.cache.register_request(123, 'historical request')
    request_manager.status.update_on_added(RequestType.Historical)

    request = request_manager.cache.get_request_by_id(123)
    status = request_manager.status

    assert 'historical request' == request
    # assert request['created']
    # # assert not request['finished']
    assert 1 == status.status[RequestType.Historical]['outstanding']
    assert 0 == status.status[RequestType.Historical]['processed']


def test_register_historical_request_succeeded(request_manager):
    request_manager.cache.register_request(123, 'historical request')
    request_manager.status.update_on_added(RequestType.Historical)

    request = request_manager.cache.get_request_by_id(123)
    status = request_manager.status

    request_manager.on_request_end(123, RequestType.Historical)

    assert 'historical request' == request
    # assert request['created']
    # assert request['finished']
    assert 0 == status.status[RequestType.Historical]['outstanding']
    assert 1 == status.status[RequestType.Historical]['processed']
    assert 0 == status.status[RequestType.Historical]['error']


def test_register_historical_request_error(request_manager):
    request_manager.cache.register_request(123, 'historical request')
    request_manager.status.update_on_added(RequestType.Historical)

    request = request_manager.cache.get_request_by_id(123)
    status = request_manager.status

    request_manager.on_request_end(123, RequestType.Historical, error=True)

    assert 'historical request' == request
    # assert request['created']
    # assert request['error']
    assert 0 == status.status[RequestType.Historical]['outstanding']
    assert 0 == status.status[RequestType.Historical]['processed']
    assert 1 == status.status[RequestType.Historical]['error']


def test_add_historical_request(request_manager):
    contracts = read_stocks()
    request = historical_request(contracts[0])

    request_manager.add_request(request, RequestType.Historical)


def test_request_manager_add_historical_request(request_manager, sample_historical_request):
    request_manager.add_request(sample_historical_request, RequestType.Historical)

    request_manager._ib_client.reqHistoricalData.assert_called_with(123, 'data')


def test_request_manager_add_fundamental_request(request_manager, sample_fundamental_request):
    request_manager.add_request(sample_fundamental_request, RequestType.Fundamental)

    request_manager._ib_client.reqFundamentalData.assert_called_with(123, 'data')


def test_request_manager_add_historical_response(request_manager: RequestManager, sample_historical_request):
    request_manager.add_request(sample_historical_request, RequestType.Historical)

    for request_id in request_manager._cache.requests.keys():
        historical_request = request_manager._cache.get_request_by_id(request_id)
        historical_request.process_data = MagicMock()
        request_manager.process_data(request_id, 'data')
        historical_request.process_data.assert_called_with('data')
