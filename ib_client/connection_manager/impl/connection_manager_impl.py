import threading
from configparser import ConfigParser
import time
from threading import Thread

from ibapi.client import EClient

import logging

from injector import inject

from api.ib_client import IbClient
from connection_manager.connection_manager import ConnectionManager

logger = logging.getLogger(__name__)


class ConnectionManagerImpl(ConnectionManager):
    @inject
    def __init__(self, config: ConfigParser, ib_client: IbClient):
        super().__init__()
        self.connection_closed = True
        self.host = config.get('ib client', 'host')
        self.port = config.getint('ib client', 'port')
        self.client_id = config.getint('ib client', 'client-id')
        self.ib_client: EClient = ib_client
        self.hold_on_requests = False
        # self.last_connection_trial_time = datetime.now()
        # self.disconnect_time = None

    def connect(self):
        # while (datetime.now() - self.last_connection_trial_time).total_seconds() < 5\
        #         or (datetime.now() - self.disconnect_time).total_seconds() < 5:
        # time.sleep(5)
        # continue
        self.hold_on_requests = True
        trial_number = 1
        while self.connection_closed:
            try:
                # self.ib_client.disconnect()
                self.ib_client.connect(self.host, self.port, self.client_id)
                time.sleep(5)
                logger.info('reconnecting to IB API {} trial(s)'.format(trial_number))
                if self.ib_client.isConnected():
                    self.connection_closed = False
            except Exception as e:
                logger.exception('error while reconnecting to IB API {} trial(s)'.format(trial_number))

            trial_number += 1
        logger.debug('EClient.run() starting')
        app_thread = Thread(target=self.ib_client.run)
        app_thread.start()
        logger.debug('EClient.run() started')
        self.hold_on_requests = False
        # self.last_connection_trial_time = datetime.now()

    def is_connected(self):
        return not self.connection_closed

    def run(self) -> None:
        while True:
            if self.connection_closed:
                print("[connection to api down]")
                self.connect()