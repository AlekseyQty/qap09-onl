"""1 Напишите функцию, которая принимает на вход одномерный массив и два числа -
размеры выходной матрицы. На выход программа должна подавать матрицу нужного
размера, сконструированную из элементов массива.
reshape([1, 2, 3, 4, 5, 6], 2, 3) =>
[1, 2, 3],
[4, 5, 6]
reshape([1, 2, 3, 4, 5, 6, 7, 8,], 4, 2) =>
[1, 2],
[3, 4],
[5, 6],
[7, 8]
"""


def get_new_array(your_lst, list_size, list_count):
    new_array = [your_lst[i:i + list_size] for i in range(0, len(your_lst), list_size)]
    return new_array[: list_count]


print(get_new_array([1, 2, 3, 4, 5, 6, 7, 8], 2, 4))
