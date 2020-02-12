from queue import Queue
from threading import Event, Thread

from ddtrace import tracer


class ActorExit(Exception):
    pass


class Actor:
    def __init__(self):
        self._mailbox = Queue()
        self._terminated = Event()

    def send(self, msg):
        self._mailbox.put(msg)

    def recv(self):
        msg = self._mailbox.get()
        if msg is ActorExit:
            raise ActorExit()
        return msg

    # @tracer.wrap(name='request closed', service='historical req')
    def close(self):
        self.send(ActorExit)

    # @tracer.wrap(name='request started', service='historical req')
    def start(self):
        self._terminated = Event()
        t = Thread(target=self._bootstrap)
        t.daemon = True
        t.start()

    # @tracer.wrap(name='request started', service='historical req')
    def _bootsrap(self):
        try:
            self.run()
        except ActorExit:
            pass
        finally:
            self._terminated.set()

    def join(self):
        self._terminated.wait()

    def run(self):
        while True:
            msg = self.recv()
