import itertools

from injector import inject

from input_manager.input_manager import InputManager
from scope import Scope
from services.listing_service import ListingService


def get_stocks(mode, items, listing_service):
    if mode == 'exchanges':
        for exchange in items:
            exchange_iter = listing_service.get_stocks_in_exchange(exchange_code=exchange)
            yield from exchange_iter
    if mode == 'stocks':
        for stock in items:
            stock_item = listing_service.get_stock_listing(stock_symbol=stock)
            yield from stock_item


class ListingServiceInput(InputManager):
    @inject
    def __init__(self, listing_service: ListingService, scope: Scope):
        self.listing_service = listing_service

        mode, items = scope.Perimeter
        self.stock_list = get_stocks(mode, items, listing_service)

        self.__finished = False

    def get_next(self):
        stock = next(self.stock_list, None)
        return stock

    @property
    def finished(self):
        return self.__finished
