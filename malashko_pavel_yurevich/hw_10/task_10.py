# Цветочница. Определить иерархию и создать несколько цветов. Собрать букет (можно использовать аксессуары)
# с определением его стоимости. Определить время его увядания по среднему времени жизни всех цветов в букете.
# Позволить сортировку цветов в букете на основе различных параметров (свежесть/цвет/длина стебля/стоимость...)
# Реализовать поиск цветов в букете по определенным параметрам. Узнать, есть ли цветок в букете.
# Методы букета: 1)Время увядания, 2)Сортивка по полям цветка, 3)Поиск по полям, 4)Поиск цветка в букете


class Flower:
    def __init__(self, name, freshness, color, stem_length, cost):
        self.name = name
        self.freshness = freshness
        self.color = color
        self.stem_length = stem_length
        self.cost = cost


class Bouquet:
    def __init__(self):
        self.list = []

    def add_to_bouquet(self):  # Метод добавляющий цевток в букет.
        for i in range(len(all_flowers)):
            print(i + 1, all_flowers[i].name)

        num = input("Choose what flowers you want to see in your bouquet(press 'q' if you finally decided): ")
        while num != 'q':
            amount = int(input("Input amount: "))
            for i in range(amount):
                self.list.append(all_flowers[int(num) - 1])
            num = input("Choose what flowers you want to see in your bouquet(press 'q' if you finally decided): ")

    def bouquets_cost(self):  # Цена букета
        cost = 0
        for flower in self.list:
            cost += flower.cost
        return cost

    def wilting_time(self):  # Среднее время увядания букета
        wilting_time = 0
        for flower in self.list:
            wilting_time += flower.freshness
        wilting_time /= len(self.list)
        return wilting_time

    def sort_bouquet(self):  # Сортировка букета по выбранному полю.
        n = int(input("1.Freshness\n2.Color\n3.Stem length\n"
                      "4.Cost\nYou can sort your bouquet by the following parameters: "))
        if n == 1:
            self.list = sorted(self.list, key=lambda x: x.freshness)
            for flower in self.list:
                print(flower.name, flower.freshness)
        elif n == 2:
            self.list = sorted(self.list, key=lambda x: x.color)
            for flower in self.list:
                print(flower.name, flower.color)
        elif n == 3:
            self.list = sorted(self.list, key=lambda x: x.stem_length)
            for flower in self.list:
                print(flower.name, flower.stem_length)
        elif n == 4:
            self.list = sorted(self.list, key=lambda x: x.cost)
            for flower in self.list:
                print(flower.name, flower.cost)

    def find_by_field(self):  # Поиск цветов в букете по параметрам
        parameter = int(input("1.Freshness\n2.Color\n3.Stem length\n4.Cost\nChoose parameter in filter: "))
        if parameter == 1:
            for flower in self.list:
                if flower.freshness < 35:
                    print(flower.name, flower.cost)
        elif parameter == 2:
            for flower in self.list:
                if flower.color == 'red' or flower.color == 'purple':
                    print(flower.name, flower.color)
        elif parameter == 3:
            for flower in self.list:
                if flower.stem_length > 1:
                    print(flower.name, flower.stem_length)
        elif parameter == 4:
            for flower in self.list:
                if flower.cost < 110:
                    print(flower.name, flower.cost)

    def is_flower_in_bouquet(self, flower):
        if flower in self.list:
            print("This flower is already in the bouquet.")
        else:
            print("This flower is not yet in the bouquet.")

    def bouquet_view(self):
        view = []
        for flower in self.list:
            view.append(f"{self.list.count(flower)} {flower.name}")

        print(f"Now your bouquet looks like this: {set(view)}")


all_flowers = [Flower("Tulip", 40, "yellow", 2, 100),
               Flower("Rose", 35, "blue", 4, 120),
               Flower("Carnation", 45, "white", 1, 80),
               Flower("Lily", 20, "purple", 1, 60),
               Flower("Violet", 15, "red", 3, 60)]

bouquet1 = Bouquet()
bouquet1.add_to_bouquet()
# print(bouquet1.wilting_time())
# print(bouquet1.bouquets_cost())
bouquet1.sort_bouquet()
# bouquet1.bouquet_view()
# bouquet1.is_flower_in_bouquet(all_flowers[1])
bouquet1.find_by_field()


