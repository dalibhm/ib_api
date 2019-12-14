import threading
from datetime import datetime
from collections import defaultdict

from proto.request_data_pb2 import HistoricalDataRequest


class RequestManager:
    def __init__(self):
        self.status = {
            'historical': {'outstanding': 0, 'processed': 0, 'error': 0},
            'fundamental': {'outstanding': 0, 'processed': 0, 'error': 0}
        }
        self.requests = defaultdict(dict)
        self.lock = threading.Lock()

    def add_request(self, request_id, request):
        self.lock.acquire()
        self.requests[request_id]['request'] = request
        self.requests[request_id]['created'] = datetime.now()
        self.lock.release()

    def on_request_succes(self, request_id):
        self.lock.acquire()
        self.requests[request_id]['finished'] = datetime.now()
        self.lock.release()

    def on_request_error(self, request_id):
        self.lock.acquire()
        self.requests[request_id]['error'] = datetime.now()
        self.lock.release()

    def update_status_on_request_added(self, request_type):
        self.lock.acquire()
        self.status[request_type]['outstanding'] += 1
        self.lock.release()

    def update_status_on_request_success(self, request_type):
        self.lock.acquire()
        self.status[request_type]['processed'] += 1
        self.status[request_type]['outstanding'] -= 1
        self.lock.release()

    def update_status_on_request_error(self, request_type):
        self.lock.acquire()
        self.status[request_type]['error'] += 1
        self.status[request_type]['outstanding'] -= 1
        self.lock.release()

    def register_historical_request(self, request_id, request):
        self.add_request(request_id, request)
        self.update_status_on_request_added('historical')

    def register_fundamental_request(self, request_id, request):
        self.add_request(request_id, request)
        self.update_status_on_request_added('fundamental', 'outstanding')

    def get_request_by_id(self, request_id):
        self.lock.acquire()
        request = self.requests[request_id]
        self.lock.release()

        return request

    def number_historical_requests_outstanding(self):
        # ask status for this
        self.lock.acquire()
        n = self.status['historical']['outstanding']
        self.lock.release()
        return n

    def on_request_end(self, reqId, request_type, error=False):
        if not error:
            self.on_request_succes(reqId)
            self.update_status_on_request_success(request_type)
        else:
            self.on_request_error(reqId)
            self.update_status_on_request_error(request_type)

    # def fundamentaDataEnd(self, reqId):
    #     self.lock.acquire()
    #     self.status['historical']['processed'] += 1
    #     self.status['historical']['outstanding'] -= 1
    #     self.lock.release()
    #
    # def historicalDataError(self, reqId):
    #     self.lock.acquire()
    #     self.status['historical']['error'] += 1
    #     self.lock.release()
