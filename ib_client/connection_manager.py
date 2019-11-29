from configparser import ConfigParser
from datetime import datetime, time

import ib_client


class ConnectionManager:
    def __init__(self, config: ConfigParser, ib_client: ib_client.IbClient):
        self.host = config.get('ib client', 'host')
        self.port = config.getint('ib client', 'port')
        self.ib_client = ib_client
        self.last_connection_trial_time = datetime.now()
        # self.disconnect_time = None

    def connect(self):
        # while (datetime.now() - self.last_connection_trial_time).total_seconds() < 5\
        #         or (datetime.now() - self.disconnect_time).total_seconds() < 5:
        time.sleep(5)
        # continue
        self.ib_client.connect(self.host, self.port, 0)
        self.last_connection_trial_time = datetime.now()

    def reconnect(self):
        self.ib_client.disconnect()
        self.ib_client.done = True
        # self.disconnect_time = datetime.now()
        self.connect()
