print(f'{"̅" * 26}{"̅" * 26}')
print(f'{" " * 20} SECOND TASK {" " * 20}')
print(f'{" " * 20}  GENERATOR  {" " * 20}')
print(f'{"̅" * 26}{"̅" * 26}')

"""Генераторы:
2.	Напишите генератор который принимает список 
numbers = [34.6, -203.4, 44.9, 68.3, -12.2, 44.6, 12.7] 
и возвращает новый список только с положительными числами
"""


def generator_positive(numbers):
    new_arr = []
    for element in range(len(numbers)):
        if numbers[element] > 0:
            new_arr.append(numbers[element])
    yield new_arr


numbers = [34.6, -203.4, 44.9, 68.3, -12.2, 44.6, 12.7]
for i in generator_positive(numbers):
    print(i)
