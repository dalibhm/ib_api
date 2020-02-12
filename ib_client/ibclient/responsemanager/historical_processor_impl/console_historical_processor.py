

from ibapi.common import BarData

from responsemanager.historical_processor import HistoricalDataProcessor


class ConsoleHistoricalDataProcessor(HistoricalDataProcessor):

    def process_data(self, request_id, request, bar_data: BarData):
        print(request_id, bar_data)

    def process_data_end(self, request_id: int, request, start: str, end: str):
        print(request_id, start, end)

    def process_error(self, request_id: int, request, errorCode: int, errorString: str):
        print(request_id, errorCode, errorString)
