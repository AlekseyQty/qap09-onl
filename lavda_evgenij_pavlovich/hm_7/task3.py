"""Шифр Цезаря — один из древнейших шифров. При шифровании каждый символ
заменяется другим, отстоящим от него в алфавите на фиксированное число позиций."""

text = input("Введите текст, который хотите зашифровавать: ")
text1 = input("Введите текст, который хотите ра""засшифровавать: ")


def encode(user):
    res, n = [], ""
    dictionary, dictionary_upper = "abcdefghijklmnopqrstuvwxyz", "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    for i in range(len(user)):
        if user[i] in dictionary:
            n = dictionary
        elif user[i] in dictionary_upper:
            n = dictionary_upper
        else:
            res.append(user[i])

        if user[i] in n:
            for j in range(len(n)):
                if 0 <= j + 3 < len(n) and user[i] == n[j]:
                    res.append(n[j + 3])
                elif j + 3 >= len(n) and user[i] == n[j]:
                    res.append(n[(1 - j - 3) % (len(n) - 1)])
                elif j + 3 < 0 and user[i] == n[j]:

                    res.append(n[(j + 3) % len(n)])

    return ''.join(res)


def deencode(user):
    res, n = [], ""
    dictionary, dictionary_upper = "abcdefghijklmnopqrstuvwxyz", "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    for i in range(len(user)):
        if user[i] in dictionary:
            n = dictionary
        elif user[i] in dictionary_upper:
            n = dictionary_upper
        else:
            res.append(user[i])

        if user[i] in n:
            for j in range(len(n)):
                if 0 <= j + 3 < len(n) and user[i] == n[j]:
                    res.append(n[j - 3])
                elif j + 3 >= len(n) and user[i] == n[j]:
                    res.append(n[(1 - j - 3) % (len(n) - 1)])
                elif j + 3 < 0 and user[i] == n[j]:

                    res.append(n[(j - 3) % len(n)])

    return ''.join(res)


print(encode(text))
print(deencode(text1))
