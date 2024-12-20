from src.product import Product


class LawnGrass(Product):
    def __init__(self, name, description, price, quantity,               # type: ignore[no-untyped-def]
                 country, germination_period, color):      # type: ignore[no-untyped-def]
        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color

# if __name__ == '__main__':
#     grass1 = LawnGrass("Газонная трава", "Элитная трава для газона", 500.0, 20, "Россия", "7 дней", "Зеленый")
#     grass2 = LawnGrass("Газонная трава 2", "Выносливая трава", 450.0, 15, "США", "5 дней", "Темно-зеленый")
#
#     print(grass1.name)
#     print(grass1.description)
#     print(grass1.price)
#     print(grass1.quantity)
#     print(grass1.country)
#     print(grass1.germination_period)
#     print(grass1.color)
#
#     print(grass2.name)
#     print(grass2.description)
#     print(grass2.price)
#     print(grass2.quantity)
#     print(grass2.country)
#     print(grass2.germination_period)
#     print(grass2.color)
#
#     grass_sum = grass1 + grass2
#     print(grass_sum)
