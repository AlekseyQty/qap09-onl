# Шифр Цезаря (the Caesar cipher) — один из древнейших шифров. При шифровании каждый символ заменяется другим,
# отстоящим от него в алфавите на фиксированное число позиций.
# Мое условие: сдвиг (при шифровании/дешифровании) может быть как положительным так и отрицательным, учитывала язык
# шифрования (русский/английский), только в русском языке игнорировала буквы Ё,ё.
# print(ord("ё"), ord("Ё"))  # 1105, 1025

def code_russian_text_pos_shift(my_string, shift):
    """This function is
        encoding a russian text with upper and lower letters in the case shift > 0 (positive shift).
        decoding a russian text with upper and lower letters in the case shift > 0."""
    new_string = ""
    russian_lower_letters = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'  # ignoring the letter ё
    russian_upper_letters = 'АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'  # ignoring the letter Ё
    for i in range(len(my_string)):  # choice each word
        for char in my_string[i]:  # check for each symbol in each word
            if char.isalpha():
                if char in russian_lower_letters:  # only Russian lower letters
                    if ord(char) + shift > 1103:  # [1072-1103]
                        new_string += chr(ord(char) + shift - 32)
                    else:
                        new_string += chr(ord(char) + shift)
                elif char in russian_upper_letters:  # only Russian upper letters
                    if ord(char) + shift > 1071:  # [1040-1071]
                        new_string += chr(ord(char) + shift - 32)
                    else:
                        new_string += chr(ord(char) + shift)
                else:
                    new_string += char  # add any letters which they are no russian letters
            else:
                new_string += char  # add any symbols which they aren't letters

        new_string += ' '  # add spaces between the words
    return new_string  # return result string after encoding/decoding with shift >0


def code_russian_text_neg_shift(my_string, shift):
    """This function is
        decoding a russian text with upper and lower letters in the case shift < 0 (negative shift).
        encoding a russian text with upper and lower letters in the case shift < 0."""
    new_string = ""
    russian_lower_letters = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'  # ignoring the letter ё
    russian_upper_letters = 'АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'  # ignoring the letter Ё

    for i in range(len(my_string)):  # choice each word
        for char in my_string[i]:  # check for each symbol in each word
            if char.isalpha():
                if char in russian_lower_letters:  # only Russian lower letters
                    if ord(char) - abs(shift) < 1072:  # [1072-1103]
                        new_string += chr(ord(char) - abs(shift) + 32)
                    else:
                        new_string += chr(ord(char) - abs(shift))
                elif char in russian_upper_letters:  # only Russian upper letters
                    if ord(char) - abs(shift) < 1040:  # [1040-1071]
                        new_string += chr(ord(char) - abs(shift) + 32)
                    else:
                        new_string += chr(ord(char) - abs(shift))

                else:
                    new_string += char  # add any letters which they are no russian letters
            else:
                new_string += char  # add any symbols which they aren't letters

        new_string += ' '  # add spaces between the words
    return new_string  # return result string after encoding/decoding with shift <0


def code_english_text_pos_shift(my_string, shift):
    """This function is
    encoding an english text with upper and lower letters in the case shift > 0 (positive shift).
    decoding an english text with upper and lower letters in the case shift > 0."""
    new_string = ""
    english_lower_letters = 'abcdefghijklmnopqrstuvwxyz'
    english_upper_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    for i in range(len(my_string)):  # choice each word
        for char in my_string[i]:  # check for each symbol in each word
            if char.isalpha():
                if char in english_lower_letters:  # only English lower letters
                    if ord(char) + shift > 122:  # [97-122]
                        new_string += chr(ord(char) + shift - 26)
                    else:
                        new_string += chr(ord(char) + shift)

                elif char in english_upper_letters:  # only English upper letters
                    if ord(char) + shift > 90:  # [65-90]
                        new_string += chr(ord(char) + shift - 26)
                    else:
                        new_string += chr(ord(char) + shift)
                else:
                    new_string += char  # add any letters which they are no english letters
            else:
                new_string += char  # add any symbols which they aren't letters

        new_string += ' '  # add spaces between the words
    return new_string  # return result string after encoding/decoding with shift >0


def code_english_text_neg_shift(my_string, shift):
    """This function is
    decoding an english text with upper and lower letters in the case shift < 0 (negative shift).
    encoding an english text with upper and lower letters in the case shift < 0."""
    new_string = ""
    english_lower_letters = 'abcdefghijklmnopqrstuvwxyz'
    english_upper_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    for i in range(len(my_string)):  # choice each word
        for char in my_string[i]:  # check for each symbol in each word
            if char.isalpha():
                if char in english_lower_letters:  # only English lower letters
                    if ord(char) - abs(shift) < 97:  # [97-122]
                        new_string += chr(ord(char) - abs(shift) + 26)
                    else:
                        new_string += chr(ord(char) - abs(shift))
                elif char in english_upper_letters:  # only English upper letters
                    if ord(char) - abs(shift) < 65:  # [65-90]
                        new_string += chr(ord(char) - abs(shift) + 26)
                    else:
                        new_string += chr(ord(char) - abs(shift))
                else:
                    new_string += char  # add any letters which they are no english letters
            else:
                new_string += char  # add any symbols which they aren't letters

        new_string += ' '   # add spaces between the words
    return new_string  # return result string after encoding/decoding with shift <0


try:
    text = input("Enter any text which you want to decode/encode: ").split()
    language = input("Enter the decode/encode English/Russian language (eng/ru): ")
    act = input("Enter the action: 1: encode English text, 2: decode English text, "
                "3: encode Russian text, 4: decode Russian text: ")

    code_shift = int(input("Enter the positive or negative integer number - the encode/decode key (shift): "
                           "for English text  1 <= |shift| < 26, "
                           "for Russian text  1 <= |shift| < 32: "))
    if language == "ru":
        if not (1 <= abs(code_shift) < 32):
            print("You have entered the wrong encode/decode shift or encode/decode language.")
            exit()
    elif language == "eng":
        if not (1 <= abs(code_shift) < 26):
            print("You have entered the wrong encode/decode shift or encode/decode language.")
            exit()
    else:
        print("Wrong language. You can use only English or Russian encode/decode language.")
        exit()

    if code_shift > 0:
        actions_positive_shift = {"1": code_english_text_pos_shift(text, code_shift),  # encode eng text for shift>0
                                  "2": code_english_text_pos_shift(text, code_shift),  # decode eng text for shift>0
                                  "3": code_russian_text_pos_shift(text, code_shift),  # encode ru text for shift>0
                                  "4": code_russian_text_pos_shift(text, code_shift)}  # decode ru text for shift>0

        result_text1 = actions_positive_shift.get(act, "No this action.")
        if result_text1.split() == text or result_text1 == "No this action.":
            print("Your text hasn't been encoded/decoded. "
                  "Check a choice of the correct action or check the input of English or Russian text. ")
        else:
            print(result_text1)

    else:
        actions_negative_shift = {"1": code_english_text_neg_shift(text, code_shift),  # encode eng text for shift<0
                                  "2": code_english_text_neg_shift(text, code_shift),  # decode eng text for shift<0
                                  "3": code_russian_text_neg_shift(text, code_shift),  # encode ru text for shift<0
                                  "4": code_russian_text_neg_shift(text, code_shift)}  # decode ru text for shift<0

        result_text2 = actions_negative_shift.get(act, "No this action.")
        if result_text2.split() == text or result_text2 == "No this action.":
            print("Your text hasn't been encoded/decoded. "
                  "Check a choice of the correct action or check the input of English or Russian text. ")
        else:
            print(result_text2)

except ValueError:
    print("It isn't the integer number.")
