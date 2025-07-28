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
    def products(self) -> str:
        """
        Выводит информацию о продуктах, принадлежащих этой категории в формате "Название, Цена руб. Остаток: Кол-во шт.

        Returns:
            Информация о продуктах в указанном формате.
        """
        info = ""
        for product in self.__products:
            info += f"{product.name}, {product.price} руб. Остаток: {product.quantity} шт.\n"
        return info

    def __str__(self) -> str:
        """
        Возвращает строковое представление категории.

        Returns:
            Строковое представление продукта в формате "Название,
            количество продуктов: общее кол-во продуктов в категории."
        """
        return f"{self.name}, количество продуктов: {Category.product_count} шт."

    @property
    def product_quantity(self) -> int:
        return Category._product_quantity
