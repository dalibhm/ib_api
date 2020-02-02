from injector import inject

from monitoring.rpc_server import RPCHandler, rpc_server
from requestmanager.cache import Cache
from requestmanager.request_scheduler import RequestScheduler
from threading import Thread, Lock
import copy


class MonitoringTool:
    @inject
    def __init__(self, cache: Cache, request_scheduler: RequestScheduler):
        self._cache = cache
        self._request_scheduler = request_scheduler

        # register with handler
        handler = RPCHandler()
        handler.register_function(self.get_cache)

        # run server
        t = Thread(target=rpc_server, args=(handler, ('localhost', 17000),), kwargs={'authkey': b'peekaboo'})
        t.start()

    def get_cache(self):
        result = self._cache.Requests
        return result
