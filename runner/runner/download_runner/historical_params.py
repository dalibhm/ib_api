from datetime import datetime, timedelta

from injector import inject


class HistoricalParams:
    @inject
    def __init__(self, start_date, end_date):
        self.start_date = start_date
        self.end_date = end_date

    def __copy__(self):
        return HistoricalParams(self.start_date, self.end_date)

    def check_for_symbol(self, symbol, historical_data_service):
        start_date = datetime.strptime(self.start_date, '%Y-%m-%d')
        end_date = datetime.strptime(self.end_date, '%Y-%m-%d')

        latest_timestamp = historical_data_service.get_latest_timestamp(symbol, "%Y-%m-%d")
        if latest_timestamp:
            latest = datetime.strptime(latest_timestamp, '%Y-%m-%d')
            if latest >= end_date - timedelta(days=1):
                logger.info('latest data already ib database for {}'.format(symbol))
                return contract, None
            elif start_date >= end_date - timedelta(days=1):
                start_date = latest

        params = {
            "start_date": start_date.strftime('%Y%m%d'),  # "1999-01-01",
            "end_date": end_date.strftime('%Y%m%d'),  # "2019-11-27",
            "bar_size": "1 day",
            "price_type": "TRADES"
        }
        params_manager = HistoricalRequestTemplate(params)
        arranged_params = params_manager.get_ib_params()
        contract['exchange'] = 'SMART'
        return contract, arranged_params
