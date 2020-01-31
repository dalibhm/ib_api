from abc import ABC, abstractmethod


class InputManager(ABC):
    @abstractmethod
    def get_next(cls):
        """
        gets the next Item in the stock list
        :return: stock
        """
        raise NotImplementedError

    @property
    @abstractmethod
    def finished(cls):
        raise NotImplementedError
