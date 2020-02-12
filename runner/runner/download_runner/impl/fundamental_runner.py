import logging
from queue import Queue

import time

from injector import inject

from services.contract_details_service import ContractsService
from services.ib_client import IbClient

logger = logging.getLogger(__name__)


class FundamentalRunner:
    @inject
    def __init__(self, ib_client: IbClient, contracts_service: ContractsService):
        self.ib_client = ib_client
        self._contracts_service = contracts_service

    def run(self, contract) -> None:
        c = self._contracts_service.get_contract(contract['conId'])
        if c is not None and c.primaryExchange == 'NYSE':
            for report_type in ["ReportsFinSummary",
                                "ReportsOwnership",
                                "ReportSnapshot",
                                "ReportsFinStatements",
                                "RESC",
                                "CalendarReport"]:
                contract['exchange'] = 'SMART'
                # contract['secType'] = 'STK'

                try:
                    logger.info('{} {} sending request'.format(contract, report_type))
                    self.ib_client.request_fundamental_data(contract, report_type)
                    logger.info('{} {} request sent'.format(contract, report_type))
                    time.sleep(0.5)
                except:
                    logger.exception('{} {} request NOT SENT'.format(contract, report_type))
