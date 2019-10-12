import requests

from log_service import init_logger
from parsers.exchange_parser import ExchangeParser
from parsers.as_stock_parser import StockParser

from configparser import ConfigParser


base_url = 'https://www.interactivebrokers.co.uk/en/'

url_exchange_listings = {
    'US': 'https://www.interactivebrokers.co.uk/en/index.php?f=41307',
    'EUROPE': 'https://www.interactivebrokers.co.uk/en/index.php?f=41307&p=europe_stk'
}


def get_exchanges(logger, api_url):
    for url in url_exchange_listings.values():
        exchange_parser = ExchangeParser(url, api_url)
        exchange_parser.parse_and_post()


def get_stocks(logger, api_url):
    r = requests.get('{}/exchanges'.format(api_url))
    if r.status_code:
        logger.info('get exchanges request status = {}'.format(r.status_code))

    exchanges = r.json()['exchanges']
    print("exchanges : {}", exchanges)
    for exchange in exchanges:
        exchange_url = base_url + exchange['link']
        stock_parser = StockParser(exchange_url, exchange['name'], api_url)
        stock_parser.parse_stock_web_pages()


def main():
    config = ConfigParser()
    config.read('./setup/development.ini')
    api_url = config.get('API', 'DATA_API_URL')
    logger = init_logger()
    # get_exchanges(logger, api_url)
    get_stocks(logger, api_url)


if __name__ == '__main__':
    main()
