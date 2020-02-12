from queue import Queue

from ddtrace import tracer
from injector import inject

from Services.request_id_generator import RequestIdGenerator
from connection_manager.connection_manager import ConnectionManager
from api.ib_client import IbClient
from requestmanager.cache import Cache

from requestmanager.request_scheduler import RequestScheduler
from requestmanager.status import Status
from responsemanager.response_manager import ResponseManager

from enums.request_type import RequestType


from requestmanager.request_constructor_map import request_constructor_map


class RequestManager:

    @inject
    def __init__(self,
                 request_id_gen: RequestIdGenerator,
                 connection_manager: ConnectionManager,
                 response_manager: ResponseManager,
                 # request_scheduler: RequestScheduler,
                 cache: Cache,
                 request_queue: Queue,
                 status: Status,
                 # requests_limit: RequestsLimit,
                 ib_client: IbClient):

        self.request_id_gen = request_id_gen
        self._connection_manager = connection_manager

        # self.status = Status()
        # self.cache = Cache()
        self._cache = cache
        self._request_queue = request_queue
        self._status = status
        self._ib_client = ib_client
        self._response_manager = response_manager

        # self.request_queue = Queue()
        # self._request_scheduler = RequestScheduler(cache=self.cache, status=self.status,
        #                                            connection_manager=connection_manager,
        #                                            request_queue=self.request_queue)
        # self._request_scheduler = request_scheduler
        # self._request_scheduler.start()

    # separate registering and running a request here
    # @tracer.wrap()
    # @tracer.wrap(name='add request', service='historical req')
    async def add_request(self, request, request_type: RequestType, context=None) -> None:
        # generate request id
        request_id = self.request_id_gen.get_id()

        span = tracer.current_span()
        if span:
            span.set_tag('reqId', request_id)

        _request = request_constructor_map[request_type](request_id=request_id,
                                                         request=request,
                                                         ib_client=self._ib_client,
                                                         response_manager=self._response_manager,
                                                         connection_manager=self._connection_manager,
                                                         context=context)

        # add request to local dictionary
        self._cache.register_request(request_id, _request)

        # self._request_queue.put(_request)
        self._status.update_on_added(request_type)

        status = await _request.run() # sends the request

        # status = False
        # with tracer.start_span(name='wait for response', child_of=span) as tr:
        #     # tr.set_tag('reqId', request_id)
        #     while not _request.finished:
        #         continue
        #     status = True
        #     # while True:
        #     #     try:
        #     #         _request.coro.send(None)
        #     #     except StopIteration as exc:
        #     #         status = exc.value
        #     #         break

        return status

    def on_request_end(self, reqId, request_type, error=False):
        if not error:
            self._cache.register_success(reqId)
            self._status.update_on_success(request_type)
        else:
            self._cache.register_error(reqId)
            self._status.update_on_error(request_type)

    # response management is delegated to the request object
    # as the request knows which ResponseManager method to call
    # to process its response

    def process_data(self, reqId: int, *data) -> None:
        request = self._cache.get_request_by_id(reqId)
        request.process_data(*data)

    def process_data_end(self, reqId, *args):
        request = self._cache.get_request_by_id(reqId)
        self.on_request_end(reqId, request.request_type)
        request.process_data_end(*args)

    def process_error(self, reqId, error_code, error_string):
        request = self._cache.get_request_by_id(reqId)
        self.on_request_end(reqId, request.request_type, error=True)
        request.process_error(error_code, error_string)
