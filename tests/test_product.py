import pytest

from src.product import Product


def test_product_initialization():
    """Проверка корректной инициализации продукта."""
    product = Product("Ноутбук", "Игровой ноутбук", 100000, 5)

    assert product.name == "Ноутбук"
    assert product.description == "Игровой ноутбук"
    assert product.price == 100000  # Проверка через property
    assert product.quantity == 5


def test_product_price_setter_valid():
    """Проверка изменения цены на допустимое значение."""
    product = Product("Телефон", "Смартфон", 50000, 10)
    product.price = 45000  # Установка новой цены

    assert product.price == 45000


def test_product_price_setter_invalid(capsys):
    """Проверка реакции на недопустимую цену (<=0)."""
    product = Product("Планшет", "10 дюймов", 30000, 3)

    # Попытка установить отрицательную цену
    product.price = -1000
    captured = capsys.readouterr()
    assert "Цена не должна быть нулевая или отрицательная" in captured.out
    assert product.price == 30000  # Цена не изменилась

    # Попытка установить нулевую цену
    product.price = 0
    captured = capsys.readouterr()
    assert "Цена не должна быть нулевая или отрицательная" in captured.out
    assert product.price == 30000  # Цена не изменилась


def test_product_new_product_classmethod():
    """Проверка создания продукта через класс-метод."""
    product_data = {"name": "Наушники", "description": "Беспроводные", "price": "7990.99", "quantity": "20"}

    product = Product.new_product(product_data)

    assert product.name == "Наушники"
    assert product.description == "Беспроводные"
    assert product.price == 7990.99  # Проверка преобразования в float
    assert product.quantity == 20  # Проверка преобразования в int


def test_product_new_product_missing_fields():
    """Проверка реакции на отсутствие обязательных полей."""
    with pytest.raises(KeyError):
        Product.new_product({"name": "Неполные данные"})

    with pytest.raises(KeyError):
        Product.new_product({})


def test_product_new_product_invalid_types():
    """Проверка обработки неверных типов данных."""
    product_data = {
        "name": "Клавиатура",
        "description": "Механическая",
        "price": "десять тысяч",  # Не число
        "quantity": "пять",  # Не число
    }

    with pytest.raises(ValueError):
        Product.new_product(product_data)


def test_product_quantity_change():
    """Проверка изменения количества товара."""
    product = Product("Мышь", "Беспроводная", 2500, 15)
    product.quantity = 10

    assert product.quantity == 10


def test_product_negative_quantity(capsys):
    """Проверка установки отрицательного количества."""
    product = Product("Коврик", "Игровой", 1500, 5)
    product.quantity = -3  # Попытка установить отрицательное количество

    # В текущей реализации нет проверки, но добавим для примера
    # В реальном коде следует добавить валидацию
    assert product.quantity == -3

    # Дополнительный тест, если добавить проверку в сеттер:
    # product.quantity = -10
    # captured = capsys.readouterr()
    # assert "Количество не может быть отрицательным" in captured.out


def test_product_price_readonly_access():
    """Проверка, что приватное свойство __price недоступно напрямую."""
    product = Product("Монитор", "27 дюймов", 35000, 7)

    # Проверка, что атрибут __price недоступен по этому имени
    with pytest.raises(AttributeError):
        price = product.__price
        print(price)

    # Но доступен по искаженному имени (name mangling)
    assert product._Product__price == 35000


def test_product_string_representation():
    """Проверка строкового представления продукта."""
    product = Product("SSD", "1TB NVMe", 8000, 25)
    representation = str(product)

    # Если не реализован __str__, используем дефолтное представление
    # Для полноты можно добавить метод __str__ в класс
    assert "object at" in representation  # Дефолтное представление

    # Альтернатива: реализовать __str__ и проверять:
    # assert str(product) == "SSD, 8000 руб. Остаток: 25 шт."
