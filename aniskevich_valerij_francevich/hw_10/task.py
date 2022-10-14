# Необходимо создать два класса:
# 1 Bouquet (букет с цветами)
# 2 Flower (цветок)

# Цветок должен содержать в себе свойства:
# - стоимость
# - цвет
# - длина стебля
# - время жизни

# Букет должен содержать в себе структуру данных, которая будет хранить в себе
# список цветов.
# - В классе букета должны быть реализованы методы для расчета стоимости
# букета, время его увядания по среднему времени жизни всех цветов в букете.
# - Реализовать поиск цветов в букете по различным параметрам.
# - Узнать, есть ли цветок в букете.
class Bouquet:
    name_list = []
    price_list = []
    color_list = []


    def __init__(self, flower):
        self.color_list.append(flower.color)
        self.price_list.append(flower.price)
        self.name_list.append(flower.name)







class Flower:
    def __init__(self, name, price, color, stem_length, lifetime):
        self.name = name
        self.price = int(price)
        self.color = color
        self.stem_lenght = int(stem_length)
        self.lifetime = int(lifetime)


roza1 = Flower("roza", 5, "blue", 70, 14)
roza2 = Flower("roza", 6, "red", 70, 11)
roza3 = Flower("romashka", 7, "orange", 70, 12)
roza4 = Flower("romashka", 8, "black", 70, 15)
bou = Bouquet(roza1)
bou1 = Bouquet(roza2)
bou2 = Bouquet(roza3)
print(bou2.color_list)
print(bou2.price_list)
