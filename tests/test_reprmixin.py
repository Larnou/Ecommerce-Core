import sys
from io import StringIO

from src.classes.product import Product
from src.classes.reprmixin import ReprMixin


def capture_output():
    """Захват вывода в стандартный поток"""
    captured_output = StringIO()
    sys.stdout = captured_output
    return captured_output


def restore_output():
    """Восстановление стандартного потока вывода"""
    sys.stdout = sys.__stdout__


def test_repr_mixin_with_mixed_args():
    """Тест со смешанными аргументами"""
    captured = capture_output()

    class TestClass(ReprMixin):
        def __init__(self, name, value, options=None):
            super().__init__(name, value, options=options or {})

    obj = TestClass("test", 100, options={"key": "value"})
    restore_output()

    expected = "TestClass('test', 100, options={'key': 'value'})"
    assert captured.getvalue().strip() == expected


def test_repr_mixin_with_product_class():
    """Тест с реальным классом Product"""
    captured = capture_output()

    p = Product("Ноутбук", "Игровой", 120000, 5)
    restore_output()

    expected = "Product('Ноутбук', 'Игровой', 120000, 5)"
    assert captured.getvalue().strip() == expected
