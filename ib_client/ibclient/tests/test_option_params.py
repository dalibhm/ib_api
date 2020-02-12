import os
import sys
from unittest.mock import Mock

import pytest

from ibclient.requestmanager.request.security_definition_option import SecDefOptParamsRequest
from ibclient.responsemanager import ResponseManager

module_dir = os.path.dirname(__file__)
sys.path.append(os.path.join(module_dir, '..'))


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


