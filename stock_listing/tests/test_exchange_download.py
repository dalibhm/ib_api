from stock_listing.parsers.exchange_parser import ExchangeParser

base_url = 'https://www.interactivebrokers.co.uk/en/'

url_exchange_listings = {
    'US': 'https://www.interactivebrokers.co.uk/en/index.php?f=41307',
    'EUROPE': 'https://www.interactivebrokers.co.uk/en/index.php?f=41307&p=europe_stk'
}

url_us = url_exchange_listings['US']


def test_exchange_download_html():
    exchange_parser = ExchangeParser(url_us)
    exchange_parser.download_html()
    assert exchange_parser.html


def test_exchange_parse_html():
    exchange_parser = ExchangeParser(url_us)
    exchange_parser.download_html()
    exchange_parser.parse_html()
    assert len(exchange_parser.exchanges) > 0
