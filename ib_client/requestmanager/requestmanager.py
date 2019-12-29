import threading
from datetime import datetime
from collections import defaultdict

from injector import inject

from Services.request_id_generator import RequestIdGenerator
from connection_manager.connection_manager import ConnectionManager
from api.ib_client import IbClient
from requestmanager.request.historicalrequest import HistoricalRequest
from enums.request_type import RequestType


class RequestsLimit(object):
    historical = 10
    fundamental = 10
    contracts = 10


class RequestManager:
    @inject
    def __init__(self,
                 request_id_gen: RequestIdGenerator,
                 connection_manager: ConnectionManager,
                 requests_limit: RequestsLimit,
                 ib_client: IbClient):

        self.request_id_gen = request_id_gen
        self._connection_manager = connection_manager
        self.requests_limit = requests_limit

        self.status = defaultdict(dict)
        for request_type in RequestType:
            self.status[request_type] = {'outstanding': 0, 'processed': 0, 'error': 0}

        self.requests = defaultdict(dict)
        self.lock = threading.Lock()
        self._ib_client = ib_client

    def add_historical_data_request(self, request):
        # generate request id
        request_id = self.request_id_gen.get_id()

        # create the appropriate request object
        # the object is responsible for sending the request
        # and processing the response

        historical_request = HistoricalRequest(request_id, request, self._ib_client)

        # add request to local dictionary
        self.add_request(request)

        # check there are not too many outstanding requests
        while self.number_historical_requests_outstanding() > self.requests_limit.historical:
            continue

        # wait until there is a connection
        while self.connection_manager.hold_on_requests:
            continue

        # send the request when the connection is available
        historical_request.run()

    def add_request(self, request):
        request_id = request.request_id
        self.lock.acquire()
        self.requests[request_id]['request'] = request
        self.requests[request_id]['created'] = datetime.now()
        self.lock.release()

    def log_success(self, request_id):
        self.lock.acquire()
        self.requests[request_id]['finished'] = datetime.now()
        self.lock.release()

    def log_error(self, request_id):
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
            self.log_success(reqId)
            self.update_status_on_request_success(request_type)
        else:
            self.log_error(reqId)
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
    def process_data(self, reqId, *args):
        request = self.get_request_by_id(reqId)['request']
        request.process_data(args)

    def process_data_end(self, reqId, *args):
        request = self.get_request_by_id(reqId)['request']
        self.on_request_end(reqId, request.request_type)
        request.process_data_end(args)

    def process_error(self, reqId, error_code, error_string):
        request = self.get_request_by_id(reqId)['request']
        self.log_error(reqId, request.request_type)
        request.process_error(error_code, error_string)
