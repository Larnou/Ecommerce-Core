from typing import Any


class Product:
    """
    Класс Product, содержит в себе информацию о названии, описании, цене и количестве товаров.

    Attributes:
        name: Название продукта.
        description: Описание продукта.
        price: Цена продукта.
        quantity: Количество продуктов.
    """

    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, name, description, price, quantity) -> None:
        """
        Создаёт объект Product.

        Args:
            name: Название продукта.
            description: Описание продукта.
            price: Цена продукта.
            quantity: Количество продуктов.
        """
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

    @classmethod
    def new_product(cls, product_data: dict):
        """
        Добавляет новый продукт.

        Args:
            product_data: Информация о продукте.
        Returns:
            Экзамляр класса Product
        """
        name = product_data["name"]
        description = product_data["description"]
        price = float(product_data["price"])
        quantity = int(product_data["quantity"])

        return cls(name, description, price, quantity)

    @property
    def price(self) -> float:
        """
        Возвращает цену проудкта.

        Returns:
            Цена продукта.
        """
        return self.__price

    @price.setter
    def price(self, price) -> None:
        """
        Задаёт новую цену товара

        Args:
            price: Новая цена.
        """
        if price <= 0:
            print("Цена не должна быть нулевая или отрицательная")
        else:
            self.__price = price

    def __str__(self) -> str:
        """
        Возвращает строковое представление продукта.

        Returns:
            Строковое представление продукта в формате "Название, Цена руб. Остаток кол-во шт."
        """
        return f"{self.name}, {self.__price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other) -> Any:
        if type(self) == type(other):
            return self.__price * self.quantity + other.__price * other.quantity
        else:
            raise TypeError()
