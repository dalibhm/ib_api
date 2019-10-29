import json

import requests
from ibapi.common import BarData

from ib_response_manager.response_manager import ResponseManager
from proto import request_data_pb2

report_type_mapping = {
    'ReportsFinStatements': 'financial_reports',
    'CalendarReport': 'calendar_reports',
    'ReportSnapshot': 'financial_snapshots',
    'ReportsFinSummary': 'financial_summaries'
}


class DataApiClient(ResponseManager):

    def __init__(self, data_api_url):
        self.data_api_url = data_api_url

    def process_contract_details(self, request, contract_details):
        self.post_contract_details(request, contract_details)

    def process_historical_data(self, request, bar_data):
        self.post_historical_data(request, bar_data)

    def process_financial_data(self, request, xml_data):
        self.post_financial_data(request, xml_data)

    def post_financial_data(self, request: request_data_pb2.FundamentalDataRequest, xml_data):
        report = {
            'symbol': request.contract.symbol,
            'xml': xml_data,
            'report_type': request.reportType
        }

        r = requests.post('http://{}/api/fundamental_data/xml'.format(self.data_api_url),json=report)
        # self.logger.info('{} {}: post request status = {}'.format(symbol, report_type, r.status_code))

    def post_historical_data(self, request: request_data_pb2.HistoricalDataRequest, bar: BarData):
        symbol = request.contract.symbol
        data = {
            'symbol': symbol,
            'secType': request.contract.secType,
            'exchange': request.contract.exchange,
            'currency': request.contract.currency,
            'endDateTime': request.endDateTime,
            'duration': request.durationString,
            'barSize': request.barSizeSetting,
            'whatToShow': request.whatToShow,
            'useRTH': request.useRTH,
            'date': bar.date,
            'open': bar.open,
            'high': bar.high,
            'low': bar.low,
            'close': bar.close,
            'volume': bar.volume,
            'barCount': bar.barCount,
            'average': bar.average
        }
        r = requests.post('http://{}/api/historical_data/'.format(self.data_api_url), json=data)
        # self.logger.info('{} {}: post request status = {}'.format(symbol, bar.date, r.status_code))

    def post_contract_details(self, contract_details):
        r = requests.post('http://{}/api/contracts/details'.format(self.data_api_url), json=contract_details)
        # self.logger.info('{} : post request status = {}'.format(contract_details['marketName'], r.status_code))
