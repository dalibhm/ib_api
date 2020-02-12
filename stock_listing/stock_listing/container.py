import os
from configparser import ConfigParser

from injector import Injector, singleton, inject, provider, Module

from data.repository import Repository
from logger import LogService


class Container(Module):
    def __init__(self):
        environment = os.getenv('environment') or 'development'
        # self.config = ConfigParser()
        # self.config.read(os.path.join('../settings', environment + '.ini'))
        # self.injector = Injector(self.configure, auto_bind=False)

    def configure(self, binder):
        # binder.bind(ConfigParser, to=self.config, scope=singleton)
        binder.bind(Repository, to=Repository, scope=singleton)
        # binder.bind(Logger, to=Logger, scope=singleton)

    @provider
    @singleton
    def configuration(self) -> ConfigParser:
        environment = os.getenv('environment') or 'development'
        config = ConfigParser()
        config.read(os.path.join('..', 'settings', environment + '.ini'))
        return config

    @provider
    @singleton
    def setup_logger(self, config: ConfigParser) -> LogService:
        log_level = config.get('logging', 'log_level')
        log_location = config.get('logging', 'log_location')
        return LogService(log_location=log_location, filename='stock_listing_server', log_level=log_level)
