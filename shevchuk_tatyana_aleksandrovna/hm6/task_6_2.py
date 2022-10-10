# 2 Подсчет количества букв
# На вход подается строка, например, "cccbba" результат работы программы - строка “c3b2a"
# Примеры для проверки работоспособности:
# "cccbba" == "c3b2a"
# "abeehhhhhccced" == "abe2h5c3ed"
# "aaabbceedd" == "a3b2ce2d2"
# "abcde" == "abcde"
# "aaabbdefffff" == "a3b2def5"

def count_letter(my_string):
    for i in range(len(my_string)):
        if my_string[i] not in my_string[:i]:
            if my_string.count(my_string[i]) == 1:
                print(my_string[i], sep="", end="")
            else:
                print(my_string[i], my_string.count(my_string[i]), sep="", end="")


count_letter("aaabbceedd")
