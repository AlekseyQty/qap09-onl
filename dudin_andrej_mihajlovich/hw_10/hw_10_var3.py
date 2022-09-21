class Flower:
    flowers_list = []

    def __init__(self, name, color, stem_length, freshness_days, cost):
        self.name = name
        self.color = color
        self.stem_length = stem_length
        self.freshness_days = freshness_days
        self.cost = cost
        self.flowers_list.append(self)


class Bouquet:
    def __init__(self, tape_cost=0, wrapping_cost=0):
        self.tape_cost = tape_cost
        self.wrapping_cost = wrapping_cost

    @staticmethod
    def create_bouquet(flower_list):
        try:
            bouquet_list = []
            for flower in flower_list:
                select_flower = input(f"Do you want to choose {flower.name}? (y/n): ").lower()
                if select_flower == "y":
                    number_flowers = int(input("Number of flowers: "))
                    for number in range(number_flowers):
                        bouquet_list.append(flower)
            return bouquet_list
        except ValueError:
            print("You have entered no integer value")
            exit()

    def bouquet_cost(self, bouquet_list_arg):
        flowers_cost = 0
        for flower in bouquet_list_arg:
            flowers_cost += flower.cost
        total_cost = self.tape_cost + self.wrapping_cost + flowers_cost
        return f"The bouquet cost is {total_cost}"

    @staticmethod
    def bouquet_freshness_time(bouquet_list_arg):
        freshness_time = 0
        for flower in bouquet_list_arg:
            freshness_time += flower.freshness_days
        average_freshness_time = freshness_time / len(bouquet_list_arg)
        return f"The bouquet's freshness time is {average_freshness_time} day(s)"

    @staticmethod
    def find_flower(bouquet_list_arg, flower_name):  # find the flower by name
        for flower in bouquet_list_arg:
            if flower.name == flower_name.title():
                return f"Yes, {flower.name} is in this bouquet"
            else:
                return f"No, {flower_name.title()} is not in this bouquet"

    @staticmethod
    def sort_colours(bouquet_list_arg):  # sorting for color
        colours_list = []
        for flower in bouquet_list_arg:
            colours_list.append(flower.color)
        return sorted(colours_list)


flower1 = Flower("Iris", "yellow", 40, 2, 1000)
flower2 = Flower("Rose", "blue", 35, 4, 1200)
flower3 = Flower("Gypsophila", "white", 45, 1, 800)
flower4 = Flower("Fern", "green", 35, 1, 600)
flower5 = Flower("Freesia", "red", 35, 3, 600)

bouquet = Bouquet(300, 100)
bouquet_list = bouquet.create_bouquet(Flower.flowers_list) #к пустому bouquet применяем create_bouquet, в который передаем список flowers_list

print(bouquet.bouquet_cost(bouquet_list))
print(bouquet.bouquet_freshness_time(bouquet_list))

print(bouquet.sort_colours(bouquet_list))
print(bouquet.find_flower(bouquet_list, input("Check flower in bouquet. Enter flower name: ")))