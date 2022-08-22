# Реализуйте программу, которая спрашивала у пользователя, какую операцию он хочет произвести над числами,
# а затем запрашивает два числа и выводит результат
# Проверка деления на 0.

def sum_function(number_1, number_2):
    print(number_1 + number_2)


def subtraction_function(number_1, number_2):
    print(number_1 - number_2)


def multiplication_function(number_1, number_2):
    print(number_1 * number_2)


def division_function(number_1, number_2):
    try:
        print(number_1 / number_2)
    except ZeroDivisionError:
        print("Вы не можете делить на ноль!")

print("Выберите операцию:")
print("1. Сложение")
print("2. Вычитание")
print("3. Умножение")
print("4. Деление")

my_choice = ""
while my_choice != "quit":
    my_choice = input("Введите желаемую математическую операцию: ")
    if my_choice == "quit":
        print("Goodbye")
    else:
        number_1 = input("Введите первое число: ")
        number_2 = input("Введите второе число: ")
        number_1 = int(number_1)
        number_2 = int(number_2)

        if my_choice == "1":
            sum_function(number_1, number_2)
        elif my_choice == "2":
            subtraction_function(number_1, number_2)
        elif my_choice == "3":
            multiplication_function(number_1, number_2)
        elif my_choice == "4":
            division_function(number_1, number_2)
        else:
            print("Попрубуйте еще раз!")
