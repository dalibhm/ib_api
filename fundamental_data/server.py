import logging
import os
from concurrent import futures
from configparser import ConfigParser

import grpc

from file_manager import FileManager
from proto import fundamental_data_pb2
from proto import fundamental_data_pb2_grpc


class FundamentalData(fundamental_data_pb2_grpc.FundamentalDataServicer):

    def ProcessReport(self, request, context):
        file_manager = FileManager(os.path.join('.', 'data'))

        file_manager.process_report(symbol=request.stock,
                                    report_type=request.reportType,
                                    report_content=request.content)
        return fundamental_data_pb2.Empty()

    def GetLatestFinancialReportDate(self, request, context):
        file_manager = FileManager(os.path.join('.', 'data'))
        insert_date = file_manager.get_latest_report_date(symbol=request.stock, report_type='ReportsFinStatements')
        response = fundamental_data_pb2.ReportMetaData(reportDate='', insertDate=insert_date)
        return response


def serve(end_point):
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    fundamental_data_pb2_grpc.add_FundamentalDataServicer_to_server(FundamentalData(), server)
    server.add_insecure_port(end_point)
    server.start()
    print('Fundamental data server started...')
    server.wait_for_termination()


if __name__ == '__main__':
    config = ConfigParser()
    config.read(os.path.join('..', 'settings', 'development.ini'))
    logging.basicConfig()
    end_point = config.get('services', 'fundamental_data')
    serve(end_point)
