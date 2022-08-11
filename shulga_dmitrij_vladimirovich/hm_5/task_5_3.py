# 3.Быки и коровы
# В классическом варианте игра рассчитана на двух игроков.
# Каждый из игроков задумывает и записывает тайное 4-значное число с неповторяющимися цифрами.
# Игрок, который начинает игру по жребию, делает первую попытку отгадать число.
# Попытка — это 4-значное число с неповторяющимися цифрами, сообщаемое противнику.
# Противник сообщает в ответ, сколько цифр угадано без совпадения с их позициями в тайном числе
# (то есть количество коров) и сколько угадано вплоть до позиции в тайном числе (то есть количество быков).
# При игре против компьютера игрок вводит комбинации одну за другой, пока не отгадает всю последовательность.
# Ваша задача реализовать программу, против которой можно сыграть в "Быки и коровы"

import random
number = random.sample("1234567890", 4)
number = int("".join(number))
if number < 1000:
    number = number * 10
number = str(number)
print(f" Hidden number: {number}")

my_number = ""
while my_number != "quit":
    my_number = input("Please enter your four-digit number: ")
    if my_number == number:
        print("Вы выиграли!")
        break
    if my_number == "quit":
        print("Goodbye")
    else:
        count_2 = 0
        count_3 = None
        index = None
        bulls = []
        for i in range(len(number)):
            if number[i] == my_number[i]:
                count_2 += 1
                bulls.append(str(my_number[i]))
            if count_2 == 1:
                count_3 = "Один бык"
                continue
            elif count_2 == 2:
                count_3 = "Два быка"
                continue
            elif count_2 == 3:
                count_3 = "Три быка"
                continue
            else:
                count_3 = ""
                index = ""

        count = 0
        count_1 = None
        for j in number:
            if j in my_number:
                if j in bulls:
                    count_1 = ""
                else:
                    count += 1
            if count == 1:
                count_1 = "Одна корова"
                continue
            elif count == 2:
                count_1 = "Две коровы"
                continue
            elif count == 3:
                count_1 = "Три коровы"
                continue
            elif count == 4:
                count_1 = "Четыри коровы"
                continue
            else:
                count_1 = ""

        if count_1 == count_3 == "":
            print("Try again")
        else:
            print(f"{count_1} {count_3}")


