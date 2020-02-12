from stock_listing.parsers.stock_parser_bis import StockParser
from data.exchange import Exchange

base_url = 'https://www.interactivebrokers.co.uk/en/'

url_exchange_listings = {
    'US': 'https://www.interactivebrokers.co.uk/en/index.php?f=41307',
    'EUROPE': 'https://www.interactivebrokers.co.uk/en/index.php?f=41307&p=europe_stk'
}
# code,name,security_type,opening_hours,link
# arcaedge,ArcaEdge (ARCAEDGE),Stocks (OTCBB),Monday - Friday: 7:30-16:01,

exchange = Exchange()
url_us = url_exchange_listings['US']

exchange.code = 'arcaedge'
exchange.link = 'index.php?f=41295&exch=arcaedge&showcategories=STK'


def test_stock_download_html():
    stock_parser = StockParser(exchange=exchange)
    stock_parser.get_stocks()
    assert stock_parser.first_html


# def test_stock_parse_html():
#     exchange_parser = ExchangeParser(url_us)
#     exchange_parser.download_html()
#     exchange_parser.parse_html()
#     assert len(exchange_parser.exchanges) > 0
