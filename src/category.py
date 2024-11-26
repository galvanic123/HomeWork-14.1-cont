from src.product import Product


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

    def __str__(self):                 # type: ignore[no-untyped-def]
        """Метод, отображающий строку в заданном формате"""
        total_quantity = 0
        for product in self.__products:
            total_quantity += product.quantity
        return f'{self.name}, количество продуктов: {total_quantity} шт.'

    @property
    def product(self):              # type: ignore[no-untyped-def]
        return self.__products

    def add_product(self, product: dict):                # type: ignore[no-untyped-def]
        """Метод добавления нового продукта в список"""
        if isinstance(product, Product):
            self.__products.append(product)
            Category.product_count += 1
        else:
            raise TypeError

    @property
    def products(self):              # type: ignore[no-untyped-def]
        """Отображение продукта в заданном формате"""
        product_list = ""
        for product in self.__products:
            product_list += f"{str(product)}\n"
        return product_list
