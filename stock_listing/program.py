import logging
import os
import time
from configparser import ConfigParser

from container import Container
from data.repository import Repository
from parsers.exchange_parser import ExchangeParser
from parsers.stock_parser_bis import StockParser

base_url = 'https://www.interactivebrokers.co.uk/en/'

url_exchange_listings = {
    'US': 'https://www.interactivebrokers.co.uk/en/index.php?f=41307',
    'EUROPE': 'https://www.interactivebrokers.co.uk/en/index.php?f=41307&p=europe_stk'
}


def init_db():
    environment = os.getenv('ENVIRONMENT') or 'development'
    config = ConfigParser()
    config.read(os.path.join('settings', environment + '.ini'))

    Repository.init(config=config)


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


def get_exchanges(repository):
    for url in url_exchange_listings.values():
        exchange_parser = ExchangeParser(url=url, repository=repository)
        exchange_parser.parse_and_post()


def get_stocks(repository):
    exchanges = repository.get_all_exchanges()

    for exchange in exchanges:
        print('[ Downloading stock listing for exchange {} ]'.format(exchange.code))

        exchange_url = base_url + exchange.link
        print(exchange_url)

        stock_parser = StockParser(exchange=exchange, repository=repository)
        # stock_parser.get_stocks()
        stock_parser.write_stocks()


def main():
    init_logger()

    container = Container()
    injector = container.injector
    repository = injector.get(Repository)

    get_exchanges(repository)
    get_stocks(repository)


if __name__ == '__main__':
    main()
