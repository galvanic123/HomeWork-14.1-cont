def test_product_str(product1):           # type: ignore[no-untyped-def]
    assert str(product1) == "Xiaomi Redmi Note 11, 31000.0 руб., Остаток: 14 шт. "


def test_add_product(product1, product2):          # type: ignore[no-untyped-def]
    assert product1 + product2 == 1334000
