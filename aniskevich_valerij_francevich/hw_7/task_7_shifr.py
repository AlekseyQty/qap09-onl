# Шифр цезаря
# Шифр Цезаря — один из древнейших шифров. При шифровании каждый символ
# заменяется другим, отстоящим от него в алфавите на фиксированное число позиций.
# Примеры:
# hello world! -> khoor zruog!
# this is a test string -> ymnx nx f yjxy xywnsl
# Напишите две функции - encode и decode принимающие как параметр строку и число -
# сдвиг.
while True:
    encode_or_decodr = int(input("Выберите операцию\n1 - decode \n2 - encode\n"))
    if encode_or_decodr == 1 or encode_or_decodr == 2:
        break
    else:
        print("Неправильный ввод, попробуйте снова")
alfavit = ("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
s = str(input("Введите текст для шифра "))
my_string = s.upper()
sdvig = int(input("Введите число-сдвиг "))
decode_list = []
encode_list = []


def decode(my_string: str, sdvig: int):
    for i in my_string:
        a = alfavit.find(i)
        if a == -1:
            decode_list.append(i)
        else:
            if (a + sdvig) > 25:
                a = a - 26
            decode_list.append(alfavit[a + sdvig])
        decode_string = ''.join(decode_list)
    return decode_string


def encode(my_string: str, sdvig: int):
    for i in my_string:
        a = alfavit.find(i)
        if a == -1:
            encode_list.append(i)
        else:
            encode_list.append(alfavit[a - sdvig])
        encode_string = ''.join(encode_list)
    return encode_string


if encode_or_decodr == 1:
    print(decode(my_string, sdvig))
else:
    print(encode(my_string, sdvig))
