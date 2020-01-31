import os
from configparser import ConfigParser

from injector import Injector, singleton, Module, provider

from download_manager.download_manager import DownloadManager
from download_runner.download_runner import DownloadRunner
from download_runner.impl.contract_details_runner import ContractDetailsRunner
from input_manager.impl.listing_service_input import ListingServiceInput
from input_manager.input_manager import InputManager
from input_manager.impl.static_list import StaticList
from scope import Scope
from request_scheduler import RequestScheduler
from services.ib_client import IbClient
from services.listing_service import ListingService


class ContractDetailsModule(Module):
    def configure(self, binder):
        binder.bind(DownloadRunner, to=ContractDetailsRunner, scope=singleton)

