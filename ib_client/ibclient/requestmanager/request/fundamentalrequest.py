import asyncio
import logging

from api.ib_client import IbClient
from connection_manager.connection_manager import ConnectionManager
from enums.request_type import RequestType
from proto.request_data_pb2 import FundamentalDataRequest
from requestmanager.request.request import Request
from responsemanager import ResponseManager

logger = logging.getLogger(__name__)


class FundamentalRequest(Request):

    def __init__(self,
                 request_id: int,
                 request: FundamentalDataRequest,
                 ib_client: IbClient,
                 response_manager: ResponseManager,
                 connection_manager: ConnectionManager,
                 context=None):

        super().__init__(request_id, request, ib_client, RequestType.Fundamental, connection_manager)
        self.response_manager = response_manager

    async def run(self):
        super().run()
        request = self._request
        request_id = self.request_id
        contract = self.contract
        self.logger.notice("{} for fundamental data : {} - sending request".format(request_id, contract))

        self._ib_client.reqFundamentalData(request_id,
                                           contract,
                                           request.reportType,
                                           []
                                           )
        self.logger.notice("{} for fundamental data : {} - request sent".format(request_id, contract))

        await asyncio.sleep(0.5)

    def process_data(self, xml_data):
        self.response_manager.process_fundamental_data(self.request_id, self._request, xml_data)

    def process_data_end(self):
        self.finished = True

    def process_error(self, error_code, error_string):
        self.finished = True
        self.response_manager.process_fundamental_data_error(self.request_id, self._request, error_code, error_string)
