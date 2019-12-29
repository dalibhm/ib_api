from threading import Thread


class ConnectionManager(Thread):
    def __init__(self):
        super().__init__()

    def connect(self):
        pass

    def reconnect(self):
        pass

    def run(self) -> None:
        pass
