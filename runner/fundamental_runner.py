import logging
from queue import Queue

import time
from threading import Thread

logger = logging.getLogger(__name__)


class FundamentalRunner(Thread):
    def __init__(self, ib_client, msg_queue):
        super().__init__()
        self.ib_client = ib_client
        self.msg_queue: Queue = msg_queue

    def run(self) -> None:
        try:
            logger.debug('starting fundamental runner loop')
            while self.msg_queue:
                if self.msg_queue.empty():
                    continue
                contract = self.msg_queue.get()
                for report_type in ["ReportsFinSummary",
                                    "ReportsOwnership",
                                    "ReportSnapshot",
                                    "ReportsFinStatements",
                                    "RESC",
                                    "CalendarReport"]:
                    contract['exchange'] = 'SMART'
                    contract['secType'] = 'STK'
                    logger.info('{} {} sending request'.format(contract, report_type))
                    try:
                        self.ib_client.request_fundamental_data(contract, report_type)
                        logger.info('{} {} request sent'.format(contract, report_type))
                        time.sleep(0.5)
                    except:
                        logger.exception('{} {} request NOT SENT'.format(contract, report_type) )
            self.msg_queue.task_done()
        except:
            logger.exception('unhandled exception in FundamentalRunner')
