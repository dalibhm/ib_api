import logging
from configparser import ConfigParser

import grpc
from injector import inject

from responsemanager.contract_details_processor import ContractDetailsProcessor
from _external import contract_pb2
from _external import contract_pb2_grpc

logger = logging.getLogger(__name__)


class GrpcContractDetailsProcessor(ContractDetailsProcessor):

    @inject
    def __init__(self, config: ConfigParser):
        server_url = config.get('services', 'contract_details')
        self.channel = grpc.insecure_channel(server_url)
        self.stub = contract_pb2_grpc.ContractServiceStub(self.channel)

    def process_data(self, request_id, request, contract_details):
        contract_details_dict = contract_details.__dict__
        contract = contract_details_dict.pop('contract')
        contract_details_dict['contractId'] = contract.conId
        contract_details = contract_pb2.ContractDetails(**contract_details_dict)
        contract_message = contract_pb2.Contract(**contract.__dict__)
        try:
            self.stub.AddContractDetails(contract_details)
            self.stub.AddContract(contract_message)
        except grpc.RpcError as e:
            logger.exception(
                'error sending data tp fundamental server {}'.format(contract))

    def process_data_end(self, request_id, request):
        pass

    def process_error(self, request_id, request, error_code, error_string):
        print(request_id, request, error_code, error_string)
