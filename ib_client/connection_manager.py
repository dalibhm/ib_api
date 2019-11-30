from configparser import ConfigParser
from datetime import datetime, time
from threading import Thread

from ibapi.client import EClient

import logging

logger = logging.getLogger(__name__)

class ConnectionManager:
    def __init__(self, config: ConfigParser, ib_client):
        self.host = config.get('ib client', 'host')
        self.port = config.getint('ib client', 'port')
        self.ib_client: EClient = ib_client
        # self.last_connection_trial_time = datetime.now()
        # self.disconnect_time = None

    def connect(self):
        # while (datetime.now() - self.last_connection_trial_time).total_seconds() < 5\
        #         or (datetime.now() - self.disconnect_time).total_seconds() < 5:
        # time.sleep(5)
        # continue
        while not self.ib_client.isConnected():
            self.ib_client.connect(self.host, self.port, 0)
            logger.error('reconnecting to IB API')
        app_thread = Thread(target=self.ib_client.run)
        app_thread.start()
        logger.error('EClient.run() started')
        # self.last_connection_trial_time = datetime.now()

    def reconnect(self):
        self.ib_client.disconnect()
        # self.ib_client.done = True
        # self.disconnect_time = datetime.now()
        self.connect()
