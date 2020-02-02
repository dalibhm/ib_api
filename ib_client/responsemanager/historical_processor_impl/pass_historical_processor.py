from responsemanager.historical_processor import HistoricalDataProcessor

from ibapi.common import BarData


class PassHistoricalDataProcessor(HistoricalDataProcessor):

    def process_data(self, request_id, request, bar_data: BarData):
        pass

    def process_data_end(self, request_id: int, request, start: str, end: str):
        pass

    def process_error(self, request_id: int, request, errorCode: int, errorString: str):
        pass
