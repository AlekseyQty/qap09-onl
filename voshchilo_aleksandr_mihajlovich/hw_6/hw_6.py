# 1. Validate

def get_user_in():
    """
    Сheck of input for digits only
    """
    while True:
        user_in_card = input('Введите номер карты: ')
        if user_in_card.isdigit():
            return user_in_card


user_in = get_user_in()
list_user_in = [int(i) for i in str(user_in)]
list_user_in_rev = list_user_in[::-1]


def numb_sum(i):
    """
    This function calculates the sum of numbers in product
    """
    list_i = i * 2
    list_i2 = [int(j) for j in str(list_i)]
    sum_prod = list_i2[0] + list_i2[1]
    return sum_prod


check_list = []

for i in enumerate(list_user_in_rev):
    if i[0] % 2 != 0:
        if i[1] * 2 > 9:
            check_list.append(numb_sum(i[1]))
        else:
            check_list.append(i[1] * 2)
    else:
        check_list.append(i[1])


if sum(check_list) % 10 == 0:
    print("Исходная последовательность корректна")
else:
    print("Исходная последовательность некорректна")


# 2. Подсчет количества букв

def get_user_in_text():
    """
    Сheck of input for letters only
    """
    while True:
        user_in_text = input('Введите строку: ')
        if user_in_text.isalpha():
            return user_in_text


user_in = get_user_in_text()
# из-за примера "abeehhhhhccced" == "abe2h5c3ed" вижу вариант только перебирать каждый элемент
# остальные примеры подходят под "from collections import Counter"
repeat = 1
result = ""

for i in range(len(user_in)):
    if i == len(user_in) - 1 and repeat != 1:
        result += user_in[i] + str(repeat)
    elif i == len(user_in) - 1 and repeat == 1:
        result += user_in[i]
    elif user_in[i] == user_in[i + 1]:
        repeat += 1
    elif repeat == 1:
        result += user_in[i]
    else:
        result += user_in[i] + str(repeat)
        repeat = 1
print(result)


# 3. Простейший калькулятор v0.1

def sum_in(a, b):
    sum_round = round(a + b, 1)
    break_sum = str(sum_round).split(".")
    print(f"Частное: {break_sum[0]}, Остаток: {break_sum[1]}")


def sub_in(a, b):
    sub_round = round(a - b, 1)
    break_sub = str(sub_round).split(".")
    print(f"Частное: {break_sub[0]}, Остаток: {break_sub[1]}")


def mult_in(a, b):
    mult_round = round(a * b, 1)
    break_mult = str(mult_round).split(".")
    print(f"Частное: {break_mult[0]}, Остаток: {break_mult[1]}")


def div_in(a, b):
    div_round = round(a / b, 1)
    break_div = str(div_round).split(".")
    print(f"Частное: {break_div[0]}, Остаток: {break_div[1]}")


print("1. Сложение \n2. Вычитание \n3. Умножение \n4. Деление \n")
operation_input = int(input("Выберите операцию (номер):"))

if operation_input == 1:
    first_numb = float(input("Введите первое число:"))
    second_numb = float(input("Введите второе число:"))
    print(sum_in(first_numb, second_numb))
elif operation_input == 2:
    first_numb = float(input("Введите первое число:"))
    second_numb = float(input("Введите второе число:"))
    print(sub_in(first_numb, second_numb))
elif operation_input == 3:
    first_numb = float(input("Введите первое число:"))
    second_numb = float(input("Введите второе число:"))
    print(mult_in(first_numb, second_numb))
elif operation_input == 4:
    first_numb = float(input("Введите первое число:"))
    second_numb = float(input("Введите второе число:"))
    if second_numb == 0:
        print("Деление на 0!!!")
    else:
        print(div_in(first_numb, second_numb))


