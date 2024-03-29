# 1.Validate
# Ваша задача написать программу, принимающее число - номер кредитной карты(число
# может быть четным или не четным). И проверяющей может ли такая карта существовать.
# Предусмотреть защиту от ввода букв, пустой строки и т.д.
def validate(a):
    '''
    Функция проверят правильность ввода номера кредитной карты по Алгоритму Луна
    :param a: номер кредитной карты, который вводится с консоли
    :return: результат проверки
    '''
    if not len(str(a)) == 16:
        return print("Ошибка: неверное количество символов")
    my_list = []
    for i in str(a):
        i = int(i)
        my_list.append(i)
    for i in range(0, 16, 2):
        if my_list[i] * 2 < 10:
            my_list[i] = my_list[i] * 2
        else:
            my_list[i] = (my_list[i] * 2) - 9
    sum = 0
    for i in my_list:
        sum = sum + i
    if sum % 10 == 0:
        return print("Выполено! Спасибо!")
    return print("Неверный ввод!")


a = int(input("Введите номер кредитной карты без пробелов "))

validate(a)

# для примера: 4234567890123456
