#                       Подсчет количества букв
# На вход подается строка, например, "cccbba" результат работы программы - строка “c3b2a"
# Примеры для проверки работоспособности:
# "cccbba" == "c3b2a"
# "abeehhhhhccced" == "abe2h5c3ed"
# "aaabbceedd" == "a3b2ce2d2"
# "abcde" == "abcde"
def function(a):
    my_list = []
    new_list = []
    for i in a:
        my_list.append(i)
    print(my_list)
    for i in range((len(my_list) - 1)):
        sum = 1
        if my_list[i - 1] == my_list[i]:
            continue
        for a in range((i + 1), len(my_list)):
            if my_list[i] == my_list[a]:
                sum += 1
            else:
                new_list.append(my_list[i])
                if sum > 1:
                    new_list.append(str(sum))
                break
    return print(''.join(new_list))


# a = str(input("Введите слово "))
a = "abeehhhhhccced"
function(a)
