from abc import ABC, abstractmethod


class BaseProduct(ABC):

    @property
    @abstractmethod
    def price(self) -> float:
        pass

    @price.setter
    @abstractmethod
    def price(self, value: float):
        pass
