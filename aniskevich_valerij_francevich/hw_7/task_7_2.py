# 2 Напишите генератор который принимает список numbers = [34.6, -203.4, 44.9, 68.3, -
# 12.2, 44.6, 12.7] и возвращает новый список только с положительными числами


def generator(numbers):
    my_list = []
    for i in numbers:
        if i > 0:
            my_list.append(i)
    yield my_list


result = generator([34.6, -203.4, 44.9, 68.3, -12.2, 44.6, 12.7])

for i in result:
    print(i)