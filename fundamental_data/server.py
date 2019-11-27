import logging
import os
from concurrent import futures
from configparser import ConfigParser

import grpc

from calendar_reports.calendar_builder import CalendarBuilder
from file_manager import FileManager
from mongo_repository import MongoRepository
from proto import fundamental_data_pb2
from proto import fundamental_data_pb2_grpc


class FundamentalData(fundamental_data_pb2_grpc.FundamentalDataServicer):

    def __init__(self, repository):
        self.repository = repository

    def ProcessReport(self, request, context):
        self.repository.process_report(symbol=request.stock,
                                       report_type=request.reportType,
                                       report_content=request.content)
        return fundamental_data_pb2.Empty()

    def GetLatestFinancialReportDate(self, request, context):
        insert_date = self.repository.get_latest_report_date(symbol=request.stock, report_type='ReportsFinStatements')
        response = fundamental_data_pb2.ReportMetaData(reportDate='', insertDate=insert_date)
        return response

    def IsUpToDate(self, request, context):
        date, file = self.repository.get_latest_report()
        calendar = CalendarBuilder.load(file)
        response = fundamental_data_pb2.UpToDate(upToDate=calendar.is_up_to_date)
        return response


def serve(end_point, repository):
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=4))
    fundamental_data_pb2_grpc.add_FundamentalDataServicer_to_server(FundamentalData(repository), server)
    server.add_insecure_port(end_point)
    server.start()
    print('Fundamental data server started...')
    server.wait_for_termination()


if __name__ == '__main__':
    config = ConfigParser()
    config.read(os.path.join('..', 'settings', 'development.ini'))
    logging.basicConfig()
    end_point = config.get('services', 'fundamental_data')

    # FileManager.init_directory(os.path.join('.', 'data'))
    from mongo_model import mongo_init

    mongo_init.global_init()
    repository = MongoRepository
    serve(end_point, repository)
