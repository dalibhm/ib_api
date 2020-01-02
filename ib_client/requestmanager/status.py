import threading
from collections import defaultdict

from enums.request_type import RequestType


class Status:
    def __init__(self):
        self._status = defaultdict(dict)
        for request_type in RequestType:
            self._status[request_type] = {'outstanding': 0, 'processed': 0, 'error': 0}
        self.lock = threading.Lock()

    def update_on_added(self, request_type):
        self.lock.acquire()
        self._status[request_type]['outstanding'] += 1
        self.lock.release()

    def update_on_success(self, request_type):
        self.lock.acquire()
        self._status[request_type]['processed'] += 1
        self._status[request_type]['outstanding'] -= 1
        self.lock.release()

    def update_on_error(self, request_type):
        self.lock.acquire()
        self._status[request_type]['error'] += 1
        self._status[request_type]['outstanding'] -= 1
        self.lock.release()

    def number_requests_outstanding(self, request_type: RequestType) -> int:
        # ask status for this
        self.lock.acquire()
        n = self._status[request_type]['outstanding']
        self.lock.release()
        return n

    @property
    def status(self):
        return self._status
