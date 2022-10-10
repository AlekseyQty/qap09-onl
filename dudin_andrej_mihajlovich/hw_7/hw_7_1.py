'''
Напишите функцию, которая принимает на вход одномерный массив и два числа -
размеры выходной матрицы. На выход программа должна подавать матрицу нужного
размера, сконструированную из элементов массива.
reshape([1, 2, 3, 4, 5, 6], 2, 3) =>
[
[1, 2, 3],
[4, 5, 6]
]
reshape([1, 2, 3, 4, 5, 6, 7, 8,], 4, 2) =>
[
[1, 2],
[3, 4],
[5, 6],
[7, 8]
]
'''
import numpy as np

def reshape(input_list, strings,columns):
    result = []
    splits = np.array_split(input_list, columns)
    for arr in splits:
        result.append(list(arr))
    print(result)

reshape([1, 2, 3, 4, 5, 6, 7, 8,], 4, 2)
reshape([1, 2, 3, 4, 5, 6], 2, 3)
