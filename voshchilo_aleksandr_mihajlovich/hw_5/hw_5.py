import math
import random
# 1. Написать программу, которая считает факториал произвольного числа. Не
# использовать метод для расчета факториала из стандартной библитоеки.

number_ran = 5
list_number = []

for i in range(1, number_ran+1):
    list_number.append(i)

# print(list_number)
number_f = math.prod(list_number)
print(f"Факториал числа {number_ran} равен {number_f}")


# 2. BuzzFuzz
# Напишите программу, которая перебирает последовательность от 1 до 100 Для чисел
# кратных 3 она должна написать: "Fuzz" вместо печати числа, а для чисел кратных 5
# печатать "Buzz". Для чисел которые кратны 3 и 5 надо печатать "FuzzBuzz". Иначе
# печатать число.

for i in range(1 , 101):
    if i % 3 == 0 and i % 5 == 0:
        print('FuzzBuzz')
    elif i % 3 == 0:
        print('Fuzz')
    elif i % 5 == 0:
        print('Buzz')
    else:
        print(i)


# 3. Быки и коровы
# В классическом варианте игра рассчитана на двух игроков. Каждый из игроков задумывает
# и записывает тайное 4-значное число с неповторяющимися цифрами. Игрок, который
# начинает игру по жребию, делает первую попытку отгадать число. Попытка — это 4-
# значное число с неповторяющимися цифрами, сообщаемое противнику. Противник
# сообщает в ответ, сколько цифр угадано без совпадения с их позициями в тайном числе
# (то есть количество коров) и сколько угадано вплоть до позиции в тайном числе (то есть
# количество быков).
# При игре против компьютера игрок вводит комбинации одну за другой, пока не отгадает
# всю последовательность.
# Ваша задача реализовать программу, против которой можно сыграть в "Быки и коровы"


list_b = []
while len(set(list_b)) < 4:
    list_b.append(random.randint(0, 9))
else:
    print("Случайное число загадано")

list_b_numb = list(map(int, set(list_b)))  # случайное число
print(list_b_numb)

result_list = ["Бык"]

while result_list.count("Бык") < 4:
    a = "1"
    while len(set(list(map(int, a)))) < 4:  # проверка числа на повтор
        a = str(input("Введите четырехзначное число без повторов: "))
    else:
        print(" ")

    list_a_numb = list(map(int, a))  # число пользователя
    # print(list_a_numb)

    result_list = []

    for i in list_a_numb:
        for j in list_b_numb:
            if i == j:
                if list_a_numb.index(i) == list_b_numb.index(j):
                    result_list.append("Бык")
                else:
                    result_list.append("Корова")
            else:
                continue

    # print(result_list)

    if result_list.count("Корова") >= 1:
        if result_list.count("Бык") == 1:
            print("Один бык,", end="")
        elif result_list.count("Бык") == 2:
            print("Два быка,", end="")
        elif result_list.count("Бык") == 3:
            print("Три быка,", end="")

    if result_list.count("Корова") < 1:
        if result_list.count("Бык") == 1:
            print("Один бык")
        elif result_list.count("Бык") == 2:
            print("Два быка")
        elif result_list.count("Бык") == 3:
            print("Три быка")

    if result_list.count("Бык") >= 1:
        if result_list.count("Корова") == 1:
            print(" одна корова")
        elif result_list.count("Корова") == 2:
            print(" две коровы")
        elif result_list.count("Корова") == 3:
            print(" три коровы")
        elif result_list.count("Корова") == 4:
            print(" четыре коровы")

    if result_list.count("Бык") < 1:
        if result_list.count("Корова") == 1:
            print("Одна корова")
        elif result_list.count("Корова") == 2:
            print("Две коровы")
        elif result_list.count("Корова") == 3:
            print("Три коровы")
        elif result_list.count("Корова") == 4:
            print("Четыре коровы")
else:
    print("Вы выйграли!")




