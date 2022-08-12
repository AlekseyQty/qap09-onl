# Подсчет количества букв. На вход подается строка, например, "cccbba" результат работы программы -
# строка “c3b2a".
# Примеры для проверки работоспособности:
# "cccbba" == "c3b2a"
# "abeehhhhhccced" == "abe2h5c3ed"
# "aaabbceedd" == "a3b2ce2d2"
# "abcde" == "abcde"
# "aaabbdefffff" == "a3b2def5"

# Леша, знаю, что не совсем как в задании, но пока только так додумалась написать

# Option_1

print(("-" * 25) + "Task_2.Option_1" + ("-" * 25))


def count_letter(my_string):
    for i in range(len(my_string)):
        if my_string[i] not in my_string[:i]:
            print(my_string[i], my_string.count(my_string[i]))


count_letter("cccbba")

# Option_2

print(("-" * 25) + "Task_2.Option_2" + ("-" * 25))

str = input("Enter your string: ")
for i in range(len(str)):
    if i == str.find(str[i]):
        print(str[i], str.count(str[i]))

# Реализуйте программу, которая спрашивала у пользователя, какую операцию он хочет произвести над числами,
# а затем запрашивает два числа и выводит результат. Проверка деления на 0.
# Пример
# Выберите операцию:
#     1. Сложение
#     2. Вычитание
#     3. Умножение
#     4. Деление
# Введите номер пункта меню:
# >>> 4
# Введите первое число:
# >>> 10
# Введите второе число:
# >>> 3
# Частное: 3, Остаток: 3

print(("-" * 25) + "Task_3" + ("-" * 25))

while True:
    print("Enter 0 to stop the program")
    operation = input("Select the number of operation: 1-Addition, 2-Subtraction, 3-Multiplication, 4-Division ")
    if operation == "0":
        break
    if operation not in ("1", "2", "3", "4"):
        continue
    number_1 = float(input("Enter the first number: "))
    number_2 = float(input("Enter the second number: "))
    if operation == "1":
        print(number_1 + number_2)
    elif operation == "2":
        print(number_1 - number_2)
    elif operation == "3":
        print(number_1 * number_2)
    elif operation == "4":
        if number_2 != 0:
            print("Quotient:", number_1 // number_2)
            print("Remainder:", number_1 % number_2)
        else:
            print("Cannot be divided by zero")

# Ваша задача написать программу, принимающее число - номер кредитной карты
# (число может быть четным или не четным). И проверяющей может ли такая карта
# существовать. Предусмотреть защиту от ввода букв, пустой строки и т.д.
# Упрощённый алгоритм алгоритма Луна:
# 1. Цифры проверяемой последовательности нумеруются справа налево.
# 2. Цифры, оказавшиеся на нечётных местах, остаются без изменений.
# 3. Цифры, стоящие на чётных местах, умножаются на 2.
# 4. Если в результате такого умножения возникает число больше 9,
# оно заменяется суммой цифр получившегося произведения — однозначным числом, то есть цифрой.
# 5. Все полученные в результате преобразования цифры складываются. Если сумма кратна 10,
# то исходные данные верны.

print(("-") * 25 + "Task_1.Validate" + ("-") * 25)

while True:
    print("Enter 0 to stop the program")
    print("Watch out! The card number can not contain letters and spaces")
    card_number = input("Enter the card number: ")
    if card_number == "0":
        break
    elif card_number.isdigit() and " " not in card_number:
        print("The input is correct")
    else:
        print("Check that the input is correct")
    rev_card_number = card_number[::-1]
    even_number = []
    odd_number = []
    for ind in range(len(rev_card_number)):
        if ind == 0:
            odd_number.append(int(rev_card_number[ind]))
        elif ind % 2 == 0:
            odd_number.append(int(rev_card_number[ind]))
        else:
            even_number.append(int(rev_card_number[ind]) * 2)

    for symbol in range(len(even_number)):
        suma = 0
        while even_number[symbol] != 0:
            digit = even_number[symbol] % 10
            suma += digit
            even_number[symbol] //= 10
        even_number[symbol] = suma

    if (sum(even_number) + sum(odd_number)) % 10 == 0:
        print("Validate card number")
    else:
        print("Unvalidate card number")
