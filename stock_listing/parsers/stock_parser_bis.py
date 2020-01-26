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


def get_number_of_pages(html):
    soup = BeautifulSoup(html, 'html.parser')
    try:
        pagination_tag = soup.findAll("ul", {"class": "pagination"})[0]
        li = pagination_tag.findAll("li")
        if len(li) > 2:
            number_of_web_pages = int(li[-2].text)
    except IndexError:
        number_of_web_pages = 1
    return number_of_web_pages


class StockParser:
    def __init__(self, exchange: Exchange):
        self.logger = logging.getLogger('listing')
        self.exchange = exchange
        self.first_html = ''
        self.number_of_web_pages = 0

    def parse_stock_web_pages(self):
        first_html = self.get_first_html()
        number_of_web_pages = get_number_of_pages(first_html)
        print('[{} pages to parse]'.format(self.number_of_web_pages))

        executor: Union[ThreadPoolExecutor, Any]
        with futures.ThreadPoolExecutor(max_workers=20) as executor:
            executor.map(self.parse_html, [1: number_of_web_pages])
        print("Done.")

    def get_first_html(self):
        url = '{}&p=&cc=&limit=100&page=1'.format(self.exchange.link)
        self.logger.debug('sending request for first page in {}'.format(self.exchange.name))
        self.logger.debug('url : {}'.format(url))
        response = requests.get(url)
        try:
            response.raise_for_status()
        except requests.exceptions.HTTPError as e:
            self.logger.exception('problem retrieving url : {}'.format(url), e)
        return response.text

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

        result = []
        for row in rows:
            processed_row = process_stock_row(row)
            if processed_row:
                processed_row['exchange'] = self.exchange.name
                result.append(processed_row)


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
