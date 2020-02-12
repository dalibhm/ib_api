import logging

from injector import inject

from download_runner.download_runner import DownloadRunner
from services.ib_client import IbClient

logger = logging.getLogger(__name__)


class ContractDetailsRunner(DownloadRunner):
    @inject
    def __init__(self, ib_client: IbClient):
        self.ib_client = ib_client

    def run(self, contract):
        logger.info('Contract Details request for {}'.format(contract))
        try:
            self.ib_client.request_contract_details(contract=contract)
        except Exception as e:
            logger.exception('Failed to request contract details for {}'.format(contract))
