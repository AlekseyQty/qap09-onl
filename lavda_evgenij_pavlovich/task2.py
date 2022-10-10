"""На вход подается строка, например, "cccbba" результат работы программы - строка “c3b2a"""


def get_cher_count():
    a = input('Введи что-нибудь: ')
    string = []
    for element in set(a):
        string.append(element)
        string.append(a.count(element))

    print("".join(map(str, string)))


get_cher_count()
