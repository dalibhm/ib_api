from datetime import datetime

from ibapi.contract import Contract
import threading
import logbook

from api.ib_client import IbClient
from connection_manager.connection_manager import ConnectionManager
from enums.request_type import RequestType
from requestmanager.actor import Actor


class Request(Actor):
    def __init__(self, request_id, request, ib_client: IbClient, request_type: RequestType,
                 connection_manager: ConnectionManager):
        """

        :type ib_client: object
        """
        super().__init__()
        self._request = request  # this GRPC raw requests
        self._connection_manager =connection_manager
        self.request_type = request_type
        self.request_time = datetime.now()
        self.response_time = None
        self.request_id = request_id
        self.contract = self.get_contract()
        self._ib_client = ib_client
        self.name = ''
        # self._data = None
        self.lock = threading.Lock()
        self.symbol = request.contract.symbol
        self.logger = logbook.Logger("App")
        self._finished = False

    def __repr__(self):
        return 'request {} {}'.format(self.request_type, self.contract)
    # @property
    # def data(self):
    #     return self._data

    @property
    def proto_request(self):
        return self._request

    # def set_response_time(self, response_time):
    #     self.response_time = response_time

    def run(self):
        while self._connection_manager.hold_on_requests:
            continue


    def get_contract(self):
        proto_contract = self._request.contract
        contract = Contract()
        contract.conId = proto_contract.conId
        contract.symbol = proto_contract.symbol
        contract.secType = proto_contract.secType
        contract.exchange = proto_contract.exchange
        contract.primaryExchange = proto_contract.primaryExchange
        contract.currency = proto_contract.currency
        return contract

    def process_data(self, data):
        raise NotImplementedError

    def process_data_end(self, *args):
        raise NotImplementedError

    def process_error(self, error_code, error_string):
        raise NotImplementedError

# implement in inherited classes
#     def __repr__(self):
#         return '{} started {} ended {}'.format(self.response_time, self.response_time)
