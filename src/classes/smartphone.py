from src.classes.product import Product


class Smartphone(Product):
    """
    Класс Smartphone, содержит в себе информацию о названии, описании, цены, количестве товара,
    производительности, модели, объем встроенной памяти и цвет "Смартфона".

    Attributes:
        name: Название продукта.
        description: Описание продукта.
        price: Цена продукта.
        quantity: Количество продуктов.
        efficiency: Производительность.
        model: Модель.
        memory: Объем встроенной памяти.
        color: Цвет.
    """
    def __init__(self, name, description, price, quantity, efficiency, model, memory, color):
        """
        Создаёт объект Product.

        Args:
            name: Название продукта.
            description: Описание продукта.
            price: Цена продукта.
            quantity: Количество продуктов.
            efficiency: Производительность.
            model: Модель.
            memory: Объем встроенной памяти.
            color: Цвет.
        """
        super().__init__(name, description, price, quantity)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color
