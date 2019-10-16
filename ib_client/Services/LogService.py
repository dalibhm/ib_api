import os
import time

import logbook
import sys


class LogService:
    @staticmethod
    def global_init(log_level_text, filename):
        # transforms the log level in the ini file from string to an enum for Logbook
        level = LogService.__get_logbook_logging_level(log_level_text)

        if not filename:
            logbook.StreamHandler(sys.stdout, level=level).push_application()
        else:
            logbook.TimedRotatingFileHandler(
                filename, level=level,
                date_format="%Y-%m-%d").push_application()

        msg = 'Logging initialized, level: {}, mode: {}'.format(
            log_level_text,
            "stdout mode" if not filename else 'file mode: ' + filename
        )

        LogService.get_startup_log().notice(msg)

    # @staticmethod
    # def init_ib_client_log():
    #     if not os.path.exists("log"):
    #         os.makedirs("log")
    #
    #     time.strftime("pyibapi.%Y%m%d_%H%M%S.log")
    #     recfmt = '(%(threadName)s) %(asctime)s.%(msecs)03d %(levelname)s %(filename)s:%(lineno)d %(message)s'
    #     timefmt = '%y%m%d_%H:%M:%S'
    #
    #     logger = logging.getLogger('ib_logger')
    #     logger.setLevel(logging.INFO)
    #     formatter = logging.Formatter(fmt=recfmt, datefmt=timefmt)
    #     file_handler = logging.FileHandler(time.strftime("log/pyibapi.%Y%m%d_%H:%M:%S.log"))
    #     file_handler.setFormatter(formatter)
    #     logger.addHandler(file_handler)
    #
    #     # logger = logging.getLogger()
    #     # console = logging.StreamHandler()
    #     # console.setLevel(logging.ERROR)
    #     # logger.addHandler(console)

    @staticmethod
    def get_startup_log():
        return logbook.Logger("App")

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
            return logbook.CRITICAL
        elif level_str == 'ERROR':
            return logbook.ERROR
        elif level_str == 'WARNING':
            return logbook.WARNING
        elif level_str == 'NOTICE':
            return logbook.NOTICE
        elif level_str == 'INFO':
            return logbook.INFO
        elif level_str == 'DEBUG':
            return logbook.DEBUG
        elif level_str == 'TRACE':
            return logbook.TRACE
        elif level_str == 'NOTSET':
            return logbook.NOTSET
        else:
            raise ValueError("Unknown logbook log level: {}".format(level_str))
