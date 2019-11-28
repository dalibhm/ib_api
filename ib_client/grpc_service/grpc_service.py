from ibapi.contract import Contract
from .kafka_producer import KafkaRequestManager
from Services.LogService import LogService
from connection_manager import ConnectionManager

from proto import request_data_pb2, request_data_pb2_grpc

import grpc
from concurrent import futures
import time

from ib_client import IbClient
from Services.request_id_generator import RequestIdGenerator
from requestmanager.requestmanager import RequestManager

_ONE_DAY_IN_SECONDS = 200000
# 55.55 hours


def get_contract(request):
    # self.logger.info(request.contract)
    contract = Contract()
    contract.conId = request.contract.conId
    contract.symbol = request.contract.symbol
    contract.secType = request.contract.secType
    contract.exchange = request.contract.exchange
    contract.primaryExchange = request.contract.primaryExchange
    contract.currency = request.contract.currency
    return contract


class RequestService(request_data_pb2_grpc.RequestDataServicer):

    def __init__(self, config, ib_client: IbClient, request_manager: RequestManager, connection_manager):
        # super.__init__()
        self.ib_client = ib_client
        self.request_id_gen = RequestIdGenerator()
        self.request_manager = request_manager
        self.connection_manager = connection_manager
        self.logger = LogService.get_startup_log()
        self.kafka_request_manager = KafkaRequestManager(config)

    # these logs propagate to the root logger
    # self.logger = logging.getLogger(type(self).__name__)
    # self.logger.setLevel(logging.INFO)
    # log_name = '{}.log'.format(type(self).__name__)
    # file_handler = logging.FileHandler(log_name)
    # formatter = logging.Formatter('%(asctime)-15s %(levelname)s %(name)-s %(message)s')
    # file_handler.setFormatter(formatter)
    # self.logger.addHandler(file_handler)

    def RequestContractDetails(self, request, context):
        contract = get_contract(request)
        request_id = self.request_id_gen.get_id()
        self.logger.notice("sending request {} for contract details : {}".format(request_id, contract))
        self.ib_client.reqContractDetails(request_id, contract)
        return request_data_pb2.Status(message=True)

    def RequestHistoricalData(self, request, context):
        contract = get_contract(request)
        request_id = self.request_id_gen.get_id()
        self.logger.notice("sending request {} for historical data : {}".format(request_id, contract))
        try:
            # avoid more than 50 requests at a time
            while self.request_manager.requests_number() > 40:
                continue
            self.request_manager.register_request(request_id, request)
            self.kafka_request_manager.push_historical_request(request_id, request)
            self.ib_client.reqHistoricalData(request_id,
                                             contract,
                                             request.endDateTime,
                                             request.durationString,
                                             request.barSizeSetting,
                                             request.whatToShow,
                                             int(request.useRTH),
                                             request.formatDate,
                                             int(request.keepUpToDate),
                                             []
                                             )
            return request_data_pb2.Status(message=True)
        except Exception as e:
            self.logger.exception('Unable to request {} historical data for {}'.format(request_id,
                                                                                       contract)
                                  )

    def RequestFundamentalData(self, request, context):
        contract = get_contract(request)
        request_id = self.request_id_gen.get_id()
        self.logger.notice("sending fundamental request {} for {:15s} : {}".format(request_id,
                                                                                   request.reportType,
                                                                                   request.contract.symbol))
        try:
            self.request_manager.register_request(request_id, request)
            self.ib_client.reqFundamentalData(request_id,
                                              contract,
                                              request.reportType,
                                              []
                                              )
        except BrokenPipeError:
            self.connection_manager.reconnect()
            return request_data_pb2.Status(message=False)
        except Exception as e:
            self.logger.exception('Unable to request {}  {} for {:15s}'.format(request_id,
                                                                               request.reportType,
                                                                               request.contract.symbol))
            return request_data_pb2.Status(message=False)
        return request_data_pb2.Status(message=True)


def serve(ib_client: IbClient, config, request_manager: RequestManager, max_workers,
          connection_manager: ConnectionManager):
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=max_workers))
    request_data_pb2_grpc.add_RequestDataServicer_to_server(RequestService(config,
                                                                           ib_client,
                                                                           request_manager,
                                                                           connection_manager),
                                                            server
                                                            )

    end_point = config.get('services', 'ib')
    server.add_insecure_port(end_point)
    server.start()
    print("server started on {}".format(end_point))
    try:
        while True:
            time.sleep(_ONE_DAY_IN_SECONDS)
    except KeyboardInterrupt:
        server.stop(0)
