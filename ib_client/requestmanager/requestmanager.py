import threading
from datetime import datetime
from collections import defaultdict
from queue import Queue

from injector import inject

from Services.request_id_generator import RequestIdGenerator
from connection_manager.connection_manager import ConnectionManager
from api.ib_client import IbClient
from requestmanager.cache import Cache
from requestmanager.request.contractdetailsrequest import ContractDetailsRequest
from requestmanager.request.fundamentalrequest import FundamentalRequest
from requestmanager.request.security_definition_option import SecDefOptParamsRequest
from requestmanager.request_scheduler import RequestScheduler
from requestmanager.status import Status
from responsemanager.response_manager import ResponseManager
from requestmanager.request.historicalrequest import HistoricalRequest
from enums.request_type import RequestType




request_constructor_map = {
    RequestType.Historical: HistoricalRequest,
    RequestType.Fundamental: FundamentalRequest,
    RequestType.ContractDetails: ContractDetailsRequest,
    RequestType.SecDefOptParams: SecDefOptParamsRequest
}


class RequestManager:

    @inject
    def __init__(self,
                 request_id_gen: RequestIdGenerator,
                 connection_manager: ConnectionManager,
                 response_manager: ResponseManager,
                 # requests_limit: RequestsLimit,
                 ib_client: IbClient):

        self.request_id_gen = request_id_gen
        self._connection_manager = connection_manager

        self.status = Status()
        self.cache = Cache()
        
        self._ib_client = ib_client
        self._response_manager = response_manager

        self.request_queue = Queue()
        self._request_scheduler = RequestScheduler(cache=self.cache, status=self.status,
                                                   connection_manager=connection_manager,
                                                   request_queue=self.request_queue)
        self._request_scheduler.start()

    # separate registering and running a request here
    def add_request(self, request, request_type: RequestType) -> None:
        # generate request id
        request_id = self.request_id_gen.get_id()

        _request = request_constructor_map[request_type](request_id=request_id,
                                                         request=request,
                                                         ib_client=self._ib_client,
                                                         response_manager=self._response_manager)

        # add request to local dictionary
        self.cache.register_request(request_id, _request)

        while self._connection_manager.hold_on_requests:
            continue

        self.request_queue.put(_request)
        self.status.update_on_added(request_type)


    def on_request_end(self, reqId, request_type, error=False):
        if not error:
            self.cache.register_success(reqId)
            self.status.update_on_success(request_type)
        else:
            self.cache.register_error(reqId)
            self.status.update_on_error(request_type)

    # response management is delegated to the request object
    # as the request knows which ResponseManager method to call
    # to process its response

    def process_data(self, reqId: int, *data) -> None:
        request = self.cache.get_request_by_id(reqId)
        request.process_data(*data)

    def process_data_end(self, reqId, *args):
        request = self.cache.get_request_by_id(reqId)
        self.on_request_end(reqId, request.request_type)
        request.process_data_end(*args)

    def process_error(self, reqId, error_code, error_string):
        request = self.cache.get_request_by_id(reqId)
        self.on_request_end(reqId, request.request_type, error=True)
        request.process_error(error_code, error_string)
