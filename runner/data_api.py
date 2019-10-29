import requests


class DataApiClient:
    def __init__(self, data_api_url):
        self.data_api_url = data_api_url

    def get_stock_listing(self, stock_symbol):
        r = requests.get('http://{}/api/stocks/symbol/{}'.format(self.data_api_url, stock_symbol))
        if r.status_code:
            # logger.info('get exchanges request status = {}'.format(r.status_code))
            print('get exchanges request status = {}'.format(r.status_code))
        return r.json()

    def post_stock(self, stock):
        r = requests.post('http://{}/api/stocks'.format(self.data_api_url), json=stock)
        # self.logger.info('{}: post request status = {}'.format(stock['ib_symbol'], r.status_code))

    def get_contract(self, con_id):
        r = requests.get('http://{}/api/contracts/{}'.format(self.data_api_url, con_id))
        if r.status_code:
            # logger.info('get exchanges request status = {}'.format(r.status_code))
            print('get exchanges request status = {}'.format(r.status_code))
        return r.json()

    def get_exchange_link(self, exchange_code):
        base_url = 'https://www.interactivebrokers.co.uk/en/'
        r = requests.get('http://{}/api/exchanges/{}'.format(self.data_api_url, exchange_code))
        if r.status_code:
            # logger.info('get exchanges request status = {}'.format(r.status_code))
            print('get exchange link request status = {}'.format(r.status_code))
        exchange_url = base_url + r.json()['link']
        return exchange_url
