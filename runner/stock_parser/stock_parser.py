import asyncio
import json
import logging
from asyncio import sleep

import aiohttp as aiohttp
import ssl
import requests
from bs4 import BeautifulSoup

from typing import List


class StockParser:
    def __init__(self, exchange_url, exchange_name, data_api_client):
        self.logger = logging.getLogger('stock_parser')
        self.url = exchange_url
        self.data_api_client = data_api_client
        self.first_html = ''
        self.exchange_name = exchange_name
        self.number_of_web_pages = 0

    def get_first_html(self):
        url = '{}&p=&cc=&limit=100&page=1'.format(self.url)
        self.logger.info('sending request for first page in {}'.format(self.exchange_name))
        self.logger.info('url : {}'.format(url))
        response = requests.get(url)
        try:
            response.raise_for_status()
        except requests.exceptions.HTTPError as e:
            self.logger.exception('problem retrieving url : {}'.format(url), e)
        self.first_html = response.text

    def parse_stock_web_pages(self):
        self.get_first_html()
        self.get_number_of_web_pages()

        global loop
        loop = asyncio.get_event_loop()
        res = loop.run_until_complete(self.parse_task())
        print("Done.")

    async def parse_task(self):
        tasks = []
        for page_number in range(1, self.number_of_web_pages):
            tasks.append((page_number, loop.create_task(self.get_html(page_number))))

        for n, t in tasks:
            html = await t
            self.parse_html(html)

    async def get_html(self, page_number: int) -> str:
        url = self.url + '&p=&cc=&limit=100&page=' + str(page_number)
        self.logger.info('sending request for page {}'.format(page_number))
        self.logger.info('url : {}'.format(url))
        ssl_context = ssl.create_default_context(purpose=ssl.Purpose.CLIENT_AUTH)
        async with aiohttp.ClientSession() as session:
            async with session.get(url, ssl=ssl_context) as resp:
                resp.raise_for_status()

                return await resp.text()

    def get_number_of_web_pages(self):
        soup = BeautifulSoup(self.first_html, 'html.parser')
        pagination_tag = soup.findAll("ul", {"class": "pagination"})[0]
        li = pagination_tag.findAll("li")
        if len(li) > 2:
            self.number_of_web_pages = int(li[-2].text)

    def parse_html(self, html: str) -> List[dict]:
        soup = BeautifulSoup(html, 'html.parser')
        rows = soup.findAll('tr')

        for row in rows:
            processed_row = self.process_stock_row(row)
            if processed_row:
                stock = processed_row
                self.data_api_client.post_stock(stock)

    def process_stock_row(self, row):
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
                'exchange': self.exchange_name,
                'product_description_link': product_description_link
                }
