def encode(string, number):
    """Функция для кодирования строки с указанным сдвигом"""
    for char in string:
        if char.isalpha():
            print(chr(ord(char) + number), end='')
        else:
            print(char, end='')


def decode(string, number):
    """Функция для расшифровки строки с указанным сдвигом"""
    for char in string:
        if char.isalpha():
            print(chr(ord(char) - number), end='')
        else:
            print(char, end='')


encode("hello world!", 3)
print()
decode("khoor zruog!", 3)
