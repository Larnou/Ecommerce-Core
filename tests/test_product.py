import pytest

from src.product import Product


def test_product_create_valid():
    """Создание продукта с корректными данными"""
    p = Product("Телефон", "Смартфон", 50000.0, 10)

    assert p.name == "Телефон"
    assert p.description == "Смартфон"
    assert p.price == 50000.0
    assert p.quantity == 10


def test_product_create_edge_cases():
    """Пограничные значения цены и количества"""
    # Нулевая цена
    p1 = Product("Бесплатный", "Товар", 0.0, 100)
    assert p1.price == 0.0

    # Очень большая цена
    p2 = Product("Дорогой", "Товар", 10**6, 1)
    assert p2.price == 1000000.0

    # Нулевое количество
    p3 = Product("Нет в наличии", "Товар", 100.0, 0)
    assert p3.quantity == 0


@pytest.mark.parametrize(
    "price,quantity",
    [(-100.0, 10), (100.0, -5), (-50.0, -3)],  # Отрицательная цена  # Отрицательное количество  # Оба отрицательные
)
def test_product_create_invalid_values(price, quantity):
    """Некорректные значения цены и количества"""
    p = Product("Некорректный", "Товар", price, quantity)

    # Проверяем что значения принимаются без валидации
    assert p.price == price
    assert p.quantity == quantity


def test_product_attributes_types():
    """Проверка типов атрибутов"""
    p = Product("Планшет", "10 дюймов", 30000.0, 8)

    assert isinstance(p.name, str)
    assert isinstance(p.description, str)
    assert isinstance(p.price, float)
    assert isinstance(p.quantity, int)


@pytest.mark.parametrize(
    "name,description",
    [
        ("", "Пустое имя"),  # Пустое имя
        ("Телевизор", ""),  # Пустое описание
        (None, "Нет имени"),  # None вместо имени
        ("Наушники", None),  # None вместо описания
    ],
)
def test_product_create_empty_fields(name, description):
    """Пустые значения для имени и описания"""
    p = Product(name, description, 1000.0, 5)

    assert p.name == name
    assert p.description == description
