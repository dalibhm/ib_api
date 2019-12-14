import logging
from queue import Queue

import time

logger = logging.getLogger(__name__)


class FundamentalRunner:
    def __init__(self, ib_client):
        self.ib_client = ib_client

    def run(self, contract) -> None:
        for report_type in ["ReportsFinSummary",
                            "ReportsOwnership",
                            "ReportSnapshot",
                            "ReportsFinStatements",
                            "RESC",
                            "CalendarReport"]:
            # contract['exchange'] = 'SMART'
            # contract['secType'] = 'STK'

            try:
                logger.info('{} {} sending request'.format(contract, report_type))
                self.ib_client.request_fundamental_data(contract, report_type)
                logger.info('{} {} request sent'.format(contract, report_type))
                time.sleep(0.5)
            except:
                logger.exception('{} {} request NOT SENT'.format(contract, report_type))
