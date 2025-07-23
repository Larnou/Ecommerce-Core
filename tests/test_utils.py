import json
from unittest.mock import mock_open, patch

from src.category import Category
from src.product import Product
from src.utils import load_categories_from_json


def test_successful_loading(sample_data):
    """Успешная загрузка данных из файла"""
    # Мокаем открытие файла и чтение JSON
    with patch("builtins.open", mock_open(read_data=json.dumps(sample_data))):
        categories = load_categories_from_json("test.json")

    assert len(categories) == 1
    category = categories[0]
    assert isinstance(category, Category)
    assert category.name == "Смартфоны"
    assert len(category.products) == 1
    product = category.products[0]
    assert isinstance(product, Product)
    assert product.name == "Samsung Galaxy"
    assert product.price == 100000.0


def test_nonexistent_file():
    """Обработка несуществующего файла"""
    categories = load_categories_from_json("nonexistent.json")
    assert categories == []


def test_invalid_json():
    """Обработка файла с невалидным JSON"""
    # Создаем мок для файла с невалидным содержимым
    with patch("builtins.open", mock_open(read_data="{invalid json}")):
        categories = load_categories_from_json("invalid.json")
    assert categories == []


def test_empty_file():
    """Обработка пустого файла"""
    with patch("builtins.open", mock_open(read_data="")):
        categories = load_categories_from_json("empty.json")
    assert categories == []


def test_permission_error():
    """Обработка ошибки прав доступа"""
    # Мокаем открытие файла с вызовом PermissionError
    mock_file = mock_open()
    mock_file.side_effect = PermissionError("No permission")

    with patch("builtins.open", mock_file):
        categories = load_categories_from_json("restricted.json")

    assert categories == []


def test_directory_path():
    """Передача пути к директории вместо файла"""
    # Мокаем открытие файла с вызовом IsADirectoryError
    mock_file = mock_open()
    mock_file.side_effect = IsADirectoryError("Is a directory")

    with patch("builtins.open", mock_file):
        categories = load_categories_from_json("/path/to/directory")

    assert categories == []


# def test_real_file_loading(mock_file_structure):
#     """Интеграционный тест с реальной файловой структурой"""
#     # Мокаем __file__ для подмены базового пути
#     with patch("utils.__file__", str(mock_file_structure["base_dir"] / "module.py")):
#         # Тест с валидным файлом
#         categories = load_categories_from_json(mock_file_structure["valid_file"])
#         assert len(categories) == 1
#         assert categories[0].name == "Телевизоры"
#         assert categories[0].products[0].name == "LG OLED"
#
#         # Тест с несуществующим файлом
#         categories = load_categories_from_json(mock_file_structure["nonexistent_file"])
#         assert categories == []
#
#         # Тест с пустым файлом
#         categories = load_categories_from_json(mock_file_structure["empty_file"])
#         assert categories == []
#
#         # Тест с невалидным JSON
#         categories = load_categories_from_json(mock_file_structure["invalid_file"])
#         assert categories == []


def test_complex_data_structure():
    """Тестирование со сложной структурой данных"""
    complex_data = [
        {
            "name": "Категория 1",
            "description": "Описание 1",
            "products": [
                {"name": "Товар 1", "description": "Описание товара 1", "price": 100.0, "quantity": 5},
                {"name": "Товар 2", "description": "Описание товара 2", "price": 200.0, "quantity": 3},
            ],
        },
        {
            "name": "Категория 2",
            "description": "Описание 2",
            "products": [{"name": "Товар 3", "description": "Описание товара 3", "price": 300.0, "quantity": 7}],
        },
    ]

    with patch("builtins.open", mock_open(read_data=json.dumps(complex_data))):
        categories = load_categories_from_json("complex.json")

    assert len(categories) == 2
    assert categories[0].name == "Категория 1"
    assert len(categories[0].products) == 2
    assert categories[1].name == "Категория 2"
    assert categories[1].products[0].price == 300.0
    assert sum(p.quantity for p in categories[0].products) == 8
