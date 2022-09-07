print(f'{"̅" * 26}{"̅" * 26}')
print(f'{" " * 20}  THIRD TASK {" " * 20}')
print(f'{" " * 20} Caesar cipher  {" " * 20}')
print(f'{"̅" * 26}{"̅" * 26}')
"""
Шифр Цезаря — один из древнейших шифров. 
При шифровании каждый символ заменяется другим, отстоящим от него в алфавите на фиксированное число позиций.
Примеры:
hello world! -> khoor zruog!
this is a test string -> ymnx nx f yjxy xywnsl

Напишите две функции - encode и decode принимающие как параметр строку и число - сдвиг.

"""
text_encrypt = input('Enter your text to encrypt: ').lower()
text_decrypt = input('Enter your text to decrypt: ').lower()
key_crypt = int(input('Enter your crypt key: '))


# Encode only for Latin alphabet
def encode(text_encrypt, key_crypt):
    result = []
    key_dict = ''
    dictionary = 'abcdefghijklmnopqrstuvwxyz'
    for letter in range(len(text_encrypt)):
        if text_encrypt[letter] in dictionary:
            key_dict = dictionary
        else:
            result.append(text_encrypt[letter])

        if text_encrypt[letter] in key_dict:
            for symbol in range(len(key_dict)):
                if (symbol + key_crypt) < len(key_dict) and text_encrypt[letter] == key_dict[symbol]:
                    result.append(key_dict[(symbol + key_crypt)])
                elif (symbol + key_crypt) >= len(key_dict) and text_encrypt[letter] == key_dict[symbol]:
                    result.append(key_dict[symbol - len(key_dict) + key_crypt])
    return ''.join(result)


# Decode only for Latin alphabet
def decode(text_decrypt, key_crypt):
    result = []
    key_dict = ''
    dictionary = 'abcdefghijklmnopqrstuvwxyz'
    for letter in range(len(text_decrypt)):
        if text_decrypt[letter] in dictionary:
            key_dict = dictionary
        else:
            result.append(text_decrypt[letter])

        if text_decrypt[letter] in key_dict:
            for symbol in range(len(key_dict)):
                if (symbol - key_crypt) < len(key_dict) and text_decrypt[letter] == key_dict[symbol]:
                    result.append(key_dict[(symbol - key_crypt)])
                elif (symbol - key_crypt) >= len(key_dict) and text_decrypt[letter] == key_dict[symbol]:
                    result.append(key_dict[symbol - len(key_dict) - key_crypt])

    return ''.join(result)


print(encode(text_encrypt, key_crypt))
print(decode(text_decrypt, key_crypt))

print(f'{"̅" * 26}{"̅" * 26}')
