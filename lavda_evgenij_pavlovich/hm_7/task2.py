"""Напишите генератор который принимает список numbers = [34.6, -203.4, 44.9, 68.3, -
12.2, 44.6, 12.7] и возвращает новый список только с положительными числами"""


def my_generator(numbers):
    new_list = []
    for i in numbers:
        if i > 0:
            new_list.append(i)
    yield new_list


generetor = my_generator([34.6, -203.4, 44.9, 68.3, -12.2, 44.6, 12.7])
for num in generetor:
    print(num)
