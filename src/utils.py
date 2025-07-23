import json
import os

from src.category import Category
from src.product import Product


def load_categories_from_json(filename: str) -> list[Category]:
    """
    Загружает данные из JSON и преобразует их в список объектов Category с вложенными Product

    Args:
        filename: Путь до загружаемого файла

    Returns:
        Список объектов Category
    """

    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    DATA_PATH = os.path.join(BASE_DIR, "data", filename)

    try:
        # Пробуем интерпретировать json_data как путь к файлу
        with open(DATA_PATH, 'r', encoding='utf-8') as file:
            data = json.load(file)

            categories = []
            for category_data in data:
                products = []
                for product_data in category_data["products"]:
                    product = Product(
                        name=product_data["name"],
                        description=product_data["description"],
                        price=product_data["price"],
                        quantity=product_data["quantity"]
                    )
                    products.append(product)

                category = Category(
                    name=category_data["name"],
                    description=category_data["description"],
                    products=products
                )
                categories.append(category)

            return categories

    except (FileNotFoundError, json.JSONDecodeError, UnicodeDecodeError, PermissionError, IsADirectoryError):
        return []
