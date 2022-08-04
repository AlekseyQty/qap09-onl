"""
2 Подсчет количества букв
На вход подается строка, например, "cccbba" результат работы программы - строка “c3b2a"
Примеры для проверки работоспособности:
"cccbba" == "c3b2a"
"abeehhhhhccced" == "abe2h5c3ed"
"aaabbceedd" == "a3b2ce2d2"
"abcde" == "abcde"
"aaabbdefffff" == "a3b2def5"
"""


def element_count():
    string_input = input('Введите текст для подсчёта элементов: ')
    string_add = []
    for let in set(string_input):
        string_add.append(let)
        if string_input.count(let) > 1:
            string_add.append(string_input.count(let))
    print(''.join(map(str, string_add)))


element_count()
