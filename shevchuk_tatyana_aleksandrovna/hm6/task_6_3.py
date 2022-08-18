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


start = int(input("Select the number of operation: 1. Addition, 2. Subtraction, 3. Multiplication, 4. Division"))
if start > 4 or start < 1:
    print("Choose correct operation")

first_num_input = int(input("Enter the first number: "))
second_num_input = int(input("Enter the second number: "))


def calc(first_num_input, second_num_input):
    if start == 1:
        result = first_num_input + second_num_input
    elif start == 2:
        result = first_num_input - second_num_input
    elif start == 3:
        result = first_num_input * second_num_input
    elif start == 4:
        if second_num_input == 0:
            result = "Division by 0 is not allowed"
        else:
            result = f" Private: {int(first_num_input // second_num_input)},   Balance: {int(first_num_input % second_num_input)}"
    return f"The result of your operation: {result}"


print(calc(first_num_input, second_num_input))
