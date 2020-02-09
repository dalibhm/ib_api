import os
from configparser import ConfigParser

from injector import Module, singleton, provider

from download_manager.download_manager import DownloadManager
from download_runner.download_runner import DownloadRunner
from download_runner.impl.historical_runner import HistoricalRunner
from input_manager.impl.listing_service_input import ListingServiceInput
from input_manager.input_manager import InputManager
from request_scheduler import RequestScheduler
from scope import Scope
from historical_data import HistoricalDataService
from services.ib_client import IbClient
from services.listing_service import ListingService


class RunnerModule(Module):
    def __init__(self, scope):
        super().__init__()
        self.scope = scope

    def configure(self, binder):
        binder.bind(Scope, to=self.scope, scope=singleton)
        binder.bind(IbClient, to=IbClient, scope=singleton)
        binder.bind(ListingService, to=ListingService, scope=singleton)
        # binder.bind(HistoricalDataService, to=HistoricalDataService, scope=singleton)
        binder.bind(InputManager, to=ListingServiceInput, scope=singleton)
        binder.bind(RequestScheduler, to=RequestScheduler, scope=singleton)
        binder.bind(DownloadManager, to=DownloadManager, scope=singleton)

    @provider
    @singleton
    def configuration(self) -> ConfigParser:
        environment = os.getenv('environment') or 'development'
        config = ConfigParser()
        config.read(os.path.join('settings', environment + '.ini'))
        return config

    @provider
    @singleton
    def historical_data(self, config: ConfigParser) -> HistoricalDataService:
        url = config.get('services', 'historical_data')
        historical_data_service = HistoricalDataService(server_url=url)
        return historical_data_service
