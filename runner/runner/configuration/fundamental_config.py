from injector import Injector, singleton, Module
from download_runner.download_runner import DownloadRunner
from download_runner.impl.fundamental_runner import FundamentalRunner
from services.contract_details_service import ContractsService


class FundamentalModule(Module):

    def configure(self, binder):
        binder.bind(ContractsService, to=ContractsService, scope=singleton)
        binder.bind(DownloadRunner, to=FundamentalRunner, scope=singleton)
