# 1.Validate
# Ваша задача написать программу, принимающее число - номер кредитной карты(число
# может быть четным или не четным). И проверяющей может ли такая карта существовать.
# Предусмотреть защиту от ввода букв, пустой строки и т.д.
# Примечания


def Luna(card):
    sum = 0
    cardnumbers = list(map(int, card))
    for count, num in enumerate(cardnumbers):
        if count % 2 == 0:
            sum2 = num * 2
            if sum2 > 9:
                sum2 -= 9
            sum += sum2
        else:
            sum += num
    return sum % 10 ==0
print(Luna("4111111111111111"))
print(Luna("3530111333300000"))
print(Luna("4012888888881881"))
print(Luna("378282246310005"))


# 2 Подсчет количества букв
# На вход подается строка, например, "cccbba" результат работы программы - строка “c3b2a"
# Примеры для проверки работоспособности:
# "cccbba" == "c3b2a"
# "abeehhhhhccced" == "abe2h5c3ed"
# "aaabbceedd" == "a3b2ce2d2"
# "abcde" == "abcde"
# "aaabbdefffff" == "a3b2def5"


my_string = input("Введите слово с повторяющимися буквами")
my_string2 = my_string[:1]
count_1 = 1
result = " "

for i in my_string[1:]:
    if i != my_string2:
        result += (my_string2 + str(count_1))
        my_string2 = i
        count_1 = 1
    else:
        count_1 += 1
result += (my_string2 + str(count_1))
print(my_string, result)


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

action = input("Введите дейсвтие которое хотите выполнить:(+,-,*,/)")
first_num = input("Введите первое число:")
two_num = input("Введите второе число:")
resoult = ()
if int(first_num) + int(two_num):
    resoult = int(first_num) + int(two_num)
elif int(first_num) - int(two_num):
    resoult = int(first_num) - int(two_num)
elif int(first_num) / int(two_num):
    resoult = int(first_num) / int(two_num)
elif int(first_num) * int(two_num):
    resoult = int(first_num) * int(two_num)
else:
    print("Выбрано не верное действие")
print(resoult)