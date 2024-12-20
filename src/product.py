from src.base_product import BaseProduct
from src.print_mixin import PrintMixin


class Product(PrintMixin, BaseProduct):
    """Класс Продукт - описание продуктов"""

    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, name, description, price, quantity):              # type: ignore[no-untyped-def]
        """Передаём одноимённые переменные для дальнейшего использования"""

        self.name = name
        self.description = description
        self.__price = price
        if quantity == 0:
            raise ValueError("Товар с нулевым количеством не может быть добавлен")
        else:
            self.quantity = quantity
        super().__init__()

    def __str__(self):                       # type: ignore[no-untyped-def]
        return f'{self.name}, {self.__price} руб., Остаток: {self.quantity} шт. '

    def __add__(self, other):              # type: ignore[no-untyped-def]
        # if type(self) == type(other):
        #     return self.__price * self.quantity + other.__price * other.quantity
        if isinstance(other, self.__class__):
            return self.__price * self.quantity + other.__price * other.quantity
        else:
            raise TypeError

    @classmethod
    def new_product(cls, product_data: dict):             # type: ignore[no-untyped-def]
        """Возвращает созданный объект класса Product из параметров товара в словаре"""

        return cls(**product_data)

    @property
    def price(self):             # type: ignore[no-untyped-def]
        """Метод, возвращающий цену продукта"""
        return self.__price

    @price.setter
    def price(self, value: int):         # type: ignore[no-untyped-def]
        """Метод, меняющий цену продукта в зависимости от условия"""
        if value <= 0:
            print("Цена не должна быть нулевая или отрицательная")
        elif value > self.__price:
            self.price = value
        else:
            while True:
                answer = input('Введите ответ на понижение цены: y/n')
                if answer.lower() == 'y':
                    self.price = value
                    break
                elif answer.lower() == 'n':
                    break
