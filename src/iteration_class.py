""" Новый вспомогательный класс, с помощью которого можно перебирать товары одной категории,
    например в цикле for. Для этого новый класс должен принимать на вход объект класса категории
    и производить итерацию по товарам, которые хранятся в данной категории."""


class ProductIteration:
    def __init__(self, category):                # type: ignore[no-untyped-def]
        self.category = category
        self.index = 0

    def __iter__(self):         # type: ignore[no-untyped-def]
        self.index = 0
        return self

    def __next__(self):              # type: ignore[no-untyped-def]
        if self.index < len(self.category.products[self.index]):
            self.index += 1
        else:
            raise StopIteration
