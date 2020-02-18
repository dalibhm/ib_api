from concurrent import futures
from configparser import ConfigParser

import grpc


from injector import Injector
from logger.Logger import LogService

from container import Container
from mongo_data.mongo_repository import MongoRepository
from proto import fundamental_data_pb2_grpc, fundamental_data_pb2


class FundamentalData(fundamental_data_pb2_grpc.FundamentalDataServicer):

    def __init__(self, repository, logger):
        self.repository = repository
        self.logger = logger

    def ProcessReport(self, request, context):
        try:
            self.logger.info('processing {} {}'.format(request.stock, request.reportType))
            self.repository.process_report(symbol=request.stock,
                                           report_type=request.reportType,
                                           report_content=request.content)
        except Exception as e:
            self.logger.exception('Error processing {} {}'.format(request.stock, request.reportType))
        return fundamental_data_pb2.Empty()

    def GetAllReports(self, request, context):
        try:
            self.logger.info('processing {} {}'.format(request.stock, request.reportType))
            results = self.repository.get_all_reports(symbol=request.stock,
                                                      report_type=request.reportType)
            for result in results:
                yield result.to_proto()

        except Exception as e:
            self.logger.exception('Error processing {} {}'.format(request.stock, request.reportType))

    def GetLatestReport(self, request, context):
        try:
            self.logger.info('processing {} {}'.format(request.stock, request.reportType))
            result = self.repository.get_latest_report(symbol=request.stock,
                                                       report_type=request.reportType)
            return result.to_proto()

        except Exception as e:
            self.logger.exception('Error processing {} {}'.format(request.stock, request.reportType))

    # def GetLatestFinancialReportDate(self, request, context):
    #     insert_date = self.repository.get_latest_report_date(symbol=request.stock, report_type='ReportsFinStatements')
    #     response = fundamental_data_pb2.ReportMetaData(reportDate='', insertDate=insert_date)
    #     return response
    #
    # def IsUpToDate(self, request, context):
    #     date, file = self.repository.get_latest_report()
    #     calendar = CalendarBuilder.load(file)
    #     response = fundamental_data_pb2.UpToDate(upToDate=calendar.is_up_to_date)
    #     return response


def serve(end_point, repository, logger):
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=4))
    fundamental_data_pb2_grpc.add_FundamentalDataServicer_to_server(FundamentalData(repository, logger), server)
    server.add_insecure_port('0.0.0.0:12399')
    # server.add_insecure_port(end_point)
    server.start()
    logger.info('[Fundamental data server started on {}]'.format(end_point))
    server.wait_for_termination()


if __name__ == '__main__':
    injector = Injector([Container])
    config = injector.get(ConfigParser)
    endpoint = config.get('services', 'fundamental_data')
    logger = injector.get(LogService).Logger(__name__)


    # FileManager.init_directory(os.path.join('.', 'data'))
    from mongo_data import mongo_init

    mongo_init.global_init(config)
    repository = MongoRepository
    serve(endpoint, repository, logger)
