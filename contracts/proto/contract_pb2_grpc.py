# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

from . import contract_pb2 as contract__pb2


class ContractServiceStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.GetContract = channel.unary_unary(
        '/contracts.ContractService/GetContract',
        request_serializer=contract__pb2.Request.SerializeToString,
        response_deserializer=contract__pb2.Contract.FromString,
        )
    self.AddContract = channel.unary_unary(
        '/contracts.ContractService/AddContract',
        request_serializer=contract__pb2.Contract.SerializeToString,
        response_deserializer=contract__pb2.Empty.FromString,
        )
    self.GetContractDetails = channel.unary_unary(
        '/contracts.ContractService/GetContractDetails',
        request_serializer=contract__pb2.Request.SerializeToString,
        response_deserializer=contract__pb2.ContractDetails.FromString,
        )
    self.AddContractDetails = channel.unary_unary(
        '/contracts.ContractService/AddContractDetails',
        request_serializer=contract__pb2.ContractDetails.SerializeToString,
        response_deserializer=contract__pb2.Empty.FromString,
        )


class ContractServiceServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def GetContract(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def AddContract(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetContractDetails(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def AddContractDetails(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_ContractServiceServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'GetContract': grpc.unary_unary_rpc_method_handler(
          servicer.GetContract,
          request_deserializer=contract__pb2.Request.FromString,
          response_serializer=contract__pb2.Contract.SerializeToString,
      ),
      'AddContract': grpc.unary_unary_rpc_method_handler(
          servicer.AddContract,
          request_deserializer=contract__pb2.Contract.FromString,
          response_serializer=contract__pb2.Empty.SerializeToString,
      ),
      'GetContractDetails': grpc.unary_unary_rpc_method_handler(
          servicer.GetContractDetails,
          request_deserializer=contract__pb2.Request.FromString,
          response_serializer=contract__pb2.ContractDetails.SerializeToString,
      ),
      'AddContractDetails': grpc.unary_unary_rpc_method_handler(
          servicer.AddContractDetails,
          request_deserializer=contract__pb2.ContractDetails.FromString,
          response_serializer=contract__pb2.Empty.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'contracts.ContractService', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
