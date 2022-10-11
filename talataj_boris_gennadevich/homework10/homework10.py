class Flower:
    def __init__(self, name, price, colour, stem_length, lifetime):
        self.name = name
        self.price = price
        self.colour = colour
        self.stem_lenght = stem_length
        self.lifetime = lifetime

class Bouquet:
    def __init__(self, flowers):
        self.flowers = flowers

    def cost_bouquet(self):
        price = 0
        for flower in self.flowers:
            price = price + flower.price

        return price

    def lifetime(self):
        lifetime = 0
        for flower in self.flowers:
            lifetime = lifetime + flower.lifetime

        lifetime = lifetime / len(self.flowers)

        return lifetime

    def search_flowers(self, flower_property, property_value):
        list_flowers = []
        if flower_property == 'price':
            for flower in self.flowers:
               if flower.price == property_value:
                   list_flowers.append(flower)

        elif flower_property == 'colour':
            for flower in self.flowers:
                if flower.colour == property_value:
                    list_flowers.append(flower)

        elif flower_property == 'stem_length':
            for flower in self.flowers:
                if flower.stem_length == property_value:
                    list_flowers.append(flower)

        elif flower_property == 'lifetime':
            for flower in self.flowers:
                if flower.lifetime == property_value:
                    list_flowers.append(flower)

        return list_flowers

    def is_flower(self, search_flower):
        for flower in self.flowers:
            if flower.price == search_flower.price and flower.colour == search_flower.colour and flower.stem_lenght == search_flower.stem_lenght and flower.lifetime == search_flower.lifetime:
               return True
        return False

flower_1 = Flower('Роза', 8, 'красный', 25, 15)
flower_2 = Flower('Тюльпан', 4, 'красный', 17, 22)
flower_3 = Flower('Лилия', 9, 'белый', 11, 22)
flower_4 = Flower('Хризантема', 7, 'желтый', 15, 18)
flower_5 = Flower('Ромашка', 5, 'белый', 13, 18)


list_2 = [flower_1, flower_2, flower_3]
list_3 = [flower_3, flower_4, flower_5]

Bouquet_1 = Bouquet(list_2)
Bouquet_2 = Bouquet(list_3)






