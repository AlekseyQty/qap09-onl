# 1 Напишите функцию, которая принимает на вход одномерный массив и два числа -
# размеры выходной матрицы. На выход программа должна подавать матрицу нужного
# размера, сконструированную из элементов массива.
# reshape([1, 2, 3, 4, 5, 6], 2, 3) =>
# [
# [1, 2, 3],
# [4, 5, 6]
# ]
# reshape([1, 2, 3, 4, 5, 6, 7, 8,], 4, 2) =>
# [
# [1, 2],
# [3, 4],
# [5, 6],
# [7, 8]
# ]
finish_list = []


def reshape(my_list, stolb, stroka):
    for a in range(stolb):
        new_list = []
        for i in range(stroka):
            new_list.append(my_list[a * stroka + i])
        finish_list.append(new_list)
    return finish_list


print(reshape([1, 2, 3, 4, 5, 6, 7, 8,], 4, 2))
