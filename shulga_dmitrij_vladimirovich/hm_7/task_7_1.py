# Напишите функцию, которая принимает на вход одномерный массив и два числа - размеры выходной матрицы.
# На выход программа должна подавать матрицу нужного размера, сконструированную из элементов массива.

import numpy as np
from random import randint

my_list = []
for i in range(8):
    my_list.append(randint(0, 10))
print(f"Исходный массив: {my_list}")

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

        def changed_matrix(number_line, number_column):
            new_list = np.reshape(my_list, (number_line, number_column))
            print("Новые массивы:" '\n' f"{new_list}")

        changed_matrix(number_line, number_column)
