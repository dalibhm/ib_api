import asyncio
import threading

from configparser import ConfigParser
from types import coroutine

from ddtrace import tracer, Tracer
from ibapi.contract import Contract
from injector import inject

from enums.request_type import RequestType
from .kafka_producer import KafkaRequestManager
from Services.LogService import LogService
from connection_manager.connection_manager import ConnectionManager

from proto import request_data_pb2, request_data_pb2_grpc

import grpc
from concurrent import futures
import time

from api.ib_client import IbClient
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


class RequestServicer(request_data_pb2_grpc.RequestDataServicer):

    def __init__(self,
                 request_manager: RequestManager):
        # super.__init__()
        # self.historical_requests_number_limit = config.getint('ib client', 'historical-requests-number-limit')
        self.request_manager: RequestManager = request_manager
        self.logger = LogService.get_startup_log()
        self.lock = threading.Lock()

    def RequestContractDetails(self, request, context):
        try:
            self.request_manager.add_request(request, RequestType.ContractDetails)
        except Exception as e:
            return request_data_pb2.Status(message=False)

        return request_data_pb2.Status(message=True)

    def RequestSecDefOptParams(self, request, context):
        try:
            self.request_manager.add_request(request, RequestType.SecDefOptParams)
        except:
            return request_data_pb2.Status(message=False)

        return request_data_pb2.Status(message=True)

    # @tracer.wrap(name='request entry', service='historical req')
    # @coroutine
    def RequestHistoricalData(self, request, context):
        try:
            context = tracer.get_call_context()
            coro = self.request_manager.add_request(request, RequestType.Historical, context)
            status = asyncio.run(coro)

            return request_data_pb2.Status(message=status)
        except Exception as e:
            return request_data_pb2.Status(message=False)



    def RequestFundamentalData(self, request, context):
        try:
            self.request_manager.add_request(request, RequestType.Fundamental)
        except:
            return request_data_pb2.Status(message=False)
        return request_data_pb2.Status(message=True)


class GrpcServer:
    @inject
    def __init__(self, config: ConfigParser, request_manager: RequestManager):
        max_workers = config.getint('ib client', 'grpc-workers')
        server = grpc.server(futures.ThreadPoolExecutor(max_workers=max_workers))

        request_data_pb2_grpc.add_RequestDataServicer_to_server(
            RequestServicer(request_manager),
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
