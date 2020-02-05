import threading

from api.ib_client import IbClient
from ibapi.common import BarData

from connection_manager.connection_manager import ConnectionManager
from responsemanager.response_manager import ResponseManager
from proto.request_data_pb2 import HistoricalDataRequest
from requestmanager.request.request import Request
from enums.request_type import RequestType


class HistoricalRequest(Request):

    def __init__(self,
                 request_id: int,
                 request: HistoricalDataRequest,
                 ib_client: IbClient,
                 response_manager: ResponseManager,
                 connection_manager: ConnectionManager):

        super().__init__(request_id, request, ib_client, RequestType.Historical, connection_manager)
        self.lock = threading.Lock()
        self.response_manager = response_manager

    def run(self):
        super().run()
        request = self._request
        request_id = self.request_id
        contract = self.contract
        self.logger.notice("sending request {} for historical data : {}".format(request_id, contract))
        try:
            # self.kafka_request_manager.push_historical_request(request_id, request)
            self._ib_client.reqHistoricalData(request_id,
                                              contract,
                                              request.endDateTime,
                                              request.durationString,
                                              request.barSizeSetting,
                                              request.whatToShow,
                                              int(request.useRTH),
                                              request.formatDate,
                                              int(request.keepUpToDate),
                                              []
                                              )
        except Exception as e:
            self.finished = True
            self.logger.exception('Unable to request {} historical data for {}'.format(request_id,
                                                                                       contract)
                                  )
            self.close()
        while not self.finished:
            continue

    def process_data(self, bar_data: BarData):
        self.response_manager.process_historical_data(self.request_id, self._request, bar_data)

    def process_data_end(self, *args):
        try:
            start = args[0]
            end = args[1]
            self.finished = True
            self.close()
            self.response_manager.process_historical_data_end(self.request_id, self._request, start, end)
        finally:
            self.close()

    def process_error(self, error_code, error_string):
        try:
            self.finished = True
            self.close()
            self.response_manager.process_historical_data_error(self.request_id, self._request, error_code, error_string)
        finally:
            self.close()

    # def add_data(self, data):
    #     self._data.append(data)
    #
    # # implement in inherited classes
    # def __repr__(self):
    #     return 'symbol {} started {} ended {}'.format(self.symbol, self.response_time, self.response_time)
