import logging
import threading

from api.ib_client import IbClient
from enums.request_type import RequestType
from proto.request_data_pb2 import ContractRequest
from requestmanager.request.request import Request
from responsemanager.response_manager import ResponseManager

logger = logging.getLogger(__name__)


class ContractDetailsRequest(Request):

    def __init__(self,
                 request_id: int,
                 request: ContractRequest,
                 ib_client: IbClient,
                 response_manager: ResponseManager):
        super().__init__(request_id, request, ib_client, RequestType.ContractDetails)
        self.response_manager = response_manager

    def run(self):
        request_id = self.request_id
        contract = self.get_contract()
        self.logger.notice("{} for contract details {} : sending request".format(request_id, contract))

        # self.kafka_request_manager.push_historical_request(request_id, request)
        self._ib_client.reqContractDetails(request_id, contract)
        self.logger.notice("{} for contract details {} : request sent".format(request_id, contract)
                         )
        while True:
            # waits for a stop signal
            msg = self.recv()

    def process_data(self, contract_details):
        self.response_manager.process_contract_details(self.request_id, self._request, contract_details)

    def process_data_end(self):
        self.close()
        self.response_manager.process_contract_details_end(self.request_id, self._request)

    def process_error(self, error_code, error_string):
        self.close()
        self.response_manager.process_contract_details_error(self.request_id, self._request, error_code, error_string)
