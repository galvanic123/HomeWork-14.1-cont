import pytest

from src.class_creator import Product


def test_new_product(products):               # type: ignore[no-untyped-def]
    product4 = Product.new_product(products)
    assert product4.name == "Product4"
    assert product4.description == "Description of the product4"
    assert product4.price == 145.75
    assert product4.quantity == 23


def test_prod_price_property(capsys, first_product):            # type: ignore[no-untyped-def]
    first_product.price = -756.57
    message = capsys.readouterr()
    assert message.out.strip() == "Цена не должна быть нулевая или отрицательная"
    first_product.price = 756.57
    assert first_product.price == 756.57


def test_product(first_product, second_product):             # type: ignore[no-untyped-def]
    assert first_product.name == "Product1"
    assert first_product.description == "Description of the product1"
    assert first_product.price == 84.50
    assert first_product.quantity == 10

    assert second_product.name == "Product2"
    assert second_product.description == "Description of the product2"
    assert second_product.price == 155.87
    assert second_product.quantity == 34


def test_cat_get_product_list_property(first_category, second_category):              # type: ignore[no-untyped-def]
    with pytest.raises(AttributeError):
        print(first_category.__products)
    assert (
            first_category.products
            == "Product1, 84.5 руб. Остаток: 10 шт.\nProduct2, 155.87 руб. Остаток: 34 шт.\n"
    )
    assert (
            second_category.products
            == "Product1, 84.5 руб. Остаток: 10 шт.\nProduct2, 155.87 руб. Остаток: 34 шт.\n"
    )
