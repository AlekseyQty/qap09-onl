# Напишите функцию, которая принимает на вход одномерный массив и два числа - размеры выходной матрицы.
# На выход программа должна подавать матрицу нужного размера, сконструированную из элементов массива.

from random import randint

def my_decorator(func):
    def wrapper(new_list):
        print("[")
        func(new_list)
        print("]")

    return wrapper

@my_decorator
def changed_matrix(number_line):
    new_list = []
    for i in range(0, len(my_list), number_line):
        new_list.append(my_list[i:i + number_line])

    for j in range(0, len(new_list)):
        print(f"  {new_list[j]}")

number_1 = ""
number_2 = ""
while number_1 != "quit" or number_2 != "quit":
    number_1 = input("Введите желаемое количество строк: ")
    if number_1 == "quit":
        print("Goodbye")
        break
    number_2 = input("Введите желаемое количество столбцов: ")
    if number_2 == "quit":
        print("Goodbye")
        break
    else:
        number_line = int(number_1)
        number_column = int(number_2)
        my_list = []
        for i in range(number_line * number_column):
            my_list.append(randint(0, 10))
        print(f"Исходный массив: {my_list}")

        changed_matrix(number_line)
