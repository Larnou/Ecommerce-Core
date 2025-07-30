import pytest

from src.classes.category import Category
from src.classes.product import Product


def test_category_create_valid(sample_products):
    """Создание категории с корректными данными"""
    cat = Category("Electronics", "Gadgets", sample_products)

    assert cat.name == "Electronics"
    assert cat.description == "Gadgets"
    assert cat.product_quantity == 2
    assert Category.category_count == 1
    assert Category.product_count == 8


def test_category_create_empty_products():
    """Создание категории без продуктов"""
    cat = Category("Books", "All books", [])

    assert cat.name == "Books"
    assert cat.description == "All books"
    assert cat.products == ""
    assert Category.category_count == 1
    assert Category.product_count == 0


def test_category_create_single_product():
    """Создание категории с одним продуктом"""
    p = Product("Book", "Novel", 500.0, 10)
    cat = Category("Literature", "Books category", [p])

    assert cat.name == "Literature"
    assert Category.category_count == 1
    assert Category.product_count == 10


def test_category_multiple_categories_counters(sample_products):
    """Счетчики при создании нескольких категорий"""
    cat1 = Category("Cat1", "Desc1", sample_products)
    cat2 = Category("Cat2", "Desc2", [Product("P3", "Desc3", 50.0, 2), Product("P4", "Desc4", 75.0, 4)])

    assert cat1.name == "Cat1"
    assert cat2.name == "Cat2"
    assert Category.category_count == 2
    assert Category.product_count == 14  # 8 (from cat1) + 6 (from cat2)


def test_category_attributes_types():
    """Проверка типов атрибутов"""
    cat = Category("Test", "Test", [Product("P1", "D1", 100.0, 1)])

    assert isinstance(cat.name, str)
    assert isinstance(cat.description, str)


@pytest.mark.parametrize(
    "name,description",
    [
        ("", "Пустое имя"),  # Пустое имя
        ("Телевизоры", ""),  # Пустое описание
        (None, "Нет имени"),  # None вместо имени
        ("Наушники", None),  # None вместо описания
    ],
)
def test_category_create_empty_fields(name, description, sample_products):
    """Пустые значения для имени и описания категории"""
    cat = Category(name, description, sample_products)

    assert cat.name == name
    assert cat.description == description
    assert Category.category_count == 1
    assert Category.product_count == 8


def test_category_product_quantity_zero():
    """Продукты с нулевым количеством"""
    products = [Product("P1", "Desc1", 100.0, 0), Product("P2", "Desc2", 200.0, 0)]
    cat = Category("Zero", "Zero products", products)

    assert cat.product_quantity == 2
    assert Category.product_count == 0  # 0 + 0


def test_category_product_quantity_negative():
    """Продукты с отрицательным количеством"""
    products = [Product("P1", "Desc1", 100.0, -5), Product("P2", "Desc2", 200.0, -3)]
    cat = Category("Negative", "Negative quantity", products)

    assert cat.product_quantity == 2
    assert Category.product_count == -8  # (-5) + (-3)


def test_category_large_number_of_products():
    """Большое количество продуктов"""
    products = [Product(f"Product{i}", f"Desc{i}", 10.0, 100) for i in range(100)]
    cat = Category("Large", "100 products", products)

    assert cat.product_quantity == 100
    assert Category.product_count == 10000  # 100 * 100


def test_category_shared_counters_multiple_instances(sample_products):
    """Общие счетчики для всех экземпляров"""
    cat1 = Category("Cat1", "Desc1", sample_products)
    cat2 = Category("Cat2", "Desc2", [Product("P3", "Desc3", 50.0, 2)])

    assert cat1.name == "Cat1"
    assert cat2.name == "Cat2"
    assert Category.category_count == 2
    assert Category.product_count == 10  # 8 + 2

    cat3 = Category("Cat3", "Desc3", [])
    assert cat3.name == "Cat3"
    assert Category.category_count == 3
    assert Category.product_count == 10


def test_category_string_representation(sample_products):
    """Проверка строкового представления категории."""
    cat1 = Category("Cat1", "Desc1", sample_products)

    assert str(cat1) == "Cat1, количество продуктов: 8 шт."


def test_category_add_valid_product():
    """Проверка добавления корректного продукта."""
    # Подготовка
    category = Category("Категория", "Описание", [])
    product = Product("Товар", "Описание", 100, 5)

    # Действие
    category.add_product(product)

    # Проверки
    assert len(category._Category__products) == 1
    assert product in category._Category__products
    assert Category.product_count == 5


def test_category_add_multiple_products():
    """Проверка добавления нескольких продуктов."""
    category = Category("Категория", "Описание", [])
    products = [Product("Товар 1", "Описание", 100, 3), Product("Товар 2", "Описание", 200, 7)]

    for p in products:
        category.add_product(p)

    assert len(category._Category__products) == 2
    assert all(p in category._Category__products for p in products)
    assert Category.product_count == 10
