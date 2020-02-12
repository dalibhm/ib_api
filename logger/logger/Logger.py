import sys

import logbook


class Logger:
    def __init__(self, filename, log_level):
        self.filename = filename
        self.log_level = Logger.__get_logbook_logging_level(log_level)

        if not filename:
            logbook.StreamHandler(sys.stdout, level=self.log_level).push_application()
        else:
            logbook.TimedRotatingFileHandler(
                filename, level=self.log_level,
                date_format="%y%m%d_%H").push_application()

        msg = 'Logging initialized, level: {}, mode: {}'.format(
            log_level,
            "stdout mode" if not filename else 'file mode: ' + filename
        )

        Logger.get_startup_log().notice(msg)

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
