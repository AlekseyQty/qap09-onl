# Цветочница. Определить иерархию и создать несколько цветов. Собрать букет (можно использовать аксессуары)
# с определением его стоимости. Определить время его увядания по среднему времени жизни всех цветов в букете.
# Позволить сортировку цветов в букете на основе различных параметров (свежесть/цвет/длина стебля/стоимость...)
# Реализовать поиск цветов в букете по определенным параметрам. Узнать, есть ли цветок в букете.
class Flower:
    flowers_list = []

    def __init__(self, name, color, stem_length, freshness_days, cost):
        self.name = name
        self.color = color
        self.stem_length = stem_length
        self.freshness_days = freshness_days
        self.cost = cost
        self.flowers_list.append(self)


class Buket:
    def __init__(self, tape_cost=0, wrapping_cost=0):
        self.tape_cost = tape_cost
        self.wrapping_cost = wrapping_cost

    @staticmethod
    def create_buket(flower_li):
        try:
            buket_l = []
            for flower in flower_li:
                print(f"Do you want to choose {flower.name}?")
                answer = input("Enter your answer (y/n): ").lower()
                if answer == "y":
                    number_flowers = int(input("How much? Enter any integer number: "))
                    for _ in range(number_flowers):
                        buket_l.append(flower)
            return buket_l
        except ValueError:
            print("You have entered no integer number")
            exit()

    def get_buket_cost(self, buket_li):
        flowers_cost = 0
        for flower in buket_li:
            # print(flower.name)
            flowers_cost += flower.cost
        total_cost = self.tape_cost + self.wrapping_cost + flowers_cost
        return f"The buket cost is {total_cost}"

    @staticmethod
    def get_buket_freshness_time(buket__list):  # find out average freshness time of the buket
        freshness_time = 0
        for flower in buket__list:
            freshness_time += flower.freshness_days
        average_freshness_time = freshness_time / len(buket__list)
        return f"The buket_freshness_time is {average_freshness_time} day(s)"

    @staticmethod
    def find_flower(buket__li, flower_name):  # find the flower for name
        for flower in buket__li:
            if flower.name == flower_name.title():
                return f"There is such flower, {flower.name}, in this buket"
            else:
                return f"There isn't such flower, {flower_name.title()}, in this buket"

    @staticmethod
    def sort_buket(buket__l):  # sorting for color
        my_list = []
        for flower in buket__l:
            my_list.append(flower.color)
        result = sorted(my_list)
        return result


flower1 = Flower("Iris", "yellow", 40, 2, 1000)
flower2 = Flower("Rose", "blue", 35, 4, 1200)
flower3 = Flower("Gypsophila", "white", 45, 1, 800)
flower4 = Flower("Fern", "green", 35, 1, 600)
flower5 = Flower("Freesia", "red", 35, 3, 600)

small_buket = Buket(300, 100)
print()
buket_list = small_buket.create_buket(Flower.flowers_list)
print()
print(small_buket.get_buket_cost(buket_list))
print(small_buket.get_buket_freshness_time(buket_list))

print(small_buket.sort_buket(buket_list))
print(small_buket.find_flower(buket_list, input("Enter any flower name: ")))
