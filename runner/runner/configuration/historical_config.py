from injector import singleton, Module

from download_runner.download_runner import DownloadRunner
from download_runner.historical_params import HistoricalParams
from download_runner.impl.historical_runner import HistoricalRunner


class HistoricalModule(Module):
    def __init__(self, historical_params):
        super().__init__()
        self.historical_params = historical_params
        
    def configure(self, binder):   
        binder.bind(HistoricalParams, to=self.historical_params, scope=singleton)
        binder.bind(DownloadRunner, to=HistoricalRunner, scope=singleton)

