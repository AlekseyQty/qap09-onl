# 2 Напишите генератор который принимает список numbers = [34.6, -203.4, 44.9, 68.3, -
# 12.2, 44.6, 12.7] и возвращает новый список только с положительными числами


def positive_number(numbers):
    positive_number = []
    for elements in numbers:
        if elements > 0:
            positive_number.append(elements)
    yield positive_number


result = positive_number([34.6, -203.4, 44.9, 68.3, -12.2, 44.6, 12.7])
print(type(result), next(result))
