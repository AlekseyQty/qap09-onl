print(f'{"̅" * 26}{"̅" * 26}')
print(f'{" " * 20} FIRST TASK {" " * 20}')
print(f'{"̅" * 26}{"̅" * 26}')

"""
1. Напишите функцию, которая принимает на вход одномерный массив и два числа - размеры выходной матрицы. 
   На выход программа должна подавать матрицу нужного размера, сконструированную из элементов массива.
reshape([1, 2, 3, 4, 5, 6], 2, 3) => 
[
    [1, 2, 3],
    [4, 5, 6]
]
reshape([1, 2, 3, 4, 5, 6, 7, 8], 4, 2) =>	 
[
    [1, 2],
    [3, 4],
    [5, 6],
    [7, 8]
]
"""


def reshape(list_input, strings, columns):
    array_new = []
    for element in range(0, len(list_input), columns):
        array_new.append(list_input[element:element + columns])

    return array_new


print(reshape([1, 2, 3, 4, 5, 6], 2, 3))
print(reshape([1, 2, 3, 4, 5, 6, 7, 8], 4, 2))
