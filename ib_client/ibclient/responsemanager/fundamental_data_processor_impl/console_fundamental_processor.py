import logging

from responsemanager.fundamental_processor import FundamentalDataProcessor

logger = logging.getLogger(__name__)


class ConsoleFundamentalDataProcessor(FundamentalDataProcessor):
    def process_data(self, request_id, request, xml_data):
        print(request_id, xml_data)

    def process_data_end(self, request_id, request):
        print(request_id, 'data end')

    def process_error(self, request_id, request, error_code, error_string):
        print(request_id, error_code, error_string)
