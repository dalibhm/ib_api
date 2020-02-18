import os
import sys

import logbook


class LogService:
    def __init__(self, log_location, filename, log_level):
        self.log_level = log_level
        self.log_file = os.path.join(log_location, filename)
        self.log_level = LogService.__get_logbook_logging_level(log_level)

        if not self.log_file:
            logbook.StreamHandler(sys.stdout, level=self.log_level).push_application()
        else:
            logbook.TimedRotatingFileHandler(
                self.log_file, level=self.log_level,
                date_format="%y%m%d").push_application()

        msg = 'Logging initialized, level: {}, mode: {}'.format(
            log_level,
            "stdout mode" if not self.log_file else 'file mode: ' + self.log_file
        )

        LogService.get_startup_log().notice(msg)

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
