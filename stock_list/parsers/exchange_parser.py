import logging
import re
import requests
import json
from bs4 import BeautifulSoup

from parsers.http import get_url_content

REG_EX = re.compile(r'.*exch=(.*?)&.*')


class ExchangeParser:
    def __init__(self, url, api_url):
        self.url = url
        self.api_url = api_url
        self.html = ''
        self.logger = logging.getLogger('stock_parser')
        self.exchanges = []

    def parse_and_post(self):
        self.download_html()
        self.parse_html()
        self.post_exchanges()

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

    def post_exchanges(self):
        self.logger.info('sending to api')
        for exchange in self.exchanges:
            # print(exchange)
            r = requests.post('{}/exchanges'.format(self.api_url), json=exchange)
            self.logger.info('{}: post request status = {}'.format(exchange['code'], r.status_code))


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
