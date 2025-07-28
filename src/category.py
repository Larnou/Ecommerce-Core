from src.product import Product


class Category:
    """
    Класс Category, содержит в себе инормацию о названии, описании и товаров относящихся к этой категории.
    Каждый продукт из категории является обьектом класса Product.

    Attributes:
        name: Название категории.
        description: Описание категории.
        products: Продукты, которые относятся к этой категории.
        category_count: Количество категорий.
        product_count: Общее количество продуктов в категории.
    """

    name: str
    description: str
    products: list[Product]

    category_count = 0
    product_count = 0

    def __init__(self, name, description, products) -> None:
        """
        Создаёт объект Category.

        Args:
            name: Название категории.
            description: Описание категории.
            products: Продукты, которые относятся к этой категории.
        """
        self.name = name
        self.description = description
        self.products = products
        Category.category_count += 1
        Category.product_count += sum(product.quantity for product in products)

    def __repr__(self) -> str:
        """Возвращает строковое представление объекта."""
        return f"Category({self.name}, {len(self.products)} products)"
