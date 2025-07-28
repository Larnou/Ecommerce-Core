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
    _product_quantity = 0

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
        self.__products = products
        Category.category_count += 1
        Category.product_count += sum(product.quantity for product in products)
        Category._product_quantity = len(products)


    def add_product(self, product: Product) -> None:
        """
        Добавляет Product в категорию.

        Args:
            product: Название категории.
        """
        self.__products.append(product)
        Category.product_count += product.quantity

    @property
    def products(self):
        """
        Выводит информацию о продуктах, принадлежащих этой категории в формате "Название, Цена руб. Остаток: Кол-во шт.

        Returns:
            Информация о продуктах в указанном формате.
        """
        info = ""
        for product in self.__products:
            info += f"{product.name}, {product.price} руб. Остаток: {product.quantity} шт.\n"
        return info

    @property
    def product_quantity(self):
        return Category._product_quantity
