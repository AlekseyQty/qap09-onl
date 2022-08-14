# Напишите генератор который принимает список numbers = [34.6, -203.4, 44.9, 68.3, -12.2, 44.6, 12.7]
# и возвращает новый список только с положительными числами

print(("-") * 25 + "Generator_1" + ("-") * 25)


def positive_number(numbers):
    pos_number = []
    for el in numbers:
        if el > 0:
            pos_number.append(el)
    yield pos_number


result = positive_number([34.6, -203.4, 44.9, 68.3, -12.2, 44.6, 12.7])
print("Generator_1:", type(result), next(result))


# Необходимо составить список чисел которые указывают на длину слов в строке:
# sentence = "the quick brown fox jumps over the lazy dog", но только если слово не "the".

print(("-") * 25 + "Generator_2.Option_1" + ("-") * 25)

sentence = "the quick brown fox jumps over the lazy dog"
list_sentence = sentence.split()
list_number = []
for word in list_sentence:
    if word == "the":
        list_number.append(word)
    else:
        list_number.append(int(len(word)))

print("Generator_2.Option_1:", type(list_number), list_number)


print(("-") * 25 + "Generator_2.Option_2" + ("-") * 25)

sentence = "the quick brown fox jumps over the lazy dog"
list_number = [word if word == "the" else len(word) for word in sentence.split()]
print("Generator_2.Option_2:", type(list_number), list_number)


# Шифр Цезаря — один из древнейших шифров. При шифровании каждый символ заменяется другим,
# отстоящим от него в алфавите на фиксированное число позиций
# Примеры:
# hello world! -> khoor zruog!
# this is a test string -> ymnx nx f yjxy xywnsl

print(("-") * 25 + "Сaesar_Сipher" + ("-") * 25)

while True:
    print("Enter 0 to stop the program")
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    my_text = input("Enter you text for coding: ")
    if my_text == "0":
        break
    shift = int(input("Enter a shift (number from 1 to 25): "))
    my_text = my_text.lower()
    encode_text = " "
    for letter in my_text:
        index = alphabet.find(letter)
        new_index = index + shift
        if letter in alphabet:
            encode_text += alphabet[new_index]
        else:
            encode_text += letter

    print("Сaesar_Сipher:", encode_text)
