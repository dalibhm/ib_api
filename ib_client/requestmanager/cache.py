import threading
from collections import defaultdict
from datetime import datetime

from requestmanager.request.request import Request


class Cache:
    def __init__(self):
        self.requests = defaultdict(dict)
        self.lock = threading.Lock()

    def register_request(self, request_id: int, request: Request) -> None:
        self.lock.acquire()
        self.requests[request_id]['request'] = request
        self.requests[request_id]['created'] = datetime.now()
        self.lock.release()
        
    def register_run(self, request_id):
        self.lock.acquire()
        self.requests[request_id]['run'] = datetime.now()
        self.lock.release()
        
    def register_success(self, request_id):
        self.lock.acquire()
        self.requests[request_id]['finished'] = datetime.now()
        self.lock.release()

    def register_error(self, request_id):
        self.lock.acquire()
        self.requests[request_id]['error'] = datetime.now()
        self.lock.release()

    def get_request_by_id(self, request_id: int) -> Request:
        self.lock.acquire()
        request: Request = self.requests[request_id]['request']
        self.lock.release()
        return request
    
    def is_active(self, request_id: int) -> bool:
        self.lock.acquire()
        status = bool('run' in self.requests[request_id].keys())
        self.lock.release()
        return status
