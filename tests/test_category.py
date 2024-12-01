import pytest

from src.category import Category
from src.product import Product


def test_category_str(first_category):             # type: ignore[no-untyped-def]
   assert str(first_category) == "Category1, количество продуктов: 44 шт."


def test_category_add_product():
   product = Product("Товар 3", "Описание товара 3", 200.0, 2)
   category = Category("Категория 2", "Описание категории 2", [])
   category.add_product(product)
   assert len(category.products.split("\n")) -1 == 1


def test_category_all_products_count():
   product1 = Product("Товар 1", "Описание товара 1", 200.0, 2)
   product2 = Product("Товар 2", "Описание товара 2", 2000.0, 20)
   category = Category("Категория 1", "Описание категории 1", [product1, product2])

   assert str(category) == "Категория 1, количество продуктов: 22 шт."



def test_middle_price(category1, category2, category3):           # type: ignore[no-untyped-def]
   assert category1.middle_price() == 140333.33
   assert category2.middle_price() == 195000.0
   assert category3.middle_price() == 210000.0


def test_custom_exception(capsys, category3):
   print(len(category3.product))
   assert len(category3.product) == 1


def test_add_product_invalid():
   category = Category("Телефизоры", "Техника для дома", "Smart TV")
   with pytest.raises(TypeError):
      category.add_product("Одежда")


def test_price():
   product = Product("Samsung Galaxy C23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
   assert product.price == 180000.0
   product.price = -190000.0
   assert product.price == 180000.0


