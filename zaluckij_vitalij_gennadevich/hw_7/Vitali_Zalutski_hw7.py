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


def my_func(arr, rows, cols):
    new_arr = []
    for i in range(rows):
        new_arr2 = []
        for col in range(cols):
            new_arr2.append(arr[col + i * cols])
        new_arr.append(new_arr2)
    return new_arr


print(my_func([1,2,3,4,5,6], 2, 3))
print(my_func([1, 2, 3, 4, 5, 6, 7, 8], 4, 2))


# Шифр цезаря
# Шифр Цезаря — один из древнейших шифров. При шифровании каждый символ
# заменяется другим, отстоящим от него в алфавите на фиксированное число позиций.
# Примеры:
# hello world! -> khoor zruog!
# this is a test string -> ymnx nx f yjxy xywnsl
# Напишите две функции - encode и decode принимающие как параметр строку и число -
# сдвиг.


alfavit = ("ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ")
smeshenie = int(input("Шаг смещения:"))
message = (input("Ваше сообщение:").upper())
end = ""
for i in message:
    mesto = alfavit.find(i)
    new_mesto = mesto + smeshenie
    if i in alfavit:
        end += alfavit[new_mesto]
    else:
        end += i


print(end)












