from ibapi.contract import Contract

from Services.LogService import LogService

from proto import request_data_pb2, request_data_pb2_grpc

import grpc
from concurrent import futures
import time

from ib_client import IbClient
from Services.request_id_generator import RequestIdGenerator
from requestmanager.requestmanager import RequestManager

_ONE_DAY_IN_SECONDS = 200000


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


class RequestData(request_data_pb2_grpc.RequestDataServicer):

    def __init__(self, ib_client: IbClient, request_manager: RequestManager):
        # super.__init__()
        self.ib_client = ib_client
        self.request_id_gen = RequestIdGenerator()
        self.request_manager = request_manager

        self.logger = LogService.get_startup_log()

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
            self.request_manager.register_request(request_id, request)
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
        except:
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
        except Exception as e:
            self.logger.exception('Unable to request {}  {} for {:15s} : {}'.format(request_id,
                                                                                    request.reportType,
                                                                                    request.contract.symbol))

        return request_data_pb2.Status(message=True)


def serve(ib_client: IbClient, config, request_manager: RequestManager, max_workers):
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=max_workers))
    request_data_pb2_grpc.add_RequestDataServicer_to_server(RequestData(ib_client, request_manager),
                                                            server
                                                            )
    server.add_insecure_port(config.get('services', 'ib'))
    server.start()
    print("server started")
    try:
        while True:
            time.sleep(_ONE_DAY_IN_SECONDS)
    except KeyboardInterrupt:
        server.stop(0)
