from configparser import ConfigParser

import ib_client


class ConnectionManager:
    def __init__(self, config: ConfigParser, ib_client: ib_client.IbClient):
        self.host = config.get('ib client', 'host')
        self.port = config.getint('ib client', 'port')
        self.ib_client = ib_client

    def connect(self):
        self.ib_client.connect(self.host, self.port, 0)

    def reconnect(self):
        self.ib_client.disconnect()
        self.connect()