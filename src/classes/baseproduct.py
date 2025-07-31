from abc import ABC, abstractmethod


class BaseProduct(ABC):
    """
    Класс BaseProduct, содержит в себе обязательные для реализации методы в классах потомках.
    """

    @property
    @abstractmethod
    def price(self) -> float:
        """
        Возвращает цену проудкта.

        Returns:
            Цена продукта.
        """
        pass

    @price.setter
    @abstractmethod
    def price(self, value: float):
        """
        Задаёт новую цену товара

        Args:
            value: Новая цена.
        """
        pass
