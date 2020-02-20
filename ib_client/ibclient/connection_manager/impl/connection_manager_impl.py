from configparser import ConfigParser
import time
from threading import Thread

from ibapi.client import EClient

import logging

from injector import inject

from Services.LogService import LogService
from ib_client.ib_client import IbClient
from connection_manager.connection_manager import ConnectionManager

logger = logging.getLogger(__name__)


class IbConnection:
    def __init__(self, ib_client: IbClient):
        self.ibclient = ib_client
        self._state = Closed()
        self.logger = LogService.get_startup_log()
        self.logger.debug('Started IbConnection manager.')

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
    def open(self, connection: ConnectionManager):
        pass

    def close(self, connection: ConnectionManager):
        connection.ib_client.disconnect()
        connection.change_state(Disconnected())

class Connecting(State):
    def open(self, connection: ConnectionManager):
        pass

    def close(self, connection: ConnectionManager):
        connection.change_state(Disconnected())


# I mean by listening ; waiting for acknowledgment from IB server
class Listening(State):
    def open(self, connection: ConnectionManager):
        if connection.ibclient.isConnected():
            connection.change_state(Connected())

    def close(self):
        pass


class Disconnected(State):
    def open(self, connection: ConnectionManager):
        connection.change_state(Connecting())
        connection.connect()

    def close(self):
        pass


class ConnectionManagerImpl(ConnectionManager):
    @inject
    def __init__(self, config: ConfigParser, ib_client: IbClient):
        super().__init__()
        self._state = Disconnected()
        self.host = config.get('ib client', 'host')
        self.port = config.getint('ib client', 'port')
        self.client_id = config.getint('ib client', 'client-id')

        self.ib_client: EClient = ib_client
        self.hold_on_requests = False
        self.connection_closed = True

        # this is EClient that read the responses from the API
        # It needs to be running, so that the ACK is received, but it shuts down when connection is lost
        self.loop_active = False
        self.loop_thread = None
        # self.loop_thread = Thread(target=self.ib_client.run)
        # self.loop_thread.start()
        self.logger = LogService.get_startup_log()
        self.logger.debug('Started connection manager.')
        self.ib_client.wrapper.attach(self)

    def change_state(self, state):
        self._state = state


    #def connect(self):
    #    self._state.connect(self)

    def open_connection(self):
        while not isinstance(self._state, Connected):
            print('trying to connect on {}:{}, state = {}'.format(self.host, self.port, self._state))
            self._state.open(self)
        print('Connected')
        self.eclient_run()

    def close(self):
        self._state.close(self)

    def connect(self):
        self.logger.debug('ConnectionManager connecting to Gateway')
        self.logger.debug('ConnectionManager blocked all requests')

        try:
            self.ib_client.connect(self.host, self.port, self.client_id)
            if isinstance(self._state, Connecting):
                self._state = Connected()
        except Exception as e:
            logger.exception('error while reconnecting to IB API ')
            self.logger.exception('error while reconnecting to IB API')


    def update(self):
        self.hold_on_requests = True
        self._state = Disconnected()


    def eclient_run(self):
        if self.loop_thread and self.loop_thread.is_alive():
            self.logger.debug('EClient.run already running')
            return

        if isinstance(self._state, Connected):
            self.loop_thread = Thread(target=self.ib_client.run)
            self.loop_thread.start()
            self.logger.debug('started EClient.run')
            # logger.debug('EClient.run() started')
            self.hold_on_requests = False
            self.connection_closed = False
            self.logger.debug('accepting requests')
            # self.last_connection_trial_time = datetime.now()

    def run(self):
        while True:
            if isinstance(self._state, Disconnected):
                self.open_connection()



    #def connect(self):
    #    # while (datetime.now() - self.last_connection_trial_time).total_seconds() < 5\
    #    #         or (datetime.now() - self.disconnect_time).total_seconds() < 5:
    #    # time.sleep(5)
    #    # continue
    #    self.logger.debug('ConnectionManager connecting to Gateway')
    #    self.hold_on_requests = True
    #    self.logger.debug('ConnectionManager blocked all requests')
    #    trial_number = 1

    #    if self.loop_thread and self.loop_thread.is_alive():
    #        return
    #    self.logger.debug('ConnectionManager ensuring that EClient.run loop is over')
    #    while not self.ib_client.isConnected():
    #        # if self.ib_client.done and self.ib_client.msg_queue.empty() :
    #        # this is using the internals if IB api and may change at any time
    #        # moreover I am not sure what REDIRECT means
    #        try:
    #            # self.ib_client.disconnect()
    #            logger.debug('ConnectionManager checking if connState == IbClient.CONNECTING')
    #            if not self.ib_client.connState == IbClient.CONNECTING:
    #                # this makes sure we don't try to connect when another connection is trying to be established,
    #                # the result is a double axcknowledgemnt and the API is not working
    #                self.logger.debug('ConnectionManager about to connect to {}:{} with id {}'.format(
    #                    self.host, self.port, self.client_id
    #                ))
    #                self.ib_client.connect(self.host, self.port, self.client_id)
    #                time.sleep(1)
    #                self.logger.debug('reconnecting to IB API {} trial(s)'.format(trial_number))
    #                logger.info('reconnecting to IB API {} trial(s)'.format(trial_number))
    #                if self.ib_client.isConnected():
    #                    self.logger.debug('still connecting')
    #                    self.connection_closed = False
    #                self.logger.debug('connection established')
    #        except Exception as e:
    #            logger.exception('error while reconnecting to IB API {} trial(s)'.format(trial_number))
    #            self.logger.exception('error while reconnecting to IB API {} trial(s)'.format(trial_number))

    #        trial_number += 1
    #    # logger.debug('EClient.run() starting')
    #    self.loop_thread = Thread(target=self.ib_client.run)
    #    self.loop_thread.start()
    #    self.logger.debug('started EClient.run')
    #    # logger.debug('EClient.run() started')
    #    self.hold_on_requests = False
    #    self.logger.debug('accepting requests')
    #    # self.last_connection_trial_time = datetime.now()

    def is_connected(self):
        return not self.connection_closed

    # def run(self) -> None:
    #     while True:
    #         if self.connection_closed:
    #             print("[connection to api down]")
    #             self.connect()
