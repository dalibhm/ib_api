import datetime
import logging
import os
import time
from configparser import ConfigParser


from ib_client import IbClient


def init_ib_client(config: ConfigParser, request_manager):
    SetupLogger()
    logger = logging.getLogger()
    logger.debug("now is %s", datetime.datetime.now())
    logger.setLevel(logging.ERROR)

    ib_client = IbClient(config, request_manager)
    ib_client.globalCancelOnly = config.getboolean('ib client', 'global-cancel')

    # ! [connect]
    host = config['ib client']['host']
    port = config['ib client'].getint('port')
    ib_client.connect(host, port, clientId=0)
    return ib_client


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
