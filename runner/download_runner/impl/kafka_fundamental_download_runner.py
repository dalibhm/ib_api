import logging

from download_runner.impl.fundamental_runner import FundamentalRunner
from download_runner.kafka_download_runner import KafkaDownloadRunner

logger = logging.getLogger(__name__)


class KafkaFundamentalDownloadRunner(KafkaDownloadRunner):
    """
    At the moment running multiple runners in the same process is not possible.
    Please run historical data separately from fundamental data for example.
    """

    def __init__(self, services, config=None):
        runner = FundamentalRunner(services['ib'])
        super().__init__(runner=runner, config=config)


