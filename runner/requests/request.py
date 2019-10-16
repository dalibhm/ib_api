class Request:
    def send(self):
        pass

    def get_stock_listing(self):
        pass

class HistoricalRequest(Request):
    def __init__(self, stock, params):
        pass

    def prepare_params(self):
        pass

    def send(self):
        pass
    # see historical data request in Scripts. there is already good stuff there



    def get_stock_listing(self, stock):
        r = requests.get('{}/stocks/{}'.format(self.data_api_url, stock))
        if r.status_code:
            # logger.info('get exchanges request status = {}'.format(r.status_code))
            print('get exchanges request status = {}'.format(r.status_code))
        return r.json()

    def get_contract(self, con_id):
        r = requests.get('{}/contracts/{}'.format(self.data_api_url, con_id))
        if r.status_code:
            # logger.info('get exchanges request status = {}'.format(r.status_code))
            print('get exchanges request status = {}'.format(r.status_code))
        return r.json()