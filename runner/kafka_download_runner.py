import time
from queue import Queue
from threading import Thread

from download_manager.download_config import DownloadConfigFactory
from download_manager.download_manager_factory import DownloadManagerFactory
from confluent_kafka import KafkaError
from confluent_kafka.avro import AvroConsumer

from request_templates.params import HistoricalRequestTemplate

MAX_COUNTER = 168624

TO_SKIP = ['AAP', 'ABM', 'ABT', 'ADC', 'ADM', 'ADX', 'AEG', 'AEM', 'AEP', 'AFL', 'AGCO', 'AIN', 'AIR', 'AIT', 'AJG', 'ALB', 'ALK', 'ALL', 'AME', 'AMX', 'AP', 'APA', 'APD', 'APH', 'ARW', 'ASA', 'ATO', 'ATR', 'AU', 'AVP', 'AVY', 'AWF', 'AXP', 'AZO', 'AZSEY', 'B', 'BA', 'BAM', 'BBVA', 'BBY', 'BC', 'BCS', 'BDX', 'BEN', 'BF A', 'BF B', 'BFS', 'BGG', 'BHP', 'BIG', 'BKH', 'BKN', 'BKT', 'BLK', 'BLL', 'BLX', 'BMO', 'BMY', 'BOH', 'BP', 'BPT', 'BRK A', 'BSX', 'BWA', 'BYD', 'CAG', 'CAH', 'CAT', 'CBL', 'CBT', 'CCK', 'CCL', 'CDNS', 'CET', 'CFR', 'CHD', 'CHE', 'CHN', 'CL', 'CLB', 'CLI', 'CLX', 'CMA', 'CMC', 'CMI', 'CMO', 'CMS', 'CNA', 'COF', 'COG', 'COO', 'CPB', 'CPK', 'CPT', 'CR', 'CRD A', 'CRD B', 'CRR', 'CRS', 'CRT', 'CSL', 'CSS', 'CTB', 'CTO', 'CTS', 'CVX', 'CW', 'CWT', 'CX', 'CYD', 'D', 'DBD', 'DCI', 'DDAIF', 'DDF', 'ECF', 'EPAC', 'FAX']

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
            "default.topic.config": {"auto.offset.reset": "earliest"}
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
            if contract['symbol'] in TO_SKIP:
                return
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
                "end_date": "2019-11-27",
                "bar_size": "1 day",
                "price_type": "TRADES"
            }
            arranged_params = HistoricalRequestTemplate(params).params
            contract['exchange'] = 'SMART'
            self.services['ib'].request_historical_data(contract, arranged_params)
            time.sleep(0.5)
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


skip = """AAP
ABM
ABT
ADC
ADM
ADX
AEG
AEM
AEP
AFL
AGCO
AIN
AIR
AIT
AJG
ALB
ALK
ALL
AME
AMX
AP
APA
APD
APH
ARW
ASA
ATO
ATR
AU
AVP
AVY
AWF
AXP
AZO
AZSEY
B
BA
BAM
BBVA
BBY
BC
BCS
BDX
BEN
BF A
BF B
BFS
BGG
BHP
BIG
BKH
BKN
BKT
BLK
BLL
BLX
BMO
BMY
BOH
BP
BPT
BRK A
BSX
BWA
BYD
CAG
CAH
CAT
CBL
CBT
CCK
CCL
CDNS
CET
CFR
CHD
CHE
CHN
CL
CLB
CLI
CLX
CMA
CMC
CMI
CMO
CMS
CNA
COF
COG
COO
CPB
CPK
CPT
CR
CRD A
CRD B
CRR
CRS
CRT
CSL
CSS
CTB
CTO
CTS
CVX
CW
CWT
CX
CYD
D
DBD
DCI
DDAIF
DDF
ECF
EPAC
FAX""".split('\n')