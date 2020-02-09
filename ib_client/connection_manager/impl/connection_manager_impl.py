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


class IbConnection:
    def __init__(self, ib_client: IbClient):
        self.ibclient = ib_client
        self._state = Closed()

    def connect(self):
        raise NotImplementedError

    def change_state(self, state):
        self._state = state

    def open(self):
        self._state.open(self)

    def close(self):
        self._state.close(self)


class State:
    pass


class Connected(State):
    def open(self, connection: IbConnection):
        pass

    def close(self, connection: IbConnection):
        connection.ibclient.DISCONNECTED


# I mean by listening ; waiting for acknowledgment from IB server
class Listening(State):
    def open(self, connection: IbConnection):
        if connection.ibclient.isConnected():
            connection.change_state(Connected())

    def close(self):
        pass


class Closed(State):
    def open(self, connection: IbConnection):
        connection.connect()
        connection.change_state(Listening())

    def close(self):
        pass


class ConnectionManagerImpl(ConnectionManager):
    @inject
    def __init__(self, config: ConfigParser, ib_client: IbClient):
        super().__init__()
        self._state = Closed()
        self.host = config.get('ib client', 'host')
        self.port = config.getint('ib client', 'port')
        self.client_id = config.getint('ib client', 'client-id')

        self.ib_client: EClient = ib_client
        self.hold_on_requests = False
        # self.last_connection_trial_time = datetime.now()
        # self.disconnect_time = None
        self.connection_closed = True
        # this is EClient that read the responses from the API
        # It needs to be running, so that the ACK is received, but it shuts down when connection is lost
        self.loop_active = False
        self.loop_thread = None
        # self.loop_thread = Thread(target=self.ib_client.run)
        # self.loop_thread.start()

    def connect(self):
        # while (datetime.now() - self.last_connection_trial_time).total_seconds() < 5\
        #         or (datetime.now() - self.disconnect_time).total_seconds() < 5:
        # time.sleep(5)
        # continue
        self.hold_on_requests = True
        trial_number = 1

        if self.loop_thread and self.loop_thread.is_alive():
            return

        while not self.ib_client.isConnected():
            # if self.ib_client.done and self.ib_client.msg_queue.empty() :
            # this is using the internals if IB api and may change at any time
            # moreover I am not sure what REDIRECT means
            try:
                # self.ib_client.disconnect()
                if not self.ib_client.connState == IbClient.CONNECTING:
                    # this makes sure we don't try to connect when another connection is trying to be established,
                    # the result is a double axcknowledgemnt and the API is not working
                    self.ib_client.connect(self.host, self.port, self.client_id)
                    time.sleep(1)
                    logger.info('reconnecting to IB API {} trial(s)'.format(trial_number))
                    if self.ib_client.isConnected():
                        self.connection_closed = False
            except Exception as e:
                logger.exception('error while reconnecting to IB API {} trial(s)'.format(trial_number))

            trial_number += 1
        # logger.debug('EClient.run() starting')
        self.loop_thread = Thread(target=self.ib_client.run)
        self.loop_thread.start()
        # logger.debug('EClient.run() started')
        self.hold_on_requests = False
        # self.last_connection_trial_time = datetime.now()

    def is_connected(self):
        return not self.connection_closed

    def run(self) -> None:
        while True:
            if self.connection_closed:
                print("[connection to api down]")
                self.connect()
