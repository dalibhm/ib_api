import grpc

from proto import fundamental_data_pb2_grpc, fundamental_data_pb2


class Client:
    def __init__(self, server_url):
        self.server_url = server_url
        self.channel = grpc.insecure_channel(self.server_url)
        self.stub = fundamental_data_pb2_grpc.FundamentalDataStub(self.channel)

    def process_data(self, symbol, report_type, content):
        report = fundamental_data_pb2.Report(stock=symbol,
                                             reportType=report_type,
                                             content=content)
        try:
            self.stub.ProcessReport(report)
        except grpc.RpcError as e:
            print(e)

    def get_all_reports(self, symbol, report_type):
        report = fundamental_data_pb2.Report(stock=symbol,
                                             reportType=report_type)
        try:
            yield from self.stub.GetAllReports(report)
        except grpc.RpcError as e:
            print(e)

    def get_latest_report(self, symbol, report_type):
        report = fundamental_data_pb2.Report(stock=symbol,
                                             reportType=report_type)
        try:
            return self.stub.GetLatestReport(report)
        except grpc.RpcError as e:
            print(e)


if __name__ == '__main__':
    url = '127.0.0.1:12399'
    client = Client(server_url=url)

