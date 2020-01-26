from concurrent import futures
from queue import Queue
from threading import Thread

from connection_manager.connection_manager import ConnectionManager
from enums.request_type import RequestType
from requestmanager.cache import Cache
from requestmanager.request.request import Request
from requestmanager.status import Status

requests_limit_map = {
    RequestType.Historical: 10,
    RequestType.Fundamental: 10,
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
    def __init__(self,
                 cache: Cache,
                 status: Status,
                 connection_manager: ConnectionManager,
                 request_queue: Queue):
        super().__init__()
        self.cache = cache
        self.status = status
        self._connection_manager = connection_manager
        self.request_queue = request_queue
        self.executors = {request_type: futures.ThreadPoolExecutor(max_workers=requests_limit_map[request_type])
                          for request_type in RequestType}

    def run(self):
        threads = []
        while 1:
            if not self.request_queue.empty():
                request = self.request_queue.get()
                self.executors[request.request_type].submit(request._bootsrap())
                self.cache.register_run(request.request_id)
                self.request_queue.task_done()
