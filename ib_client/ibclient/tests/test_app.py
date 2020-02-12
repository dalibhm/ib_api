import datetime
import logging
import os
import sys
import time

import pytest

module_dir = os.path.dirname(__file__)
sys.path.append(os.path.join(module_dir, '../ib_client/'))

from ibclient.init_app import SetupLogger

from ibclient.api import ib_client


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
def test_app(app):
    pass