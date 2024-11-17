import pytest

from src.category import Category
from src.class_creator import Product, Category    # noqa: F811
from src.iteration_class import ProductIteration


@pytest.fixture
def first_product():            # type: ignore[no-untyped-def]
    return Product(
        name="Product1",
        description="Description of the product1",
        price=84.50,
        quantity=10,
    )


@pytest.fixture
def second_product():                   # type: ignore[no-untyped-def]
    return Product(
        name="Product2",
        description="Description of the product2",
        price=155.87,
        quantity=34,
    )


@pytest.fixture
def first_category(first_product, second_product):             # type: ignore[no-untyped-def]
    return Category(
        name="Category1",
        description="Description of the category1",
        products=[first_product, second_product],)


@pytest.fixture
def second_category(first_product, second_product):             # type: ignore[no-untyped-def]
    return Category(
        name="Category2",
        description="Description of the category2",
        products=[first_product, second_product],)


@pytest.fixture
def products():           # type: ignore[no-untyped-def]
    return {
        "name": "Product4",
        "description": "Description of the product4",
        "price": 145.75,
        "quantity": 23,
    }


@pytest.fixture
def category():          # type: ignore[no-untyped-def]
    return Category(
        "Смартфоны",
        """Смартфоны, как средство не только коммуникации,
           но и получение дополнительных функций для удобства жизни""",
        [
            {
                "name": "Samsung Galaxy C23 Ultra",
                "description": "256GB, Серый цвет, 200MP камера",
                "price": 180000.0,
                "quantity": 5,
            },
            {"name": "Iphone 15", "description": "512GB, Gray space",
             "price": 210000.0, "quantity": 8},
            {"name": "Xiaomi Redmi Note 11", "description": "1024GB, Синий",
             "price": 31000.0, "quantity": 14},
        ],
    )


@pytest.fixture
def product():       # type: ignore[no-untyped-def]
    return Product("Samsung Galaxy C23 Ultra",
                   "256GB, Серый цвет, 200MP камера", 180000.0, 5)


@pytest.fixture
def test_init_product(product):            # type: ignore[no-untyped-def]
    assert product.name == "Samsung Galaxy C23 Ultra"
    assert product.description == "256GB, Серый цвет, 200MP камера"
    assert product.price == 180000.0
    assert product.quantity == 5


@pytest.fixture
def test_category_count(category):            # type: ignore[no-untyped-def]
    assert Category.category_count == 2
    assert Category.product_count == 3


@pytest.fixture
def product1():            # type: ignore[no-untyped-def]
    return Product("Xiaomi Redmi Note 11", "25GB, Серый цвет 200Mp камера", 31000.0, 14)


@pytest.fixture
def product2():              # type: ignore[no-untyped-def]
    return Product("Samsung Galaxy S23 Ultra", "1024GB, Синий", 180000.0, 5)


@pytest.fixture
def product_iterator(first_category):           # type: ignore[no-untyped-def]
    return ProductIteration(first_category)
