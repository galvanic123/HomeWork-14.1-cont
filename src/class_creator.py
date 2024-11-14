class Product:
    """Класс Продукт - описание продуктов"""

    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, name, description, price, quantity):             # type: ignore[no-untyped-def]
        """Передаём одноимённые переменные для дальнейшего использования"""
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

    @classmethod
    def new_product(cls, product_data: dict):             # type: ignore[no-untyped-def]
        """Возвращает созданный объект класса Product из параметров товара в словаре"""
        name = product_data["name"]
        description = product_data["description"]
        price = product_data["price"]
        quantity = product_data["quantity"]
        return cls(name, description, price, quantity)

    @property
    def price(self):             # type: ignore[no-untyped-def]
        return self.__price

    @price.setter
    def price(self, value: int):         # type: ignore[no-untyped-def]
        if value <= 0:
            print("Цена не должна быть нулевая или отрицательная")
        else:
            self.__price = value


class Category:
    """Класс Категория Товара - принимает на вход значение и ведёт подсчёт количества
    категорий и уникальных значений"""

    category_count = 0
    product_count = 0
    name: str
    description: str
    products_list: list

    def __init__(self, name, description, products):              # type: ignore[no-untyped-def]
        """Передаём одноимённые переменные для дальнейшего использования"""
        self.name = name
        self.description = description
        self.__products = products if products else []
        Category.category_count += 1
        Category.product_count += len(products) if products else 0

    @property
    def product(self):              # type: ignore[no-untyped-def]
        return self.__products

    def add_product(self, product: Product):                # type: ignore[no-untyped-def]
        self.__products.append(product)
        Category.product_count += 1

    @property
    def products(self):              # type: ignore[no-untyped-def]
        product_list = ""
        for product in self.__products:
            product_list += f"{product.name}, {product.price} руб. Остаток: {product.quantity} шт.\n"
        return "".join(product_list)
