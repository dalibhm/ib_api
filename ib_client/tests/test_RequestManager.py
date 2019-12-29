import datetime
import logging
import os
import sys
import time

import pytest

module_dir = os.path.dirname(__file__)
sys.path.append(os.path.join(module_dir, '..'))

from requestmanager.requestmanager import RequestManager

@pytest.mark.skip
def test_request_manager_add_request():
    rm = RequestManager()
    rm.add_request(123, 'test.request')
    request = rm.get_request_by_id(123)
    assert 'test.request' == request['request']
    assert request['created']

@pytest.mark.skip
def test_register_historical_request_started():
    rm = RequestManager()
    rm.register_historical_request(123, 'historical request')
    request = rm.get_request_by_id(123)
    status = rm.status
    assert 'historical request' == request['request']
    assert request['created']
    # assert not request['finished']
    assert 1 == status['historical']['outstanding']
    assert 0 == status['historical']['processed']

@pytest.mark.skip
def test_register_historical_request_succeeded():
    rm = RequestManager()
    rm.register_historical_request(123, 'historical request')
    request = rm.get_request_by_id(123)
    status = rm.status
    rm.on_request_end(123, 'historical')
    assert 'historical request' == request['request']
    assert request['created']
    assert request['finished']
    assert 0 == status['historical']['outstanding']
    assert 1 == status['historical']['processed']
    assert 0 == status['historical']['error']

@pytest.mark.skip
def test_register_historical_request_error():
    rm = RequestManager()
    rm.register_historical_request(123, 'historical request')
    request = rm.get_request_by_id(123)
    status = rm.status
    rm.on_request_end(123, 'historical', error=True)
    assert 'historical request' == request['request']
    assert request['created']
    assert request['error']
    assert 0 == status['historical']['outstanding']
    assert 0 == status['historical']['processed']
    assert 1 == status['historical']['error']