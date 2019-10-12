import logging

from bs4 import BeautifulSoup

from parsers.http import get_url_content
from mongo_files.exchange import Exchange


class ExchangeParser:
    def __init__(self, url):
        self.url = url
        self.html = ''
        self.logger = logging.getLogger('stock_parser')
        self.exchanges = []

    def parse_and_save(self):
        self.download_html()
        self.parse_html()
        self.write_to_db()

    def download_html(self):
        self.logger.info('sending request for {}'.format(self.url))
        self.html = get_url_content(self.url)
        self.logger.info('response received for {}'.format(self.url))

    def parse_html(self):
        soup = BeautifulSoup(self.html, 'html.parser')
        rows = soup.find_all('tr')
        self.logger.info('parsing {} rows'.format(len(rows)))
        for row in rows:
            exchange = parse_exchange_row(row)
            if exchange:
                self.exchanges.append(exchange)

    def write_to_db(self):
        self.logger.info('saving to db if not already there')
        for exchange in self.exchanges:
            if not Exchange.objects().filter(name=exchange['name']).limit(1):
                record = Exchange(**exchange)
                record.save()
                self.logger.info('added to db : {}'.format(exchange))


def parse_exchange_row(row):
    cells = row.find_all('td')
    if len(cells) == 0:
        return

    start_index = 0
    href = cells[start_index].find('a')
    if href is None:
        start_index = 1
        href = cells[start_index].find('a')
    return {'link': href['href'].strip(),
            'name': cells[start_index].text.strip(),
            'security_type': cells[start_index + 1].text.strip(),
            'opening_hours': cells[start_index + 2].text.strip()
            }
