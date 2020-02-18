import asyncio
import threading

from ib_client.ib_client import IbClient
from ibapi.common import BarData

from connection_manager.connection_manager import ConnectionManager
from responsemanager import ResponseManager
from proto.request_data_pb2 import HistoricalDataRequest
from requestmanager.request.request import Request
from enums.request_type import RequestType

from ddtrace import tracer


class HistoricalRequest(Request):

    def __init__(self,
                 request_id: int,
                 request: HistoricalDataRequest,
                 ib_client: IbClient,
                 response_manager: ResponseManager,
                 connection_manager: ConnectionManager,
                 context):

        super().__init__(request_id, request, ib_client, RequestType.Historical, connection_manager)
        self.lock = threading.Lock()
        self.response_manager = response_manager
        self.coro = self.run()
        self.context = context
        self.finished_queue = asyncio.Queue

    @property
    def finished(self):
        self.lock.acquire()
        res = self._finished
        self.lock.release()
        return res

    @finished.setter
    def finished(self, value):
        self.lock.acquire()
        self._finished = value
        self.lock.release()

    # @coroutine
    # @tracer.wrap(name='send request', service='historical req')
    @tracer.wrap()
    async def run(self):
        # tracer.context_provider.activate(self.context)
        # with tracer.trace('child of context: start run'):
        #     time.sleep(1)
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
            self.stop_notification.wait()
            return True
        except:
            self.logger.exception("{} for fundamental data : {} - request sent".format(request_id, contract))
            return False

    # @tracer.wrap(name='process data', service='historical req')
    @tracer.wrap()
    def process_data(self, bar_data: BarData):
        tracer.context_provider.activate(self.context)
        with tracer.trace('child of context: data') as span:
            span.set_tag('reqId', self.request_id)
            self.response_manager.process_historical_data(self.request_id, self._request, bar_data)


    # @tracer.wrap(name='process data end', service='historical req')
    @tracer.wrap()
    def process_data_end(self, *args):
        self.update()
        tracer.context_provider.activate(self.context)
        with tracer.trace('child of context: data end') as span:
            # if span:
            span.set_tag('reqId', self.request_id)
            try:
                start = args[0]
                end = args[1]
                self.response_manager.process_historical_data_end(self.request_id, self._request, start, end)
            finally:
                self.finished = True
                self.close()

    @tracer.wrap(name='process data error', service='historical req')
    def process_error(self, error_code, error_string):
        self.update()
        tracer.context_provider.activate(self.context)
        with tracer.trace('child of context: data error') as span:
            span.set_tag('reqId', self.request_id)
            try:
                self.response_manager.process_historical_data_error(self.request_id, self._request, error_code,
                                                                    error_string)
            finally:
                self.finished = True
                self.close()


    # def add_data(self, data):
    #     self._data.append(data)
    #
    # # implement in inherited classes
    # def __repr__(self):
    #     return 'symbol {} started {} ended {}'.format(self.symbol, self.response_time, self.response_time)
