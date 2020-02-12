from injector import singleton, Module

from download_runner.download_runner import DownloadRunner
from download_runner.impl.contract_details_runner import ContractDetailsRunner


class ContractDetailsModule(Module):
    def configure(self, binder):
        binder.bind(DownloadRunner, to=ContractDetailsRunner, scope=singleton)

