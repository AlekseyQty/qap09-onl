# Необходимо создать два класса:
# 1.	Bouquet (букет с цветами)
# 2.	Flower (цветок)
# Цветок должен содержать в себе свойства:
# -	стоимость
# -	цвет
# -	длина стебля
# -	время жизни
# Букет должен содержать в себе структуру данных, которая будет хранить в себе список цветов.
# -	В классе букета должны быть реализованы методы для расчета стоимости букета, время его увядания по среднему времени жизни всех цветов в букете.
# -	Реализовать поиск цветов в букете по различным параметрам.
# -	Узнать, есть ли цветок в букете.
#
# Создать несколько разных экземпляров цветов и несколько букетов, содержащих в себе разные цветы.

class Flower:
    def __init__(self, name, price, color, length, livetime):
        self.name = name
        self.price = price
        self.color = color
        self.length = length
        self.livetime = livetime


class Bouquet:
    def __init__(self, flowers):
        self.flowers = flowers

    def name_flower(self, name_flower):
        result = []
        for flower in self.flowers:
            if name_flower == flower.name:
                result.append(True)
            else:
                result.append(False)
        if True in result:
            return f'{name_flower} in'
        else:
            return f'{name_flower} not in'

    def overall_price(self):
        ov_price = 0
        for flower in self.flowers:
            ov_price += flower.price
        return f'Overall price = {ov_price} BYN'

    def average_lifetime(self):
        av_lifetime = 0
        for flower in self.flowers:
            av_lifetime += flower.livetime
        return f'Average lifetime = {int(av_lifetime / len(self.flowers))} hours'

    def search_flower(self, flower_prop, prop_val):
        result = []
        if flower_prop == 'price':
            for flower in self.flowers:
                if prop_val == flower.price:
                    result.append(flower.name)

        elif flower_prop == 'color':
            for flower in self.flowers:
                if prop_val == flower.color:
                    result.append(flower.name)

        elif flower_prop == 'length':
            for flower in self.flowers:
                if prop_val == flower.length:
                    result.append(flower.name)

        elif flower_prop == 'livetime':
            for flower in self.flowers:
                if prop_val == flower.livetime:
                    result.append(flower.name)

        return ' and '.join(result)


flower_1 = Flower('rose', 3, 'red', 0.5, 168)
flower_2 = Flower('lilie', 5, 'white', 0.2, 240)
flower_3 = Flower('tulips', 2, 'yellow', 0.3, 72)
flower_4 = Flower('chrysanthemum', 4, 'red', 0.6, 120)
flower_5 = Flower('gerbera', 8, 'pink', 0.7, 336)

list_1 = [flower_1, flower_2, flower_3]
list_2 = [flower_4, flower_5, flower_1]
list_3 = [flower_2, flower_3, flower_4]

Bouquet_1 = Bouquet(list_1)
Bouquet_2 = Bouquet(list_2)
Bouquet_3 = Bouquet(list_3)

print(f'Bouquet 1: {Bouquet.overall_price(Bouquet_1)}')
print(f'Bouquet 2: {Bouquet.overall_price(Bouquet_2)}')
print(f'Bouquet 3: {Bouquet.overall_price(Bouquet_3)}')

print(f'Bouquet 1: {Bouquet.average_lifetime(Bouquet_1)}')
print(f'Bouquet 2: {Bouquet.average_lifetime(Bouquet_2)}')
print(f'Bouquet 3: {Bouquet.average_lifetime(Bouquet_3)}')

print(f"{Bouquet.name_flower(Bouquet_1, 'rose')} Bouquet 1")
print(f"{Bouquet.name_flower(Bouquet_1, 'lilie')} Bouquet 1")
print(f"{Bouquet.name_flower(Bouquet_1, 'tulips')} Bouquet 1")
print(f"{Bouquet.name_flower(Bouquet_1, 'chrysanthemum')} Bouquet 1")
print(f"{Bouquet.name_flower(Bouquet_1, 'gerbera')} Bouquet 1")
print(f"{Bouquet.name_flower(Bouquet_2, 'chrysanthemum')} Bouquet 2")
print(f"{Bouquet.name_flower(Bouquet_3, 'lilie')} Bouquet 3")

print(f"This is {Bouquet.search_flower(Bouquet_1, 'price', 2)}")
print(f"There are {Bouquet.search_flower(Bouquet_2, 'color', 'red')}")
print(f"This is {Bouquet.search_flower(Bouquet_3, 'length', 0.2)}")
