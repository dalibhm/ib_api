import threading

from grpc_service.kafka_producer import KafkaRequestManager
from ibapi.common import BarData
from requestmanager.request.request import Request
from enums.request_type import RequestType


class HistoricalRequest(Request):

    def __init__(self, request_id, request, response_processor):
        super().__init__(request_id, request)
        self.lock = threading.Lock()
        self.name = "HistoricalRequest"
        self.request_type = RequestType.Historical
        self.response_processor = response_processor

    def run(self):
        request = self._request
        request_id = self.request_id
        contract = self.get_contract(request)
        self.logger.notice("sending request {} for historical data : {}".format(request_id, contract))
        try:
            # self.kafka_request_manager.push_historical_request(request_id, request)
            self.ib_client.reqHistoricalData(request_id,
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
            self.logger.exception('Unable to request {} historical data for {}'.format(request_id,
                                                                                       contract)
                                  )

    def process_data(self, bar_data: BarData):
        self.response_processor.process_historical_data(self.request_id, self.request, bar_data)

    def process_data_end(self, start, end):
        self.response_processor.process_historical_data_end(self.request_id, self.request, start, end)

    def process_error(self, error_code, error_string):
        self.response_processor.process_historicall_data_error(self.request_id, error_code, error_string)


    # def add_data(self, data):
    #     self._data.append(data)
    #
    # # implement in inherited classes
    # def __repr__(self):
    #     return 'symbol {} started {} ended {}'.format(self.symbol, self.response_time, self.response_time)
