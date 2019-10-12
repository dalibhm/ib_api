import datetime
import logging
import os
import time

from ibapi import utils
from ibapi.tag_value import TagValue

from ib_app import TestApp


def init_application(args):
    SetupLogger()
    logger = logging.getLogger()
    logger.debug("now is %s", datetime.datetime.now())
    logger.setLevel(logging.ERROR)

    print("Using args", args)
    logger.debug("Using args %s", args)
    # print(args)

    app = TestApp()
    if args.global_cancel:
        app.globalCancelOnly = True
    # ! [connect]
    app.connect(args.host, args.port, clientId=0)
    return app


def SetupLogger():
    if not os.path.exists("log"):
        os.makedirs("log")

    time.strftime("pyibapi.%Y%m%d_%H%M%S.log")

    recfmt = '(%(threadName)s) %(asctime)s.%(msecs)03d %(levelname)s %(filename)s:%(lineno)d %(message)s'

    timefmt = '%y%m%d_%H:%M:%S'

    # logging.basicConfig( level=logging.DEBUG,
    #                    format=recfmt, datefmt=timefmt)
    logging.basicConfig(filename=time.strftime("log/pyibapi.%Y%m%d_%H_%M_%S.log"),
                        filemode="w",
                        level=logging.INFO,
                        format=recfmt, datefmt=timefmt)
    # logger = logging.getLogger(__name__)
    # logger.setLevel(logging.INFO)
    # formatter = logging.Formatter(fmt=recfmt, datefmt=timefmt)
    # file_handler = logging.FileHandler(time.strftime("log/pyibapi.%Y%m%d_%H:%M:%S.log"))
    # file_handler.setFormatter(formatter)
    # logger.addHandler(file_handler)

    # logger = logging.getLogger()
    # console = logging.StreamHandler()
    # console.setLevel(logging.ERROR)
    # logger.addHandler(console)
