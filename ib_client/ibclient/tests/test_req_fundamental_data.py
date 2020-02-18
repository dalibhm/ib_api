import datetime
import logging
import os
import sys
import time

import pytest
from ibapi.contract import Contract

module_dir = os.path.dirname(__file__)
sys.path.append(os.path.join(module_dir, '../ib_client/'))

from ibclient.init_app import SetupLogger

from ibclient.ib_client import ib_client


@pytest.fixture(scope="module")
def app():
    SetupLogger()
    logger = logging.getLogger()
    logger.debug("now is %s", datetime.datetime.now())
    logger.setLevel(logging.ERROR)

    import configparser
    config = configparser.ConfigParser()
    config.read_dict({'data api': {'url': ''}})

    app = ib_client.TestApp(config['data api'])

    # ! [connect]
    app.connect("127.0.0.1", 4001, clientId=0)
    yield app
    time.sleep(5)
    app.disconnect()


@pytest.mark.skip
def test_req_fundamental_data(app):
    contract = Contract()
    contract.symbol = "IBKR"
    contract.secType = "STK"
    contract.currency = "USD"
    contract.exchange = "ISLAND"
    print('*********************************')
    print('started test_req_fundamental_data')
    print('*********************************')

    time.sleep(1)

    app.reqFundamentalData(1000, contract, 'ReportsFinSummary', [])
    time.sleep(5)
