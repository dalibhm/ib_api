import copy
import threading
from collections import defaultdict
from datetime import datetime

from requestmanager.request.request import Request


class Cache:
    def __init__(self):
        self.requests = defaultdict(dict)
        self.lock = threading.Lock()

    @property
    def Requests(self):
        self.lock.acquire()
        try:
            result = defaultdict(dict)
            for (k, v) in self.requests.items():
                for (k1, v1) in v.items():
                    if k1 == 'request':
                        result[k][k1] = str(self.requests[k][k1])
                    else:
                        result[k][k1] = self.requests[k][k1]
        finally:
            self.lock.release()
        return result

    def register_request(self, request_id: int, request: Request) -> None:
        self.lock.acquire()
        try:
            self.requests[request_id]['request'] = request
            self.requests[request_id]['created'] = datetime.now()
        finally:
            self.lock.release()

    def register_run(self, request_id):
        self.lock.acquire()
        try:
            self.requests[request_id]['run'] = datetime.now()
        finally:
            self.lock.release()

    def register_success(self, request_id):
        self.lock.acquire()
        try:
            self.requests[request_id]['finished'] = datetime.now()
        finally:
            self.lock.release()

    def register_error(self, request_id):
        self.lock.acquire()
        try:
            self.requests[request_id]['error'] = datetime.now()
        finally:
            self.lock.release()

    def get_request_by_id(self, request_id: int) -> Request:
        self.lock.acquire()
        try:
            request: Request = self.requests[request_id]['request']
        finally:
            self.lock.release()
        return request

    def is_active(self, request_id: int) -> bool:
        self.lock.acquire()
        try:
            status = bool('run' in self.requests[request_id].keys())
        finally:
            self.lock.release()
        return status
