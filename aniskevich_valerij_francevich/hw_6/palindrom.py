# 6) Напишите функцию, которая проверяет на то, является ли строка палиндромом или
# нет.
# Палиндром — это слово или фраза, которые одинаково читаются слева направо и
# справа налево.
def palindrom(a: str):
    str_upp = a.upper()
    str_split = str_upp.split()
    my_string = "".join(str_split)
    new_string = my_string[::-1]
    if my_string == new_string:
        return print(f"Строка '{a}' - палиндром!")
    return print(f"Строка '{a}' не является палиндромом!")


a = str(input("ВВедите слово или строку "))
palindrom(a)
