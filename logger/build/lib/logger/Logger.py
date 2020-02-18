import os
import sys

import logging
import time


class LogService:
    def __init__(self, log_location, filename, log_level):
        self.log_file = os.path.join(log_location, filename)
        self.log_level = LogService.__get_logbook_logging_level(log_level)

        if not os.path.exists("../log"):
            os.makedirs("../log")

        self.recfmt = '[%(threadName)s][%(asctime)s.%(msecs)03d][%(levelname)s] %(filename)s:%(lineno)d %(message)s'

        self.timefmt = '%y%m%d_%H:%M:%S'

        self.file = time.strftime(self.log_file + "_%Y%m%d_%H_%M_%S.log")
        # logging.basicConfig( level=logging.DEBUG,
        #                    format=recfmt, datefmt=timefmt)
        # logging.basicConfig(filename=time.strftime(self.log_file + "_%Y%m%d_%H_%M_%S.log"),
        #                     filemode="w",
        #                     level=self.log_level,
        #                     format=recfmt, datefmt=timefmt)

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

        msg = 'Logging initialized, level: {}, mode: {}'.format(
            log_level,
            "stdout mode" if not self.log_file else 'file mode: ' + self.log_file
        )
        self.Logger(__name__).info(msg)

    def Logger(self, logger_name):
        logger = logging.getLogger(logger_name)
        logger.setLevel(self.log_level)
        formatter = logging.Formatter(fmt=self.recfmt, datefmt=self.timefmt)
        file_handler = logging.FileHandler(self.file)
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)
        return logger


    @staticmethod
    def __get_logbook_logging_level(level_str):
        # logbook levels:
        # CRITICAL = 15
        # ERROR = 14
        # WARNING = 13
        # NOTICE = 12
        # INFO = 11
        # DEBUG = 10
        # TRACE = 9
        # NOTSET = 0

        level_str = level_str.upper().strip()

        if level_str == 'CRITICAL':
            return logging.CRITICAL
        elif level_str == 'ERROR':
            return logging.ERROR
        elif level_str == 'WARNING':
            return logging.WARNING
        elif level_str == 'INFO':
            return logging.INFO
        elif level_str == 'DEBUG':
            return logging.DEBUG
        elif level_str == 'NOTSET':
            return logging.NOTSET
        else:
            raise ValueError("Unknown logbook log level: {}".format(level_str))
