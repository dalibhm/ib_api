from ddtrace import patch

patch(futures=True)

from concurrent import futures
from queue import Queue
from threading import Thread

from injector import inject

from enums.request_type import RequestType
from requestmanager.cache import Cache
from requestmanager.request.request import Request

requests_limit_map = {
    RequestType.Historical: 1,
    RequestType.Fundamental: 1,
    RequestType.ContractDetails: 10,
    RequestType.SecDefOptParams: 10
}


def task(request: Request):
    print(request.request_id, 'started')
    request.run()
    while not request.finished:
        print(request.request_id, 'is finised = ', request.finished)
        continue
    print(request.request_id, 'is finised = ', request.finished)


class RequestScheduler(Thread):
    @inject
    def __init__(self,
                 cache: Cache,
                 # status: Status,
                 # connection_manager: ConnectionManager,
                 request_queue: Queue):
        super().__init__()
        self.cache = cache
        # self.status = status
        # self._connection_manager = connection_manager
        self.request_queue = request_queue
        self.executors = {request_type: futures.ThreadPoolExecutor(max_workers=requests_limit_map[request_type])
                          for request_type in RequestType}

    def run(self):
        threads = []
        while 1:
            if not self.request_queue.empty():
                try:
                    request = self.request_queue.get()
                    self.executors[request.request_type].submit(request._bootsrap)
                    self.cache.register_run(request.request_id)
                    self.request_queue.task_done()
                except Exception as e:
                    print(e)
