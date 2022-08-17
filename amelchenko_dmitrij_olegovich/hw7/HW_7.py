# #1 Напишите функцию, которая принимает на вход одномерный массив и два числа -
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

def reshap(my_list, list_size, col):
    new_arr = [my_list[i:i + list_size] for i in range (0, len(my_list), list_size)]
    return new_arr[: col]

print(reshap([1, 2, 3, 4, 5, 6], 3, 2))

# #2. Напишите генератор который принимает список numbers = [34.6, -203.4, 44.9, 68.3, -
# 12.2, 44.6, 12.7] и возвращает новый список только с положительными числами

def generator(x):
    my_list = []
    for i in x:
        if i > 0:
            my_list.append(i)
    return my_list

print(generator([34.6, -203.4, 44.9, 68.3, -12.2, 44.6, 12.7]))



#3 Шифр цезаря

def caesar():
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ'

    step = int(input('Введите шаг шифра: '))

    report = input('Введите сообщение для шифровки: ')

    answer = ''

    for i in report.upper():
        site = alphabet.find(i)
        new_site = site + step
        if i in alphabet:
            answer = answer + alphabet[new_site]

    print(answer)

caesar()