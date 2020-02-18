import asyncio
import logging
from threading import Event, Thread

from ddtrace import tracer

from ib_client.ib_client import IbClient
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
        self.event = Event()

    async def schedule_termination(self):
        await asyncio.sleep(1.0)
        self.stop_notification.set()


    @tracer.wrap()
    def run(self):
        try:
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

            # loop = asyncio.new_event_loop()
            # asyncio.set_event_loop(loop)
            # t = Thread(target=loop.run_forever)
            # t.start()
            # coro = self.schedule_termination()
            # task = asyncio.create_task(coro)

            self.stop_notification.wait()
            # task.cancel()
            return True
        except:
            self.logger.exception("{} for fundamental data : {} - request sent".format(request_id, contract))
            return False
        # finally:
        #     if loop:
        #         loop.close()

    @tracer.wrap()
    def process_data(self, xml_data):
        self.update()
        self.response_manager.process_fundamental_data(self.request_id, self._request, xml_data)

    def process_data_end(self):
        self.update()

    def process_error(self, error_code, error_string):
        self.update()
        self.response_manager.process_fundamental_data_error(self.request_id, self._request, error_code, error_string)
