import string

# 1 Напишите функцию, которая принимает на вход одномерный массив и два числа -
# размеры выходной матрицы. На выход программа должна подавать матрицу нужного
# размера, сконструированную из элементов массива.

def reshape_num():
    """
    Сhanges shape of list, does not change data in list

    """
    numb_in = [int(i) for i in input('Введите список чисел через пробел: ').split()]
    num_lines = int(input("Введите количество строк выходной матрицы:"))
    num_columns = int(input("Введите количество столбцов выходной матрицы:"))
    numb_in.append(0)  # for work with slice
    list_numb_reshape = []
    for i in range(num_lines):
        list_numb_reshape.append(numb_in[num_columns * i:num_columns + (num_columns * i)])
    return list_numb_reshape


print(reshape_num())


# 2. Напишите генератор который принимает список numbers = [34.6, -203.4, 44.9, 68.3, -
# 12.2, 44.6, 12.7] и возвращает новый список только с положительными числами


numbers_list = [1.2, -2.369, -5.895, 6896.32]

plus_number_list = [i for i in numbers_list if i > 0]

print(plus_number_list)


# 3. Шифр цезаря

def encode():
    alf_letters = string.ascii_lowercase
    list_alf_letters = [i for i in alf_letters]
    message = str(input("Введите текст для шифрования: "))
    shift = int(input("Введите сдвиг шифрования: "))
    list_message = [i for i in message]
    new_message = []

    for i in message:
        if i.isalpha():
            if list_alf_letters.index(i) + shift < len(list_alf_letters):
                new_message.append(list_alf_letters.index(i) + shift)
            else:
                new_message.append(list_alf_letters.index(i) + shift - len(list_alf_letters))
        else:
            new_message.append(i)

    new_message_translate = []

    for i in new_message:
        if str(i).isdigit():
            new_message_translate.append(list_alf_letters[i])
        else:
            new_message_translate.append(i)
    return "".join(new_message_translate)


print(encode())


def decode():
    alf_letters = string.ascii_lowercase
    list_alf_letters = [i for i in alf_letters]
    message = str(input("Введите текст для шифрования: "))
    shift = int(input("Введите сдвиг шифрования: "))
    list_message = [i for i in message]
    new_message = []

    for i in message:
        if i.isalpha():
            if list_alf_letters.index(i) - shift >= 0:
                new_message.append(list_alf_letters.index(i) - shift)
            else:
                new_message.append(list_alf_letters.index(i) - shift + len(list_alf_letters))
        else:
            new_message.append(i)

    new_message_translate = []

    for i in new_message:
        if str(i).isdigit():
            new_message_translate.append(list_alf_letters[i])
        else:
            new_message_translate.append(i)
    return "".join(new_message_translate)


print(decode())
