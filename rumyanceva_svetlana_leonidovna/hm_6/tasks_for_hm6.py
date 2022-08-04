print("--------task1_start--------")
# Task1_Validate Ваша задача написать программу, принимающую число - номер кредитной карты
# (число может быть четным или не четным)и проверяющую может ли такая карта существовать.
# Предусмотреть защиту от ввода букв, пустой строки и т.д. Lun Algorithm


def validate_creditcard_digits(creditcard_num):
    """Validate № credit card - all digits are numbers. And № credit card is no empty string."""
    while True:
        creditcard_str = ""
        for elem in creditcard_num.split():
            if elem.isdigit():
                creditcard_str += elem
                #  print(creditcard_str)

        creditcard_list = list(map(int, creditcard_str))
        if len(creditcard_list) == len(list("".join(creditcard_num.split()))) and creditcard_list:
            return creditcard_list
        else:
            print("The number of the credit card is wrong. It must consist of only numbers.")
            creditcard_num = input('Try again.(Exit the program:Ctrl+C) Enter your number of the credit card: ')


def validate_creditcard_number(creditcard_dig):
    """ Algorithm Lun"""
    if 11 <= len(creditcard_dig) <= 19:  # № credit card can contain 11, 13, 14, 15, 16, 18 or 19 digits
        for i in range(len(creditcard_dig) - 2, -1, -2):
            creditcard_dig[i] = creditcard_dig[i] * 2
            if creditcard_dig[i] > 9:
                creditcard_dig[i] = creditcard_dig[i] - 9
        return sum(creditcard_dig) % 10 == 0
    return "This number is no credit card number."


creditcard_number = input("Enter your number of the credit card: ")
creditcard_digit = validate_creditcard_digits(creditcard_number)

print(validate_creditcard_number(creditcard_digit))

print("--------task1_end----------")
print("--------task2_start--------")
# Task2 Подсчет количества букв. На вход подается строка, например, "cccbba"
# результат работы программы - строка “c3b2a"


def calculate_letters(text):
    counter = 1
    new_string = ""
    for i in range(len(text)):  # validate each symbol of the string
        if not text[i].isalpha():  # if symbol is no letter, just add to new_string
            new_string += text[i]
        elif i == len(text) - 1 and counter != 1:
            new_string += text[i] + str(counter)
            continue
        elif i == len(text) - 1 and counter == 1:
            new_string += text[i]
            continue
        elif text[i] == text[i + 1]:  # calculate the same letters
            counter += 1
        elif counter == 1:
            new_string += text[i]  # if symbol is one, just add to new_string
        else:
            new_string += text[i] + str(counter)
            counter = 1
    return new_string


my_string = input("Enter any sentence: ")
print(calculate_letters(my_string))

print("--------task2_end----------")
print("--------task3_start--------")
# Task3 Простейший калькулятор v0.1. Реализуйте программу, которая спрашивала у пользователя, какую операцию
# он хочет произвести над числами, а затем запрашивает два числа и выводит результат. Проверка деления на 0.
# Реализовать программу нужно с использованием функций.


def add(first_num, second_num):
    return first_num + second_num


def subtract(first_num, second_num):
    return first_num - second_num


def multiply(first_num, second_num):
    return int(first_num * second_num)


def divide(first_num, second_num):
    try:
        result = first_num / second_num
    except ZeroDivisionError:
        return "Division by 0!!!"
    else:
        return result


try:
    first_number = float(input("Enter the first number: "))
    act = input("Menu: "
                "1: addition, 2: subtraction, 3: multiplication, 4: division. "
                "Choice any actions from 1 or 2 or 3 or 4: ")
    second_number = float(input("Enter the second number: "))
    actions = {"1": add(first_number, second_number), "2": subtract(first_number, second_number),
               "3": multiply(first_number, second_number), "4": divide(first_number, second_number)}
    print(actions.get(act, "No such action in the menu."))

except ValueError:
    print("It’s not a number.")

print("--------task3_end--------")
