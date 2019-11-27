import logging
import os
import time


from data.db_factory import DbSessionFactory
from data.repository import Repository
from parsers.exchange_parser import ExchangeParser
from parsers.stock_parser import StockParser


base_url = 'https://www.interactivebrokers.co.uk/en/'

url_exchange_listings = {
    'US': 'https://www.interactivebrokers.co.uk/en/index.php?f=41307',
    'EUROPE': 'https://www.interactivebrokers.co.uk/en/index.php?f=41307&p=europe_stk'
}


def init_db():
    # settings = config.get_settings()
    # db_file = settings.get('db_filename')

    DbSessionFactory.global_init()


def init_logger():
    if not os.path.exists("log"):
        os.makedirs("log")

    log_file = time.strftime("./log/listing_%Y%m%d_%H%M%S.log")
    recfmt = '(%(threadName)s) %(asctime)s.%(msecs)03d %(levelname)s %(filename)s:%(lineno)d %(message)s'
    timefmt = '%y%m%d_%H:%M:%S'

    logger = logging.getLogger('listing')
    logger.setLevel(logging.DEBUG)
    formatter = logging.Formatter(fmt=recfmt, datefmt=timefmt)
    file_handler = logging.FileHandler(log_file)
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    console = logging.StreamHandler()
    console.setLevel(logging.ERROR)
    logger.addHandler(console)


def get_exchanges():
    for url in url_exchange_listings.values():
        exchange_parser = ExchangeParser(url)
        exchange_parser.parse_and_post()


def get_stocks():
    exchanges = Repository.get_all_exchanges()

    for exchange in exchanges:
        print('[ Downloading stock listing for exchange {} ]'.format(exchange))

        exchange_url = base_url + exchange.link
        print(exchange_url)

        stock_parser = StockParser(exchange_url, exchange.code)
        stock_parser.parse_stock_web_pages()


def main():
    # config = ConfigParser()
    # config.read('./setup/development.ini')
    init_db()
    init_logger()
    get_exchanges()
    get_stocks()


if __name__ == '__main__':
    main()
