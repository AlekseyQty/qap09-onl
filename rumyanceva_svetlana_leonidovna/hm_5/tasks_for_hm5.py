from random import randint

# Task1. Факториал. Написать программу, которая считает факториал произвольного числа.
# Не использовать метод для расчета факториала из стандартной библиотеки.
# 5! = 5 × 4 × 3 × 2 × 1 = 120
try:
    number = int(input("Enter any integer number for which you want to calculate the factorial: "))
except ValueError:
    print("Oops! You has entered no integer number. Factorial is calculated only for integers.")
else:
    factorial = 1
    if number == 0:
        print("0! = 0")
    else:
        for i in range(1, number + 1):
            factorial *= i
        print(f"{number}! = {factorial}")
print("--------task1_end----------")
print("--------task2_start--------")
# Task2. Напишите программу, которая перебирает последовательность от 1 до 100.
# Для чисел, кратных 3, она должна написать: "Fuzz" вместо печати числа, а для чисел, кратных 5, печатать "Buzz".
# Для чисел, которые кратны 3 и 5, надо печатать "FuzzBuzz". Иначе печатать число.
# Вывод должен быть следующим:
# 1
# 2
# fuzz
# 4
# buzz
# fuzz
# 7
# 8
for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        print("FuzzBuzz")
    elif i % 5 == 0:
        print("Buzz")
    elif i % 3 == 0:
        print("Fuzz")
    else:
        print(i)

print("--------task2_end----------")
print("--------task3_start--------")
# Task3. The Game "Bills and cows". В классическом варианте игра рассчитана на двух игроков.
# Каждый из игроков задумывает и записывает тайное 4-значное число с неповторяющимися цифрами.
# Игрок, который начинает игру по жребию, делает первую попытку отгадать число.
# Попытка — это 4-значное число с неповторяющимися цифрами, сообщаемое противнику.
# Противник сообщает в ответ, сколько цифр угадано без совпадения с их позициями в тайном числе
# (то есть количество коров) и сколько угадано вплоть до позиции в тайном числе (то есть количество быков).
# При игре против компьютера игрок вводит комбинации одну за другой, пока не отгадает всю последовательность.
# Ваша задача реализовать программу, против которой можно сыграть в "Быки и коровы".


def verify_unique_number(num):
    while True:
        if len(set(list(num))) != 4:
            num = str(randint(1023, 9876))
        else:
            return num


def verify_integer_number(num):
    while True:
        try:
            num = int(num)
        except ValueError:
            print("You have entered no integer number. Try again. (Quit from the game: Ctrl+C) ")
            num = input("Enter any four-digit integer number with unique digits: ")
        else:
            return str(num)


def verify_unique_4digit_number(num):
    while True:
        if num[0] == "-":
            num = num.replace("-", "")
        if len(num) != 4:
            print("You have entered no four-digit number. Try again. (Quit from the game: Ctrl+C) ")
            num = input("Enter any four-digit integer number with unique digits: ")
            num = verify_integer_number(num)
        elif len(set(list(num))) != 4:
            print("Entered number has the same digits. Try again. (Quit from the game: Ctrl+C)")
            num = input("Enter any four-digit integer number with unique digits: ")
            num = verify_integer_number(num)
        else:
            return num


hidden_number = str(randint(1023, 9876))
new_hidden_number = verify_unique_number(hidden_number)
print(new_hidden_number, type(new_hidden_number))
estimated_number = input("Enter guessed four-digit integer number with unique digits: ")
new_estimated_number = verify_unique_4digit_number(verify_integer_number(estimated_number))

while True:
    bulls_counter, cows_counter = 0, 0
    position_list, position_bulls, position_cows = [], [], []
    print(new_hidden_number, new_estimated_number)
    for i in range(4):
        if new_estimated_number[i] == new_hidden_number[i]:
            bulls_counter += 1
        elif new_estimated_number[i] in new_hidden_number:
            cows_counter += 1

    if bulls_counter != 4:
        print(f"bulls = {bulls_counter}")
        print(f"cows = {cows_counter}")
        estimated_number = input("Try again. Enter guessed four-digit integer number with unique digits: ")
        new_estimated_number = verify_unique_4digit_number(verify_integer_number(estimated_number))
    else:
        print("You have won!!!!")
        break

print("--------task3_end----------")
