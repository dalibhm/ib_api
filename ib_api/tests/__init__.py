import datetime
import logging

from init_app import SetupLogger
from ib_app import TestApp


def init_application():
    SetupLogger()
    logger = logging.getLogger()
    logger.debug("now is %s", datetime.datetime.now())
    logger.setLevel(logging.ERROR)

    app = TestApp()

    # ! [connect]
    app.connect("127.0.0.1", 4001, clientId=0)
    return app
