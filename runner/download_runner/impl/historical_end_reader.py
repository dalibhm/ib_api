import logging
import time
from threading import Thread

from download_runner.impl.kafka_consumer import KafkaConsumer

logger = logging.getLogger(__name__)


class HistoricalEndReader(Thread):
    def __init__(self, hist_data_end_queue, request_scheduler, config):
        """

        :rtype: object
        """
        super().__init__()
        self.hist_data_end_queue = hist_data_end_queue
        self.request_scheduler = request_scheduler
        self.consumer = KafkaConsumer(group_id='hist.data.end.group',
                                      topic=config.get('kafka', 'historical-data-end-topic'),
                                      default_topic_config={"auto.offset.reset": "latest"},
                                      config=config)

    def run(self) -> None:
        try:
            logger.debug('starting historical data end reader loop')
            while True:
                time.sleep(1)
                try:
                    hist_data_end = self.consumer.poll()
                    logger.info('got historical data end {}'.format(hist_data_end))
                    self.request_scheduler.on_historical_data_end()
                except:
                    logger.exception('exception polling hist_data_end topic')
        except:
            logger.exception('unhandled exception in HistoricalEndReader')


