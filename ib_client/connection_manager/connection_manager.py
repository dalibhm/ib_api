from threading import Thread


class ConnectionManager(Thread):
    def __init__(self):
        super().__init__()
        self.hold_on_requests = False
    
    def connect(self):
        pass

    def is_connected(self):
        pass

    def run(self) -> None:
        pass
