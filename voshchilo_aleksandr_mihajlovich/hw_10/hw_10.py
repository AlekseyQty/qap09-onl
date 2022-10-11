from collections import Counter
import random

# 1. Цветочница.


class Bouquet:


    @staticmethod
    def rand_bouquet(numb_flowers_min, numb_flowers_max, flowers_list, find_flower):
        """
        Создаю букет из случайных цветов, вывожу состав букета, стоимость, время увядания и поиск цветка в букете
        """
        numb_flowers = random.randint(numb_flowers_min, numb_flowers_max)
        bouquet = [i for i in range(numb_flowers)]
        for i in bouquet:
            bouquet[i] = random.choice(flowers_list)
        bouquet_bouquet = []
        name_bouquet = []
        time_wither = 0
        cost = 0
        count_flower = 0
        for i in bouquet:
            bouquet_bouquet.append(i)
            cost += i.price
            time_wither += i.wither_time
            name_bouquet.append(i.name)
        for i in bouquet:
            if i.name == find_flower:
                count_flower += 1

        all_time_wither = time_wither / len(bouquet_bouquet)
        new_bouquet = dict(Counter(name_bouquet))
        compound_bouquet = "; ".join([f"{key}:{value}" for key, value in new_bouquet.items()])
        print(f"Composition of the bouquet: {compound_bouquet}")
        print(f"Cost of the bouquet: {cost} rub.")
        print(f"Bouquet withering time: {all_time_wither} h.")
        print(f"In this bouquet find {count_flower} {find_flower}")



    @staticmethod
    def create_bouquet(*args):
        """
        Создаю букет из выбранных цветов, вывожу состав букета, стоимость и время увядания
        """
        bouquet = []
        name_bouquet = []
        time_wither = 0
        cost = 0
        for i in args:
            bouquet.append(i)
            cost += i.price
            time_wither += i.wither_time
            name_bouquet.append(i.name)

        all_time_wither = time_wither/len(bouquet)
        new_bouquet = dict(Counter(name_bouquet))
        compound_bouquet = "; ".join([f"{key}:{value}" for key, value in new_bouquet.items()])
        print(f"Composition of the bouquet: {compound_bouquet}")
        print(f"Cost of the bouquet: {cost} rub.")
        print(f"Bouquet withering time: {all_time_wither} h.")

    @staticmethod
    def sort_color(*args):
        """
        Поиск цветов в букете по цвету (не стал делать все варианты поиска, они все одинаково реализуется у меня. Может
        нужна другая логика?)
        """
        bouquet = []
        for i in args:
            bouquet.append(i)

        bouquet.sort(key=lambda y: y.color)
        bouquet_color_sort = []
        for i in bouquet:
            bouquet_color_sort.append(i.name)

        bouquet_color_sort_set = ", ".join([i for i in bouquet_color_sort])
        print(f"Sort by color: {bouquet_color_sort_set}")

    @staticmethod
    def sort_price(*args):
        """
        Поиск цветов в букете по стоимости
        """
        bouquet = []
        for i in args:
            bouquet.append(i)

        bouquet.sort(key=lambda y: y.price)
        bouquet_price_sort = []
        for i in bouquet:
            bouquet_price_sort.append(i.name)

        bouquet_price_sort_set = ", ".join([i for i in bouquet_price_sort])
        print(f"Sort by price: {bouquet_price_sort_set}")

    @staticmethod
    def find_flower_by_param(length, price, *args):
        """
        Поиск цветов в букете по заданным параметрам.
        """
        bouquet = []
        for i in args:
            bouquet.append(i)

        find_in_bouquet = [i for i in bouquet if i.stem_length > length and i.price < price]
        find_in_bouquet_flower = []
        for i in find_in_bouquet:
            find_in_bouquet_flower.append(i.name)
        search_flowers = ", ".join([i for i in find_in_bouquet_flower])
        print(f"Search flowers: {search_flowers}")


class Flower:

    list_flowers = []

    def __init__(self, name, freshness, color, stem_length, price, wither_time):
        self.name = name
        self.freshness = freshness
        self.color = color
        self.stem_length = stem_length
        self.price = price
        self.wither_time = wither_time
        Flower.list_flowers.append(self)


chrysanthemum = Flower("Chrysanthemum", True, "blue", 25, 3, 48)
chamomile = Flower("Chamomile", False, "white", 20, 2, 36)
peony = Flower("Peony", True, "green", 30, 4, 60)
rose = Flower("Rose", False, "red", 30, 5, 36)

jim_bouquet = Bouquet()
jim_bouquet.create_bouquet(chamomile, peony, rose, rose, chrysanthemum, chrysanthemum)
jim_bouquet.sort_color(chamomile, peony, rose, rose, chrysanthemum, chrysanthemum)
jim_bouquet.sort_price(chamomile, peony, rose, rose, chrysanthemum, chrysanthemum)
jim_bouquet.find_flower_by_param(25, 5, chamomile, peony, rose, rose, chrysanthemum, chrysanthemum)

billy_bouquet = Bouquet()
billy_bouquet.rand_bouquet(5, 20, Flower.list_flowers, "Rose")





