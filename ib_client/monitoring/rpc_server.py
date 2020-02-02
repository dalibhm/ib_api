import pickle


class RPCHandler:
    def __init__(self):
        self.functions = {}

    def register_function(self, func):
        self.functions[func.__name__] = func

    def handle_connection(self, connection):
        try:
            while True:
                # receive message
                func_name, args, kargs = pickle.loads(connection.recv())
                # run RPC and send a response
                try:
                    r = self.functions[func_name](*args, **kargs)
                    connection.send(pickle.dumps(r))
                except Exception as e:
                    connection.send(pickle.dumps(e))
        except EOFError:
            pass


from multiprocessing.connection import Listener
from threading import Thread


def rpc_server(handler: RPCHandler, address, authkey):
    sock = Listener(address, authkey=authkey)
    while True:
        client = sock.accept()
        t = Thread(target=handler.handle_connection, args=(client,))
        t.daemon = True
        t.start()




