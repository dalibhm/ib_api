import logging
from threading import Thread, Lock

logger = logging.getLogger(__name__)


class HistoricalEndReader(Thread):
    def __init__(self, hist_data_end_queue, request_scheduler):
        """

        :rtype: object
        """
        super().__init__()
        self.hist_data_end_queue = hist_data_end_queue
        self.request_scheduler = request_scheduler

    def run(self) -> None:
        try:
            logger.debug('starting historical data end reader loop')
            while self.hist_data_end_queue:
                try:
                    hist_data_end = self.hist_data_end_queue.get()
                    logger.info('got historical data end {}'.format(hist_data_end))
                    self.report_scheduler.request_ended()
                except:
                    logger.info('exception trying to access hist_data_end_queue')
        except:
            logger.exception('unhandled exception in HistoricalEndReader')


class RequestScheduler:
    def __init__(self):
        self.max_simultaneous_requests = 20
        self.active_requests = 0
        self.lock = Lock()

    def request_added(self):
        self.lock.acquire()
        self.active_requests += 1
        self.lock.release()

    def request_ended(self):
        self.lock.acquire()
        self.active_requests -= 1
        self.lock.release()

    def send(self):
        return self.active_requests <= self.max_simultaneous_requests
