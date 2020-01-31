import asyncio
import json
import logging
from asyncio import sleep
from concurrent import futures
from concurrent.futures.thread import ThreadPoolExecutor

import aiohttp as aiohttp
import ssl
import requests
from bs4 import BeautifulSoup

from typing import List, Any, Union

from data.exchange import Exchange
from data.repository import Repository

BASE_URL = 'https://www.interactivebrokers.co.uk/en/'


def get_number_of_pages(html):
    soup = BeautifulSoup(html, 'html.parser')
    try:
        pagination_tag = soup.findAll("ul", {"class": "pagination"})[0]
        li = pagination_tag.findAll("li")
        if len(li) > 2:
            number_of_web_pages = int(li[-2].text)
        else:
            number_of_web_pages = 1
    except IndexError:
        number_of_web_pages = 1
    return number_of_web_pages


class StockParser:
    def __init__(self, exchange: Exchange, repository: Repository):
        self.logger = logging.getLogger('listing')
        self.exchange = exchange
        self.first_html = ''
        self.number_of_web_pages = 0
        self.stocks = []
        self.repository = repository

    def get_stocks(self):
        html_pages = self.get_html_pages()
        for html_page in html_pages:
            stocks = self.parse_html(html_page)
            yield from stocks
        # [self.stocks.extend(self.parse_html(html)) for html in html_list]

    def write_stocks(self):
        [self.repository.add_stock(stock) for stock in self.get_stocks()]

    def get_html_pages(self):
        first_html = self.get_first_html()
        number_of_web_pages = get_number_of_pages(first_html)
        print('[{} pages to parse]'.format(number_of_web_pages))

        with futures.ThreadPoolExecutor(max_workers=10) as executor:
            for html in executor.map(self.get_html, range(1, number_of_web_pages + 1)):
                yield html


    def get_first_html(self):
        url = '{}{}&p=&cc=&limit=100&page=1'.format(BASE_URL, self.exchange.link)
        self.logger.debug('sending request for first page in {}'.format(self.exchange.name))
        self.logger.debug('url : {}'.format(url))
        response = requests.get(url)
        return response.text

    def get_html(self, page_number: int) -> str:
        url = BASE_URL + self.exchange.link + '&p=&cc=&limit=100&page=' + str(page_number)
        self.logger.debug('sending request for page {}'.format(page_number))
        self.logger.debug('url : {}'.format(url))
        try:
            r = requests.get(url)
            result = r.text
        except:
            result = ''
            print('http request failed for : {}'.format(url))
        return result

    def parse_html(self, html: str):
        """
        Parses html and adds stock to database
        if the http request does not succeed, then html = '' and no action is taken
        :param html:
        :return:
        """
        if html == '':
            return
        soup = BeautifulSoup(html, 'html.parser')
        rows = soup.findAll('tr')

        for row in rows:
            processed_row = process_stock_row(row)
            if processed_row:
                processed_row['exchange'] = self.exchange.code
                yield processed_row


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
