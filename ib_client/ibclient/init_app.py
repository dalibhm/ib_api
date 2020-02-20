import logging
import os
import time


def SetupLogger():
    log_path = os.path.join("..", "log")
    if not os.path.exists(log_path):
        os.makedirs(log_path)

    recfmt = '(%(threadName)s) %(asctime)s.%(msecs)03d %(levelname)s %(filename)s:%(lineno)d %(message)s'

    timefmt = '%y%m%d_%H:%M:%S'

    # logging.basicConfig( level=logging.DEBUG,
    #                    format=recfmt, datefmt=timefmt)
    logging.basicConfig(filename=time.strftime(os.path.join("../log", "ibapi_%Y%m%d_%H_%M_%S.log")),
                        filemode="w",
                        level=logging.DEBUG,
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
