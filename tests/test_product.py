import pytest

from src.product import Product


def test_product_str(product1):           # type: ignore[no-untyped-def]
    assert str(product1) == "Xiaomi Redmi Note 11, 31000.0 руб., Остаток: 14 шт. "


def test_add_product(product1, product2):          # type: ignore[no-untyped-def]
    assert product1 + product2 == 1334000


def test_add_zero_product() -> None:
    with pytest.raises(ValueError) as ex:
        quantity_zero = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 0)
        assert quantity_zero == f"{ex}: Товар с нулевым количеством не может быть добавлен"
