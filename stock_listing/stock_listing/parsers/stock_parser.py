import asyncio
import logging

import aiohttp as aiohttp
import ssl
import requests
from bs4 import BeautifulSoup

from typing import List


class StockParser:
    def __init__(self, exchange_url, exchange_code, repository):
        self.logger = logging.getLogger('listing')
        self.url = exchange_url
        self.first_html = ''
        self.exchange_name = exchange_code
        self.number_of_web_pages = 0
        self.repository = repository

    def get_first_html(self):
        url = '{}&p=&cc=&limit=100&page=1'.format(self.url)
        self.logger.debug('sending request for first page in {}'.format(self.exchange_name))
        self.logger.debug('url : {}'.format(url))
        response = requests.get(url)
        try:
            response.raise_for_status()
        except requests.exceptions.HTTPError as e:
            self.logger.exception('problem retrieving url : {}'.format(url), e)
        self.first_html = response.text

    def parse_stock_web_pages(self):
        self.get_first_html()
        self.get_number_of_web_pages()
        print('[{} pages to parse]'.format(self.number_of_web_pages))

        global loop
        loop = asyncio.get_event_loop()
        res = loop.run_until_complete(self.parse_task())
        print("Done.")

    async def parse_task(self):
        tasks = []
        for page_number in range(1, self.number_of_web_pages + 1):
            tasks.append((page_number, loop.create_task(self.get_html(page_number))))

        for n, t in tasks:
            try:
                html = await t
                self.parse_html(html)
            except Exception as e:
                print('[ page {} failed due to {} ]'.format(n, e))
            finally:
                print('[ page {} : from finally as exception could not be written ]'.format(n))

    async def get_html(self, page_number: int) -> str:
        url = self.url + '&p=&cc=&limit=100&page=' + str(page_number)
        self.logger.debug('sending request for page {}'.format(page_number))
        self.logger.debug('url : {}'.format(url))
        ssl_context = ssl.create_default_context(purpose=ssl.Purpose.CLIENT_AUTH)
        async with aiohttp.ClientSession() as session:
            async with session.get(url, ssl=ssl_context) as resp:
                # resp.raise_for_status()
                try:
                    result = resp.text()
                except:
                    result = ''
                    print('http request failed for : {}'.format(url))
                return await resp.text()

    def get_number_of_web_pages(self):
        soup = BeautifulSoup(self.first_html, 'html.parser')
        try:
            pagination_tag = soup.findAll("ul", {"class": "pagination"})[0]
            li = pagination_tag.findAll("li")
            if len(li) > 2:
                self.number_of_web_pages = int(li[-2].text)
        except IndexError:
            self.number_of_web_pages = 1

    def parse_html(self, html: str) -> List[dict]:
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
            processed_row = self.process_stock_row(row)
            if processed_row:
                stock = processed_row
                stock_db = self.repository.get_stock_by_id_and_exchange(stock['con_id'], stock['exchange'])
                if not stock_db:
                    self.repository.add_stock(stock)

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
