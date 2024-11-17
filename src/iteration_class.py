from src.product import Product
from src.category import Category

""" Новый вспомогательный класс, с помощью которого можно перебирать товары одной категории, 
например в цикле for. Для этого новый класс должен принимать на вход объект класса категории 
и производить итерацию по товарам, которые хранятся в данной категории."""

class ProductIteration:
    def __init__(self, category):
        self.category = category
        self.index = 0

    def __iter__(self):
        self.index = -1
        return self

    def __next__(self):
        if self.index + 1 < len(self.category.products_list[self.index]):
            self.index += 1
        else:
            raise StopIteration
