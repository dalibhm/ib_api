import json

import requests
from ibapi.common import BarData

from proto import request_data_pb2

DATA_API_URL = 'http://localhost:5000'

report_type_mapping = {
    'ReportsFinStatements': 'financial_reports',
    'CalendarReport': 'calendar_reports',
    'ReportSnapshot': 'financial_snapshots',
    'ReportsFinSummary': 'financial_summaries'
}


class DataApiClient:
    def __init__(self):
        pass

    def post_financial_data(self, request: request_data_pb2.FundamentalDataRequest, xml_data):
        symbol = request.contract.symbol
        report_type = request.reportType
        report = {'symbol': symbol, 'xml': xml_data}

        r = requests.post('{}/{}/stocks'.format(DATA_API_URL, report_type_mapping[report_type]), data=json.dump(report))
        self.logger.info('{} {}: post request status = {}'.format(symbol, report_type, r.status_code))

    def post_historical_data(self, request: request_data_pb2.HistoricalDataRequest, bar: BarData):
        symbol = request.contract.symbol
        data = {
            'symbol': symbol,
            'secType': request.contract.secType,
            'exchange': request.contract.exchange,
            'currency': request.contract.currency,
            'endDateTime': request.endDateTime,
            'duration': request.duration,
            'barSize': request.barSize,
            'whatToShow': request.whatToShow,
            'useRTH': request.useRTH,
            'date': bar.date,
            'open': bar.open,
            'high': bar.high,
            'close': bar.close,
            'volume': bar.volume,
            'barCount': bar.barCount,
            'average': bar.average
        }
        r = requests.post('{}/{}/stocks'.format(DATA_API_URL, symbol), data=json.dump(data))
        self.logger.info('{} {}: post request status = {}'.format(symbol, bar.date, r.status_code))

    def post_contract_details(self, contract_details):
        r = requests.post('{}/contracts/details'.format(DATA_API_URL), data=json.dump(contract_details))
        self.logger.info('{} : post request status = {}'.format(contract_details['marketName'], r.status_code))
