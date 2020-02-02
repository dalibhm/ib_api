import logging
from configparser import ConfigParser

import grpc
from injector import inject

from proto.contract_details import contract_pb2, contract_pb2_grpc


class ContractsService:
    @inject
    def __init__(self, config: ConfigParser):
        server_url = config.get('services', 'contract_details')
        self.logger = logging.getLogger(__name__)
        self.channel = grpc.insecure_channel(server_url)
        self.stub = contract_pb2_grpc.ContractServiceStub(self.channel)

    def get_contract_details(self, con_id: int):
        """
        I kept the protobuffer object as a result, until I decide what to do with it

        :param con_id:
        :return: ontract_details_pb2.ContractDetails objects
        """
        request = contract_pb2.Request(conId=con_id)
        response = self.stub.GetContractDetails(request)
        return response

    def get_contract(self, con_id: int):
        """
        I kept the protobuffer object as a result, until I decide what to do with it

        :param con_id:
        :return: contract_pb2.Contract objects
        """
        request = contract_pb2.Request(conId=con_id)
        try:
            response = self.stub.GetContract(request)
        except:
            self.logger.exception('Error in GetContract : conId {}'.format(con_id))
            response = None
        return response
