# HomeWork-14.1

Задание 1


Создаём классы Product и Category в модуле: class_creator.py. Для класса Product определяем следующие свойства: название (name),описание (description),цена (price),количество в наличии (quantity). Для класса Category определяем следующие свойства:название (name),описание (description),список товаров категории (products).
Образец:

"""class Category:
    name: str
    description: str
    products: list
    category_count = 0
    product_count = 0"""



"""class Product:
    name: str
    description: str
    price: float
    quantity: int"""

Задание 2

Для этих двух классов добавляем инициализацию, чтобы каждый параметр был передан при создании объекта и сохранен. Также для класса Category добавляем два атрибута класса. 
 


    def __init__(self, name, description,
                 products=None): 
        self.name = name
        self.description = description
        self.products = products if products else []
        Category.product_count += len(products) if products else 0
        Category.category_count += 1

    def __init__(self, name, description, price,
                 quantity):    
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity
Задание 3

В пакете с тестами созданы тесты на проверку модулей class_creator.py, utils.py которые проверяют:

корректность инициализации объектов класса Category , корректность инициализации объектов класса Product , подсчет количества продуктов,

* Дополнительное задание
* Реализовываем приём данных по категориями и товарам из файла JSON. Для этого создадим специальную функцию """def read_json(path: str):  """, которая будет читать файл и создавать объекты классов """def create_objects_from_json(data):  """

### Домашняя работа 15.1
 * В модули product и category добавлены магические методы __str__ и __add__
 * Добавлены тетсты на новые функции
 * Создан вспомогательный класс для периборки товаров одной категории