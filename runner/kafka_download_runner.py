import time
from queue import Queue
from threading import Thread

from download_manager.download_config import DownloadConfigFactory
from download_manager.download_manager_factory import DownloadManagerFactory
from confluent_kafka import KafkaError
from confluent_kafka.avro import AvroConsumer

from request_templates.params import HistoricalRequestTemplate

MAX_COUNTER = 10000000000


class KafkaDownloadRunner:
    def __init__(self, services, config=None):
        self.services = services
        # self.consumer = AvroConsumer(config.get('runner-kafka-config'))
        kafka_config = {
            "api.version.request": True,
            "enable.auto.commit": True,
            "enable.auto.offset.store": False,
            'bootstrap.servers': config.get('kafka', 'bootstrap.servers'),
            "group.id": 'runner.group1',
            'schema.registry.url': config.get('kafka', 'schema.registry.url'),
            # the consumer was not running without default.topic.config
            "default.topic.config": {"auto.offset.reset": "smallest"}
        }
        self.consumer = AvroConsumer(kafka_config)
        topic = config.get('kafka', 'stocks-topic')
        self.consumer.subscribe([topic])

        self.last_fundamental_request_time = None
        self.q = Queue()
        self.th = Thread(target=self.send_historical_request, daemon=True)
        self.th.start()
        # tf = Thread(target=self.send_fundamental_request, daemon=True)
        # tf.start()
        self.first = True

    def go(self):
        counter = 0
        while True and counter < MAX_COUNTER:
            self.poll()
            counter += 1

        # self.pull()
        self.th.join()

    def poll(self):
        msg = self.consumer.poll(10)
        if msg is None:
            return
        elif not msg.error():
            print('Received message: {}'.format(msg.value()))
            contract = {k: v for (k, v) in msg.value().items() if
                        k in ['con_id', 'symbol', 'secType', 'exchange', 'currency']}
            contract['conId'] = contract.pop('con_id')
            self.q.put(contract)
        elif msg.error().code() == KafkaError._PARTITION_EOF:
            print('End of partition reached {0}/{1}'
                  .format(msg.topic(), msg.partition()))
        else:
            print('Error occured: {0}'.format(msg.error().str()))

    def send_historical_request(self):
        while self.q:
            contract = self.q.get()
            params = {
                "start_date": "1999-01-01",
                "end_date": "2019-10-22",
                "bar_size": "1 day",
                "price_type": "TRADES"
            }
            arranged_params = HistoricalRequestTemplate(params).params
            self.services['ib'].request_historical_data(contract, arranged_params)
            time.sleep(2)
            self.q.task_done()

    def send_fundamental_request(self):
        contract = self.q.get()
        for report_type in ["ReportsFinSummary",
                            "ReportsOwnership",
                            "ReportSnapshot",
                            "ReportsFinStatements",
                            "RESC",
                            "CalendarReport"]:
            self.services['ib'].request_fundamental_data(contract, report_type)
            time.sleep(0.5)
        self.q.task_done()
