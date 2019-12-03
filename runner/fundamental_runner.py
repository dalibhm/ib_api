import logging
import time
from threading import Thread

logger = logging.getLogger(__name__)


class FundamentalRunner(Thread):
    def __init__(self, ib_client, msg_queue):
        super().__init__()
        self.ib_client = ib_client
        self.msg_queue = msg_queue

    def run(self) -> None:
        try:
            logger.debug('starting fundamental runner loop')
            while self.msg_queue:
                contract = self.msg_queue.get()
                for report_type in ["ReportsFinSummary",
                                    "ReportsOwnership",
                                    "ReportSnapshot",
                                    "ReportsFinStatements",
                                    "RESC",
                                    "CalendarReport"]:
                    self.ib_client.request_fundamental_data(contract, report_type)
                    time.sleep(0.5)
            self.msg_queue.task_done()
        except:
            logger.exception('unhandled exception in FundamentalRunner')
