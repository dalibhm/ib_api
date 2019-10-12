from __future__ import print_function
import datetime
from time import sleep
from Services.HistoricalDataService import HistoricalDataService
from historical_client.historical_request import PriceType, HistoricalRequest
from historical_client.stock_provider import get_contracts


historical_data_service = HistoricalDataService()

end_date = '20190701'
start_date = '20100101'
bar_size = '1 day'
price_type = PriceType.TRADES
request_args = HistoricalRequest(start_date, end_date, bar_size, price_type).request_args()


contracts = get_contracts()
for contract in contracts[:1]:
    historical_data_service.request_historical_data(contract, **request_args)
    sleep(1)

