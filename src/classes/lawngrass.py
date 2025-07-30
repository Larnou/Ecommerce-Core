from src.classes.product import Product


class LawnGrass(Product):
    """
    Класс LawnGrass, содержит в себе информацию о названии, описании, цене, количестве товара,
    стране-производителе, срок прорастания и цвет "Травы газонной"

    Attributes:
        name: Название продукта.
        description: Описание продукта.
        price: Цена продукта.
        quantity: Количество продуктов.
        country: Страна производитель.
        germination_period: Срок прорастания.
        color: Цвет.
    """
    def __init__(self, name, description, price, quantity, country, germination_period, color):
        """
        Создаёт объект Product.

        Args:
            name: Название продукта.
            description: Описание продукта.
            price: Цена продукта.
            quantity: Количество продуктов.
            country: Страна производитель.
            germination_period: Срок прорастания.
            color: Цвет.
        """
        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color
