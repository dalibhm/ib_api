from parsers.exchange_parser import ExchangeParser


def test_exchange_parser():
    url_exchange_listings = {
        'US': 'https://www.interactivebrokers.co.uk/en/index.php?f=41307',
        'EUROPE': 'https://www.interactivebrokers.co.uk/en/index.php?f=41307&p=europe_stk'
    }

    for key in url_exchange_listings.keys():
        exchange_parser = ExchangeParser(url_exchange_listings[key])
        exchange_parser.download_html()
        exchange_parser.parse_html()
        exchanges = exchange_parser.exchanges
        for exchange in exchanges:
            assert isinstance(exchange, dict)
            assert all(a in ['code', 'name', 'security_type', 'opening_hours', 'link'] for a in exchange.keys())
