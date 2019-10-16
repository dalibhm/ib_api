import grpc
from Services.Helper import contract2grpc
from Services.ServiceBase import ServiceBase
from proto import request_data_pb2_grpc, request_data_pb2


class ContractService(ServiceBase):

    def __init__(self):
        super().__init__()
        self.channel = grpc.insecure_channel('localhost:50051')
        self.stub = request_data_pb2_grpc.RequestDataStub(self.channel)

    def contract_details(self, contract):
        request = request_data_pb2.ContractDetailsRequest(contract=contract2grpc(contract))
        try:
            response = self.stub.RequestContractDetails(request)
            self.logger.info('Contract details request sent for ' + str(contract.symbol))
            self.logger.info("Client received Contract details: " + str(response.message))
        except Exception as e:
            self.logger.error("Unable to receive Contract details: " + str(e))

