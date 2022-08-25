"""Четыре основные функции программы калькулятор"""


class Methods:
    @staticmethod
    def addition(x, y):
        print(f'{x} + {y} = {x+y}')

    @staticmethod
    def subtaraction(x, y):
        print(f'{x} - {y} = {x-y}')

    @staticmethod
    def multiplication(x, y):
        print(f'{x} * {y} = {x*y}')

    @staticmethod
    def division(x, y):
        if y != 0:
            print(f'{x} / {y} = {x / y}')
        else:
            print("Деление на ноль!")
