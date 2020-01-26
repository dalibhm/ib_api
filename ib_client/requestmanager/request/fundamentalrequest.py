import logging
import threading

from api.ib_client import IbClient
from enums.request_type import RequestType
from proto.request_data_pb2 import FundamentalDataRequest
from requestmanager.request.request import Request
from responsemanager.response_manager import ResponseManager

logger = logging.getLogger(__name__)


class FundamentalRequest(Request):

    def __init__(self,
                 request_id: int,
                 request: FundamentalDataRequest,
                 ib_client: IbClient,
                 response_manager: ResponseManager):

        super().__init__(request_id, request, ib_client, RequestType.Fundamental)
        self.response_manager = response_manager

    def run(self):
        request = self._request
        request_id = self.request_id
        contract = self.get_contract()
        self.logger.notice("{} for fundamental data : {} - sending request".format(request_id, contract))

        self._ib_client.reqFundamentalData(request_id,
                                           contract,
                                           request.reportType,
                                           []
                                           )
        self.logger.notice("{} for fundamental data : {} - request sent".format(request_id, contract))

    def process_data(self, xml_data):
        self.response_manager.process_fundamental_data(self.request_id, self._request, xml_data)

    def process_data_end(self):
        self.finished = True

    def process_error(self, error_code, error_string):
        self.finished = True
        self.response_manager.process_fundamental_data_error(self.request_id, self._request, error_code, error_string)
