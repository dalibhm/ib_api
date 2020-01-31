import grpc

from proto.contract_details import contract_details_pb2, contract_details_pb2_grpc


class ContractsService:
    def __init__(self, server_url):
        self.logger = None
        self.channel = grpc.insecure_channel(server_url)
        self.stub = contract_details_pb2_grpc.ContractDetailsServiceStub(self.channel)

    def get_contract_details(self, con_id: int):
        """
        I kept the protobuffer object as a result, until I decide what to do with it

        :param con_id:
        :return: ontract_details_pb2.ContractDetails objects
        """
        request = contract_details_pb2.Request(conId=con_id)
        response = self.stub.GetContractDetails(request)
        return response
