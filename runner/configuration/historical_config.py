from injector import singleton, Module

from download_manager.download_manager import DownloadManager
from download_runner.download_runner import DownloadRunner
from download_runner.historical_params import HistoricalParams
from download_runner.impl.historical_runner import HistoricalRunner
from input_manager.impl.listing_service_input import ListingServiceInput
from input_manager.input_manager import InputManager
from scope import Scope
from request_scheduler import RequestScheduler


class HistoricalModule(Module):
    def __init__(self, historical_params):
        super().__init__()
        self.historical_params = historical_params
        
    def configure(self, binder):   
        binder.bind(HistoricalParams, to=self.historical_params, scope=singleton)
        binder.bind(DownloadRunner, to=HistoricalRunner, scope=singleton)

