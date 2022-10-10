# Шифр цезаря
# Шифр Цезаря — один из древнейших шифров. При шифровании каждый символ
# заменяется другим, отстоящим от него в алфавите на фиксированное число позиций.
# Примеры:
# hello world! -> khoor zruog!
# this is a test string -> ymnx nx f yjxy xywnsl

while True:
    print("Enter 'stop' to stop the program")
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ"
    text_for_coding = input("Enter you text for coding: ")
    if text_for_coding == "stop":
        break
    shift = int(input("Enter a shift number: "))
    text_for_coding = text_for_coding.upper()
    encode_text = " "
    for letter in text_for_coding:
        index = alphabet.find(letter)
        new_index = index + shift
        if letter in alphabet:
            encode_text += alphabet[new_index]
        else:
            encode_text += letter

    print(encode_text)
