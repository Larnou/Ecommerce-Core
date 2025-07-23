class Product:
    """
    Класс Product, содержит в себе инормацию о названии, описании, цене и количестве товаров.

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
        self.price = price
        self.quantity = quantity