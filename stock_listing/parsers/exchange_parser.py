import logging
import re
import requests
from bs4 import BeautifulSoup

from data.repository import Repository

REG_EX = re.compile(r'.*exch=(.*?)&.*')


class ExchangeParser:
    def __init__(self, url):
        self.url = url
        self.html = ''
        self.logger = logging.getLogger('listing')
        self.exchanges = []

    def parse_and_post(self):
        self.download_html()
        self.parse_html()
        self.post_exchanges()

    def download_html(self):
        self.logger.info('sending request for {}'.format(self.url))
        response = requests.get(self.url)
        if response:
            self.html = response.text
        self.logger.debug('response received for {}'.format(self.url))

    def parse_html(self):
        soup = BeautifulSoup(self.html, 'html.parser')
        rows = soup.find_all('tr')
        self.logger.debug('parsing {} rows'.format(len(rows)))
        for row in rows:
            exchange = parse_exchange_row(row)
            if exchange:
                self.exchanges.append(exchange)

    def post_exchanges(self):
        self.logger.info('adding exchane')
        for exchange in self.exchanges:
            Repository.add_exchange(exchange)


def parse_exchange_row(row):
    cells = row.find_all('td')
    if len(cells) == 0:
        return

    start_index = 0
    href = cells[start_index].find('a')
    if href is None:
        start_index = 1

    href = cells[start_index].find('a')
    link = href['href'].strip()
    code = REG_EX.findall(link)[0]
    return {'link': link,
            'code': code,
            'name': cells[start_index].text.strip(),
            'security_type': cells[start_index + 1].text.strip(),
            'opening_hours': cells[start_index + 2].text.strip()
            }
