import logging
from configparser import ConfigParser

import grpc
from injector import inject

from responsemanager.fundamental_processor import FundamentalDataProcessor
from _external import fundamental_data_pb2_grpc
from _external import fundamental_data_pb2

logger = logging.getLogger(__name__)


class ConsoleFundamentalDataProcessor(FundamentalDataProcessor):
    def process_data(self, request_id, request, xml_data):
        print(request_id, xml_data)

    def process_data_end(self, request_id, request):
        print(request_id, 'data end')

    def process_error(self, request_id, request, error_code, error_string):
        print(request_id, error_code, error_string)
