# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import proto.fundamental_data_pb2 as fundamental__data__pb2


class FundamentalDataStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.ProcessReport = channel.unary_unary(
        '/fundamental_data.FundamentalData/ProcessReport',
        request_serializer=fundamental__data__pb2.Report.SerializeToString,
        response_deserializer=fundamental__data__pb2.Empty.FromString,
        )
    self.GetAllReports = channel.unary_stream(
        '/fundamental_data.FundamentalData/GetAllReports',
        request_serializer=fundamental__data__pb2.Report.SerializeToString,
        response_deserializer=fundamental__data__pb2.Report.FromString,
        )
    self.GetLatestReport = channel.unary_unary(
        '/fundamental_data.FundamentalData/GetLatestReport',
        request_serializer=fundamental__data__pb2.Report.SerializeToString,
        response_deserializer=fundamental__data__pb2.Report.FromString,
        )
    self.GetLatestFinancialReportDate = channel.unary_unary(
        '/fundamental_data.FundamentalData/GetLatestFinancialReportDate',
        request_serializer=fundamental__data__pb2.StockRequest.SerializeToString,
        response_deserializer=fundamental__data__pb2.ReportMetaData.FromString,
        )
    self.IsUpToDate = channel.unary_unary(
        '/fundamental_data.FundamentalData/IsUpToDate',
        request_serializer=fundamental__data__pb2.StockRequest.SerializeToString,
        response_deserializer=fundamental__data__pb2.UpToDate.FromString,
        )


class FundamentalDataServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def ProcessReport(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetAllReports(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetLatestReport(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetLatestFinancialReportDate(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def IsUpToDate(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_FundamentalDataServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'ProcessReport': grpc.unary_unary_rpc_method_handler(
          servicer.ProcessReport,
          request_deserializer=fundamental__data__pb2.Report.FromString,
          response_serializer=fundamental__data__pb2.Empty.SerializeToString,
      ),
      'GetAllReports': grpc.unary_stream_rpc_method_handler(
          servicer.GetAllReports,
          request_deserializer=fundamental__data__pb2.Report.FromString,
          response_serializer=fundamental__data__pb2.Report.SerializeToString,
      ),
      'GetLatestReport': grpc.unary_unary_rpc_method_handler(
          servicer.GetLatestReport,
          request_deserializer=fundamental__data__pb2.Report.FromString,
          response_serializer=fundamental__data__pb2.Report.SerializeToString,
      ),
      'GetLatestFinancialReportDate': grpc.unary_unary_rpc_method_handler(
          servicer.GetLatestFinancialReportDate,
          request_deserializer=fundamental__data__pb2.StockRequest.FromString,
          response_serializer=fundamental__data__pb2.ReportMetaData.SerializeToString,
      ),
      'IsUpToDate': grpc.unary_unary_rpc_method_handler(
          servicer.IsUpToDate,
          request_deserializer=fundamental__data__pb2.StockRequest.FromString,
          response_serializer=fundamental__data__pb2.UpToDate.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'fundamental_data.FundamentalData', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
