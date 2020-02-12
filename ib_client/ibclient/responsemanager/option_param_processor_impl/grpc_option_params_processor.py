import logging
from configparser import ConfigParser

import grpc
from ibapi.common import SetOfString, SetOfFloat
from injector import inject

from _external import option_params_pb2, option_params_pb2_grpc
from responsemanager import OptionParamsProcessor

logger = logging.getLogger(__name__)


class GrpcOptionParamsProcessor(OptionParamsProcessor):

    @inject
    def __init__(self, config: ConfigParser):
        server_url = config.get('services', 'option_params')
        self.channel = grpc.insecure_channel(server_url)
        self.stub = option_params_pb2_grpc.OptionParamsServiceStub(self.channel)

    def process_data(self, request_id, request, exchange: str,
                     underlyingConId: int, tradingClass: str, multiplier: str,
                     expirations: SetOfString, strikes: SetOfFloat):
        pb = option_params_pb2.OptionParams()
        pb.exchange = exchange
        pb.underlyingConId = underlyingConId
        pb.tradingClass = tradingClass
        pb.multiplier = int(multiplier)
        pb.expirations.extend(expirations)
        pb.strikes.extend(strikes)
        try:
            self.stub.AddRecord(pb)
        except grpc.RpcError as e:
            logger.exception(
                'error sending data to option params server {} {}'.format(request.contract.symbol,
                                                                        request.reportType))

    def process_data_end(self, request_id, request):
        pass

    def process_error(self, request_id, request, error_code, error_string):
        raise NotImplementedError
