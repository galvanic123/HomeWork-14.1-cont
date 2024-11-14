from src.class_creator import Category


def test_init_category(category):          # type: ignore[no-untyped-def]
    assert category.name == "Смартфоны"
    assert (
        category.description
        == """Смартфоны, как средство не только коммуникации,
           но и получение дополнительных функций для удобства жизни""",
    )


def test_init_product(product):            # type: ignore[no-untyped-def]
    assert product.name == "Samsung Galaxy C23 Ultra"
    assert product.description == "256GB, Серый цвет, 200MP камера"
    assert product.price == 180000.0
    assert product.quantity == 5


def test_category_count(category):            # type: ignore[no-untyped-def]
    assert Category.category_count == 2
    assert Category.product_count == 6
