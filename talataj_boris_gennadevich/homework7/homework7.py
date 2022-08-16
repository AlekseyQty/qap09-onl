#Напишите функцию, которая принимает на вход одномерный массив и два числа -
# размеры выходной матрицы. На выход программа должна подавать матрицу нужного
# размера, сконструированную из элементов массива. reshape([1, 2, 3, 4, 5, 6], 2, 3) =>
# [1, 2, 3],
# [4, 5, 6]
# reshape([1, 2, 3, 4, 5, 6, 7, 8,], 4, 2) =>
# [1, 2],
# [3, 4],
# [5, 6],
# [7, 8]

def reshape(arr, lines, columns):
    new_arr = []
    for lines in range(lines):
        tmp_arr = []
        for num in range(columns):
            tmp_arr.append(arr[num + columns*lines])
        new_arr.append(tmp_arr)
    return new_arr

print(reshape([1, 2, 3, 4, 5, 6], 2, 3))
print(reshape([1, 2, 3, 4, 5, 6, 7, 8,], 4, 2))


#Напишите генератор который принимает список numbers = [34.6, -203.4, 44.9, 68.3, -12.2, 44.6, 12.7]
#и возвращает новый список только с положительными числами

def first_generator(numb):
    my_list = []
    for i in numb:
        if i > 0:
            my_list.append(i)
    yield my_list

generator = first_generator([34.6, -203.4, 44.9, 68.3, -12.2, 44.6, 12.7])
for num in generator:
    print(num)


# Шифр Цезаря

alfabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

step = int(3)
report = input('Введите сообщение : ').upper()

answer = ''

for i in report:
    message = alfabet.find(i)
    new_message = message + step
    if i in alfabet:
        answer = answer + alfabet[new_message]
    elif i == ' ':
        answer = answer + ' '

print(answer)