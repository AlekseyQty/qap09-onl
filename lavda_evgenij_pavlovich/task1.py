"""Ваша задача написать программу, принимающее число - номер кредитной карты(число
может быть четным или не четным). И проверяющей может ли такая карта существовать.
Предусмотреть защиту от ввода букв, пустой строки и т.д.
"""

from functools import reduce


def luhn(code):
    # Предварительно рассчитанные результаты умножения на 2 с вычетом 9 для больших цифр
    # Номер индекса равен числу, над которым проводится операция
    lookup = (0, 2, 4, 6, 8, 1, 3, 5, 7, 9)
    code = reduce(str.__add__, filter(str.isdigit, code))
    evens = sum(int(i) for i in code[-1::-2])
    odds = sum(lookup[int(i)] for i in code[-2::-2])
    return (evens + odds) % 10 == 0


your_credit_card_number = input("Введите номер кредитной карты: ")
if your_credit_card_number.isdigit():
    print(luhn(your_credit_card_number))
else:
    print("Номер карты должен состоять из цифр")
