# Напишите генератор который принимает список numbers = [34.6, -203.4, 44.9, 68.3, -12.2, 44.6, 12.7] и возвращает
# новый список только с положительными числами

def positive_generator(*args):
    for number in args:
        if number > 0:
            yield number


positive_numbers = positive_generator(34.6, -203.4, 44.9, 68.3, -12.2, 44.6, 12.7)
for positive_number in positive_numbers:
    print(positive_number)
