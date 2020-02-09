import os
from configparser import ConfigParser

from injector import Injector, singleton

from data.repository import Repository


class Container:
    def __init__(self):
        environment = os.getenv('ENVIRONMENT') or 'development'
        self.config = ConfigParser()
        self.config.read(os.path.join('settings', environment + '.ini'))
        self.injector = Injector(self.configure, auto_bind=False)

    def configure(self, binder):
        binder.bind(ConfigParser, to=self.config, scope=singleton)
        binder.bind(Repository, to=Repository, scope=singleton)