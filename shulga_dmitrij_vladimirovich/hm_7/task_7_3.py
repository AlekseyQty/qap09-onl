# Шифр цезаря

import string

def encode(encode_word):
    encode_list = []
    count = 0
    for x in range(len(encode_word)):
        if encode_word[x] in my_alphabet:
            for i in range(len(my_alphabet)):
                if my_alphabet[i] == encode_word[x]:
                    if my_alphabet[i] not in my_alphabet[-shear_step:]:
                        encode_list.append(my_alphabet[i + shear_step])
                    elif my_alphabet[i] == my_alphabet[-shear_step - 1]:
                        encode_list.append(my_alphabet[i + shear_step])
                    elif my_alphabet[i] == my_alphabet[-shear_step]:
                        encode_list.append(my_alphabet[0])
                    elif my_alphabet[i] > my_alphabet[-shear_step]:
                        count = i - (26 - shear_step)
                        encode_list.append(my_alphabet[count])

        elif encode_word[x] == " ":
            encode_list.append(" ")
        else:
            encode_list.append(encode_word[x])

    encode_finish = " ".join(encode_list)
    print(encode_finish)

my_alphabet = list(string.ascii_lowercase)
print(my_alphabet)

my_word = ""
shear_step = ""
while my_word != "quit" or shear_step != "quit":
    my_word = input("Введите слово для шифрования: ")
    encode_word = my_word[::]

    if my_word == "quit":
        print("Goodbye")
        break

    shear_step = input("Введите шаг: ")
    if shear_step == "quit":
        print("Goodbye")
        break
    else:
        shear_step = int(shear_step)

        encode(encode_word)

