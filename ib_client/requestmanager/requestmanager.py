import threading

from proto.request_data_pb2 import HistoricalDataRequest


class RequestManager:
    def __init__(self):
        self.requests = {}
        self.active_historical_requests_counter = 0
        self.lock = threading.Lock()

    def register_request(self, request_id, request):
        self.lock.acquire()
        self.requests[request_id] = request
        self.active_historical_requests_counter += 1
        self.lock.release()

    def get_request_by_id(self, request_id):
        self.lock.acquire()
        request = self.requests[request_id]
        self.lock.release()

        return request

    def requests_number(self):
        self.lock.acquire()
        n = self.active_historical_requests_counter
        self.lock.release()
        return n

    def decrement_counter(self):
        self.lock.acquire()
        self.active_historical_requests_counter -= 1
        self.lock.release()
