"""Четыре основные функции программы калькулятор"""


class Methods:
    @staticmethod
    def summ(x, y):
        print(f'{x} + {y} = {x+y}')

    @staticmethod
    def subtraction(x, y):
        return print(f'{x} - {y} = {x-y}')

    @staticmethod
    def multiplication(x, y):
        return print(f'{x} * {y} = {x*y}')

    @staticmethod
    def division(x, y):
        if y != 0:
            return print(f'{x} / {y} = {x / y}')
        else:
            return print("Деление на ноль!")