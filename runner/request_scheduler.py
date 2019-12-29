from configparser import ConfigParser
from threading import Lock

from download_runner.impl.historical_end_reader import logger


class RequestScheduler:
    def __init__(self, config: ConfigParser = None):
        self.max_simultaneous_requests = config.getint('runner', 'max-simultaneous-requests') or 1
        self.requests_number = 0
        self.responses_number = 0
        self.started = False
        self.lock = Lock()

    def request_added(self):
        self.lock.acquire()
        self.requests_number += 1
        logger.debug('request added, outstanding : {}'.format(self.requests_number - self.responses_number))
        self.lock.release()

    def on_historical_data_end(self):
        self.lock.acquire()
        self.responses_number += 1
        logger.debug('request ended, outstanding : {}'.format(self.requests_number - self.responses_number))
        self.lock.release()

    def poll_stock(self):
        self.lock.acquire()
        if self.requests_number <= self.max_simultaneous_requests:
            poll = True
        else:
            poll = self.requests_number - self.responses_number <= self.max_simultaneous_requests
        self.lock.release()
        logger.debug('poll stock ? => {}'.format(poll))
        return poll
