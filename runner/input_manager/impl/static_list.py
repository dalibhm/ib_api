from input_manager.input_manager import InputManager
import csv


class StaticList(InputManager):
    def __init__(self):
        self.stock_list = []
        with open('./input_manager/impl/ten_stocks.csv', 'r') as f:
            reader = csv.reader(f)
            self.stock_list = list(reader)
        self.__finished = False

    def get_next(self):
        stock = self.stock_list.pop()
        if len(self.stock_list) == 0:
            self.__finished = True
        return stock

    @property
    def finished(self):
        return self.__finished
