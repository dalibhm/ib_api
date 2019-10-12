import threading


class RequestIdGenerator:
    def __init__(self):
        self.last_request_id = 10
        self.counter_lock = threading.Lock()

    def get_id(self):
        with self.counter_lock:
            self.last_request_id += 1
        return self.last_request_id
