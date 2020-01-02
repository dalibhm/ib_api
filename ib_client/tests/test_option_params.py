import datetime
import logging
import os
import sys
import time
from unittest.mock import Mock, MagicMock

import pytest

from api.impl.ib_client_impl import IbClientImpl
from connection_manager.connection_manager import ConnectionManager
from enums.request_type import RequestType
from requestmanager.request.security_definition_option import SecDefOptParamsRequest
from responsemanager.response_manager import ResponseManager
from tests import read_stocks, historical_request, fundamental_request

module_dir = os.path.dirname(__file__)
sys.path.append(os.path.join(module_dir, '..'))

from requestmanager.requestmanager import RequestManager


@pytest.fixture()
def option_param_request():
    response_manager = ResponseManager(historical_data_processor=Mock(),
                                       fundamental_data_processor=Mock(),
                                       contract_details_processor=Mock(),
                                       option_params_processor=Mock())
    op = SecDefOptParamsRequest(request_id=123,
                                request=Mock(),
                                ib_client=Mock(),
                                response_manager=response_manager)

    return op


def test_option_params_process_data(option_param_request: SecDefOptParamsRequest):
    option_param_request.process_data('exchange', 123456, 'trading class', 100, {'213', '234'}, {1, 2, 4})
    a = 1


