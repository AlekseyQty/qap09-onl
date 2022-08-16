# 3 Простейший калькулятор v0.1
# Реализуйте программу, которая спрашивала у пользователя, какую операцию он хочет
# произвести над числами, а затем запрашивает два числа и выводит результат
# Проверка деления на 0 Реализовать программу нужно с использованием функций.
# Пример
# Выберите операцию:
# 1 Сложение
# 2 Вычитание
# 3 Умножение
# 4 Деление
# Введите номер пункта меню:
# >>> 4
# Введите первое число:
# >>> 10
# Введите второе число:
# >>> 3
# Частное: 3, Остаток: 3
def sum(a, b):
    return print(f"Cумма {a} и {b} равна {a + b}")


def subtract(a, b):
    return print(f"Разность {a} и {b} равна {a - b}")


def multiply(a, b):
    return print(f"Умножение {a} на {b} равно {a * b}")


def divide(a, b):
    if b == 0:
        return print("Деление на 0 невозможно!")
    return print(f"Деление {a} на {b} равно {a / b}")


while True:
    operation = int(input("Выберите операцию:\n1.Cложение\n2.Вычитание\n3.Умножение\n4.Деление\n"))
    if operation == 1 or operation == 2 or operation == 3 or operation == 4:
        break
    print("Неверный ввод, попробуйте снова")

a = float(input("Введите первое число "))
b = float(input("Введите второе число "))
if operation == 1:
    sum(a, b)
elif operation == 2:
    subtract(a, b)
elif operation == 3:
    multiply(a, b)
elif operation == 4:
    divide(a, b)

