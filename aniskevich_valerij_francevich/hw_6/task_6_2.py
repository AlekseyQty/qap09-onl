#                       Подсчет количества букв
# На вход подается строка, например, "cccbba" результат работы программы - строка “c3b2a"
# Примеры для проверки работоспособности:
# "cccbba" == "c3b2a"
# "abeehhhhhccced" == "abe2h5c3ed"
# "aaabbceedd" == "a3b2ce2d2"
# "abcde" == "abcde"
# "aaabbdefffff" == "a3b2def5"

def function(my_string):
    my_list = []
    new_list = []
    for i in my_string:
        my_list.append(i)
    for el in range(len(my_list)):
        sum = 1
        if el > 0 and my_list[el] == my_list[el - 1]:
            continue
        else:
            new_list.append(my_list[el])
        for i in range(el, (len(my_list) - 1)):
            if my_list[i] == my_list[i + 1]:
                sum += 1
                if sum > 1 and i == (len(my_list) - 2):
                    new_list.append(str(sum))
                continue
            else:
                if sum > 1:
                    new_list.append(str(sum))
                break
    return print(''.join(new_list))


a = str(input("Введите текст "))
function(a)
