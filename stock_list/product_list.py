from parsers.stock_parser import StockParser

exchange_url = 'https://www.interactivebrokers.co.uk/en/index.php?f=41295&exch=vwap&showcategories=STK'
exchange_name = 'vwap'
stock_parser = StockParser(exchange_url, exchange_name)
stock_parser.load_stocks_from_exchange()
