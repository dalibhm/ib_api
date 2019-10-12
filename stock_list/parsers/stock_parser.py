import logging

import requests
from bs4 import BeautifulSoup

from parsers.http import get_url_content
from mongo_files.stock import Stock


class StockParser:
    def __init__(self, url, exchange_name):
        self.logger = logging.getLogger('stock_parser')
        self.url = url
        self.exchange_name = exchange_name
        self.loaded_page_number = 0
        self.html = ''
        self.get_url_content(1)
        self.number_of_web_pages = 0
        self.get_number_of_web_pages()

    def get_url_content(self, requested_page_number):
        if requested_page_number == self.loaded_page_number:
            return
        url = self.url + '&p=&cc=&limit=100&page=' + str(requested_page_number)
        self.logger.info('sending request for page {}'.format(requested_page_number))
        self.logger.info('url : {}'.format(url))
        response = requests.get(url)
        if response:
            self.html = response.text
        else:
            self.logger.info('problem with url : {}'.format(url))

    def process_stocks(self):
        soup = BeautifulSoup(self.html, 'html.parser')
        rows = soup.findAll('tr')

        for row in rows:
            processed_row = process_stock_row(row)
            if processed_row:
                stock = processed_row

                if not Stock.objects().filter(ib_symbol=stock['ib_symbol']).first():
                    self.logger.info('adding to db : {}'.format(stock))
                    record = Stock(
                        **stock,
                        exchange=self.exchange_name
                    )
                    try:
                        record.save()
                    except:
                        self.logger.error('stock : {}'.format(stock))

    def get_number_of_web_pages(self):
        soup = BeautifulSoup(self.html, 'html.parser')
        pagination_tag = soup.findAll("ul", {"class": "pagination"})[0]
        li = pagination_tag.findAll("li")
        if len(li) > 2:
            self.number_of_web_pages = int(li[-2].text)

    def load_stocks_from_exchange(self):
        for page_number in range(1, self.number_of_web_pages):
            self.get_url_content(page_number)
            self.process_stocks()


def process_stock_row(row):
    link_tag = row.find('a')
    if link_tag is not None:
        link = link_tag.get('href')
        if link.split(':')[0] != 'javascript':
            return
    else:
        return
    cells = row.findAll('td')
    product_description_link = link.split("'")[1]
    return {'ib_symbol': cells[0].text.strip(),
            'con_id': int(product_description_link.split(sep='=')[-1]),
            'symbol': cells[2].text.strip(),
            'currency': cells[3].text.strip(),
            'product_description_link': product_description_link
            }
