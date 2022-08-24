# Определить иерархию и создать несколько цветов. Собрать букет (можно использовать аксессуары) с определением его
# стоимости. Определить время его увядания по среднему времени жизни всех цветов в букете.
# Позволить сортировку цветов в букете на основе различных параметров (свежесть/цвет/длина стебля/стоимость...)
# Реализовать поиск цветов в букете по определенным параметрам.
# Узнать, есть ли цветок в букете.

from operator import itemgetter
import random


class Flowers:
    dict_flowers = {}

    def __init__(self, dict_flowers, flower_amount):
        self.dict_flowers = dict_flowers
        self.flower_amount = flower_amount

    def bouquet(self):
        bouquet_flowers = {}

        middle_cost = []
        wither_time = []
        for i in range(1, (self.flower_amount + 1)):
            flower = random.choice(list(self.dict_flowers.keys()))
            bouquet_flowers[i] = self.dict_flowers[flower]
            middle_cost.append(bouquet_flowers[i][4])
            wither_time.append(bouquet_flowers[i][1])

        sum_bouquet = 0
        for j in range(len(middle_cost)):
            sum_bouquet = sum_bouquet + middle_cost[j]

        print(f"The cost of the bouquet: {sum_bouquet}")

        remaining_days = 0
        middle_remaining_days = 0
        for m in range(len(wither_time)):
            remaining_days2 = remaining_days + wither_time[m]
            middle_remaining_days = remaining_days2 / self.flower_amount

        print(f"Wither time of the bouquet: {round(middle_remaining_days, 1)} days")
        print("My bouquet:")
        for count in bouquet_flowers.keys():
            print(f"  {count} : {bouquet_flowers[count][0]} - {bouquet_flowers[count][2]}, "
                  f"price - {bouquet_flowers[count][4]} rub, length - {bouquet_flowers[count][3]} cm, "
                  f"days left - {bouquet_flowers[count][1]}")
        return bouquet_flowers


class Sorted:
    def __init__(self, flower_sort, flower_type=None, flower_color=None, flower_price=None):
        self.flower_type = flower_type
        self.flower_sort = flower_sort
        self.flower_color = flower_color
        self.flower_price = flower_price

    def sorted_bouquet(self):

        if self.flower_sort == 1:
            count = 1
            for sort in sorted(my_bouquet.values()):
                print(f" {count} - {sort[0]}")
                count += 1
        elif self.flower_sort == 2:
            count = 1
            for sort in sorted(my_bouquet.values(), key=itemgetter(1)):
                print(f" {count} - {sort[0]}, {sort[1]} - days left")
                count += 1
        elif self.flower_sort == 3:
            count = 1
            for sort in sorted(my_bouquet.values(), key=itemgetter(2)):
                print(f" {count} - {sort[0]}, {sort[2]}")
                count += 1
        elif self.flower_sort == 4:
            count = 1
            for sort in sorted(my_bouquet.values(), key=itemgetter(3)):
                print(f" {count} - {sort[0]}, {sort[3]} - cm")
                count += 1
        elif self.flower_sort == 5:
            count = 1
            for sort in sorted(my_bouquet.values(), key=itemgetter(4)):
                print(f" {count} - {sort[0]}, {sort[4]} - rub")
                count += 1

    def flower_search_type(self):
        list_flowers = []

        for k in my_bouquet.keys():
            if self.flower_type == my_bouquet[k][0]:
                if self.flower_type == "Rose":
                    list_flowers.append(my_bouquet[k])
                elif self.flower_type == "Golden-daisy":
                    list_flowers.append(my_bouquet[k])
                elif self.flower_type == "Peony":
                    list_flowers.append(my_bouquet[k])
                elif self.flower_type == "Tulip":
                    list_flowers.append(my_bouquet[k])

        count = 1
        if list_flowers:
            print(f"Such a flowers is in the bouquet:")
            for flower in list_flowers:
                print(f"  {count} - {flower[0]} - {flower[2]}, "
                      f"price - {flower[4]} rub, "
                      f"length - {flower[3]} cm, "
                      f"days left - {flower[1]}")
                count += 1
        else:
            print("Sorry your flower is not in the bouquet")

    def flower_search_color(self):
        list_flowers_1 = []

        for k in my_bouquet.keys():
            if self.flower_color == my_bouquet[k][2]:
                if self.flower_color == "Red":
                    list_flowers_1.append(my_bouquet[k])
                elif self.flower_color == "White":
                    list_flowers_1.append(my_bouquet[k])
                elif self.flower_color == "Yellow":
                    list_flowers_1.append(my_bouquet[k])
                elif self.flower_color == "Pink":
                    list_flowers_1.append(my_bouquet[k])

        count_1 = 1
        if list_flowers_1:
            print(f"Such a flower colors is in the bouquet:")
            for flower in list_flowers_1:
                print(f"  {count_1} - {flower[0]} - {flower[2]}, "
                      f"price - {flower[4]} rub, "
                      f"length - {flower[3]} cm, "
                      f"days left - {flower[1]}")
                count_1 += 1
        else:
            print("Sorry your flower color is not in the bouquet")

    def flower_search_price(self):
        list_flowers_2 = []

        if self.flower_price == "a":
            for k in my_bouquet.keys():
                if my_bouquet[k][4] >= 6:
                    list_flowers_2.append(my_bouquet[k])
            count_2 = 1
            if list_flowers_2:
                print(f"Such a flower price is in the bouquet:")
                for price in list_flowers_2:
                    if max(list_flowers_2, key=itemgetter(4)):
                        print(f"  {count_2} - {price[0]} - {price[2]}, "
                              f"price - {price[4]} rub, "
                              f"length - {price[3]} cm, "
                              f"days left - {price[1]}")
                        count_2 += 1
            else:
                print("Sorry your flower price is not in the bouquet")
        elif self.flower_price == "b":
            for k in my_bouquet.keys():
                if my_bouquet[k][4] <= 5:
                    list_flowers_2.append(my_bouquet[k])
            count_2 = 1
            if list_flowers_2:
                print(f"Such a flower price is in the bouquet:")
                for price in list_flowers_2:
                    if min(list_flowers_2, key=itemgetter(4)):
                        print(f"  {count_2} - {price[0]} - {price[2]}, "
                              f"price - {price[4]} rub, "
                              f"length - {price[3]} cm, "
                              f"days left - {price[1]}")
                        count_2 += 1
            else:
                print("Sorry your flower price is not in the bouquet")


my_dict = {1: ["Rose", 10, "Red", 50, 10], 2: ["Rose", 5, "White", 30, 5],
           3: ["Golden-daisy", 8, "Yellow", 30, 8], 4: ["Golden-daisy", 4, "Pink", 25, 4],
           5: ["Peony", 9, "Pink", 40, 7], 6: ["Peony", 6, "White", 30, 3],
           7: ["Tulip", 7, "Red", 35, 6], 8: ["Tulip", 4, "Yellow", 30, 4]}

my_amount = input("Enter the number of flowers and we will generate a bouquet:")
my_amount = int(my_amount)
my_flower = Flowers(my_dict, my_amount)
my_bouquet = my_flower.bouquet()
print("Choose a sort method:")
print("  1 - Type")
print("  2 - Number of days the flower will last")
print("  3 - Color")
print("  4 - Stem length")
print("  5 - cost")
my_number = input("Enter the number of sort:")
my_number = int(my_number)
my_sort = Sorted(my_number)
my_sort.sorted_bouquet()
print("Select Options")
print("Flower type:")
print("- Rose")
print("- Golden-daisy")
print("- Peony")
print("- Tulip")
my_type = input("Your choice, enter type:")
my_sort = Sorted(my_number, my_type)
my_sort.flower_search_type()
print("- Red")
print("- White")
print("- Yellow")
print("- Pink")
my_color = input("Your choice, enter color:")
my_sort = Sorted(my_number, my_type, my_color)
my_sort.flower_search_color()
print("  a - Most expensive")
print("  b - Cheapest")
my_price_choice = input("Your choice, enter color:")
my_price = Sorted(my_number, my_type, my_color, my_price_choice)
my_price.flower_search_price()
