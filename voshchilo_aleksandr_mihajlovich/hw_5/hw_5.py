import random
# 1. Написать программу, которая считает факториал произвольного числа. Не
# использовать метод для расчета факториала из стандартной библитоеки.

number_ran = 6
list_number = []
for i in range(1, number_ran+1):
    list_number.append(i)
numb_fact = 1
for i in list_number:
    numb_fact *= i

print(f"Факториал числа {number_ran} равен {numb_fact}")


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


pc_rand = []
while len(set(pc_rand)) < 4:
    pc_rand.append(random.randint(0, 9))
else:
    print("Случайное число загадано")

pc_rand_numb = list(map(int, set(pc_rand)))  # случайное число

result_list = ["Бык"]

while result_list.count("Бык") < 4:
    user_choice = str(input("Введите четырехзначное число без повторов: "))
    while len(set(list(map(int, user_choice)))) != 4:  # проверка числа на повтор
        user_choice = str(input("Введите четырехзначное число без повторов: "))
    else:
        print(" ")

    list_user_choice = list(map(int, user_choice))  # число пользователя

    result_list = []

    for i in list_user_choice:
        for j in pc_rand_numb:
            if i == j:
                if list_user_choice.index(i) == pc_rand_numb.index(j):
                    result_list.append("Бык")
                else:
                    result_list.append("Корова")
            else:
                continue

    print(f"{result_list.count('Корова')} коров(а/ы) {result_list.count('Бык')} бык(а)")
else:
    print("Вы выйграли!")




