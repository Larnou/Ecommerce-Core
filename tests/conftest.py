import json

import pytest

from src.classes.category import Category
from src.classes.product import Product


@pytest.fixture(autouse=True)
def reset_counters():
    """Сбрасываем счетчики перед каждым тестом"""
    Category.category_count = 0
    Category.product_count = 0


@pytest.fixture
def sample_products():
    """Фикстура с тестовыми продуктами"""
    return [Product("Product1", "Desc1", 100.0, 3), Product("Product2", "Desc2", 200.0, 5)]


@pytest.fixture
def sample_data():
    """Фикстура с тестовыми данными в формате JSON"""
    return [
        {
            "name": "Смартфоны",
            "description": "Смартфоны",
            "products": [{"name": "Samsung Galaxy", "description": "Флагман", "price": 100000.0, "quantity": 10}],
        }
    ]


@pytest.fixture
def mock_file_structure(tmp_path):
    """Создает временную структуру файлов для тестирования"""
    # Создаем базовую структуру проекта
    base_dir = tmp_path / "project"
    base_dir.mkdir()

    # Создаем директорию data
    data_dir = base_dir / "data"
    data_dir.mkdir()

    # Создаем файл в правильном месте
    valid_file = data_dir / "valid.json"
    valid_file.write_text(
        json.dumps(
            [
                {
                    "name": "Телевизоры",
                    "description": "Телевизоры",
                    "products": [{"name": "LG OLED", "description": "4K", "price": 150000.0, "quantity": 3}],
                }
            ]
        ),
        encoding="utf-8",
    )

    # Создаем пустой файл
    empty_file = data_dir / "empty.json"
    empty_file.write_text("", encoding="utf-8")

    # Создаем файл с битым JSON
    invalid_file = data_dir / "invalid.json"
    invalid_file.write_text("{invalid json}", encoding="utf-8")

    # Возвращаем информацию о созданных файлах
    return {
        "base_dir": base_dir,
        "valid_file": "valid.json",
        "empty_file": "empty.json",
        "invalid_file": "invalid.json",
        "nonexistent_file": "nonexistent.json",
    }
