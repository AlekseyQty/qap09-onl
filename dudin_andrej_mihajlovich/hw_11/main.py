'''
Написать калькулятор. Программа должна содержать 4 функции принимающие
два аргумента и возвращающие результаты сложения, вычитания, умножения и
деления. Реализовать пользовательский интерфейс Methods. От него
унаследовать математические методы и реализовать их.
Добавить валидацию входных данных. Программа должна состоять из двух
файлов(main.py, func.py).
'''
from func import Methods

def calculator():
    while True:
        print("Возможные действия:\n"
              "Сложение: +\n"
              "Вычитание: -\n"
              "Умножение: *\n"
              "Деление: /\n"
              "Выйти: q\n")
        action = input("Выберите действие: ")
        if action in ('+', '-', '*', '/'):
            x = float(input("x = "))
            y = float(input("y = "))
            if action == '+':
                Methods.summ(x, y)
            elif action == '-':
                Methods.subtraction(x, y)
            elif action == '*':
                Methods.multiplication(x, y)
            elif action == '/':
                Methods.division(x, y)
            else:
                print("Выход из программы")
        break

calculator()