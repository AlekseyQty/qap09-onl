import collections
import operator

# 1. Перевести строку в массив
from operator import itemgetter

text_1 = "Robin Singh"
text_2 = "I love arrays they are my favorite"

list_text_1 = text_1.split()
print(list_text_1)

list_text_2 = text_2.split()
print(list_text_2)


# 2. Дан список: [‘Ivan’, ‘Ivanou’], и 2 строки: Minsk, Belarus
# Напечатайте текст: “Привет, Ivan Ivanou! Добро пожаловать в Minsk Belarus”

list_name = ["Ivan", "Ivanou"]
text_name = " ".join(list_name)

text_city = "Minsk"
text_country = "Belarus"

print(f"Привет, {text_name}! Добро пожаловать в {text_city} {text_country}")


# 3. Дан список ["I", "love", "arrays", "they", "are", "my", "favorite"] сделайте из него
# строку => "I love arrays they are my favorite"

list_text_3 = ["I", "love", "arrays", "they", "are", "my", "favorite"]
print(" ".join(list_text_3))


# 4. Создайте список из 10 элементов, вставьте на 3-ю позицию новое значение,
# удалите элемент из списка под индексом 6

list_4 = list(range(1, 11))
print(list_4)

list_4.insert(2, "Boris")
print(list_4)

del list_4[6]
print(list_4)


# 5. Есть 2 словаря
# a = { 'a': 1, 'b': 2, 'c': 3}
# b = { 'c': 3, 'd': 4,'e': 5}
# Необходимо их объединить по ключам, а значения ключей поместить в список,
# если у одного словаря есть ключ "а", а у другого нету, то поставить значение
# None на соответствующую позицию(1-я позиция для 1-ого словаря, вторая для
# 2-ого)
# ab = {'a': [1, None], 'b': [2, None], 'c': [3, 3], 'd': [None, 4], 'e': [None, 5]}

a = {'a': 1, 'b': 2, 'c': 3}
b = {'c': 3, 'd': 4, 'e': 5}

ab = {key: [a.get(key), b.get(key)] for key in set(a) | set(b)}
ab = dict(sorted(ab.items()))
print(f"ab = {ab}")


# *1) Вам передан массив чисел. Известно, что каждое число в этом массиве имеет
# пару, кроме одного: [1, 5, 2, 9, 2, 9, 1] => 5
# Напишите программу, которая будет выводить уникальное число


list_numbers = [1, 5, 2, 9, 2, 9, 1]
list_frequency = collections.Counter(list_numbers)
rare_numb = list_frequency.most_common()[:-2:-1]
(c, d) = rare_numb[0]
print(f"Уникальное число - {c}")


# *2) Дан текст, который содержит различные английские буквы и знаки препинания. Вам
# необходимо найти самую частую букву в тексте. Результатом должна быть буква в
# нижнем регистре.

rand_text = "27 403 – Twenty-seven ThouSand, foUr hunndddRed and tHree."

text_low = rand_text.lower()   # меняем в тексте все буквы на строчные
text_list = list(text_low)   # т.к. строки неизменяемый тип данных - преобразуем строку в лист

# Удаляем все символы которые не являются буквами алфавита
# What does Isalpha () do in Python?
# The isalpha() method returns True if all the characters are alphabet letters (a-z).
list_alphabet_letters = [i for i in text_list if i.isalpha() is True]
# print(list_alphabet_letters)  # list

letters_count = collections.Counter(list_alphabet_letters)  # кол-во одинаковых букв в тексте
# print(letters_count)  # словарь

letters_count_tup = dict.items(letters_count)  # преобразуем словарь в массив кортежей
# print(letters_count_tup)  # массив кортежей

letters_count_tup_sort = sorted(letters_count_tup, key=itemgetter(1, 0))  # сортируем массив по 2-ум параметрам кортежа
# print(letters_count_tup_sort)  # упорядоченный массив кортежей

list_letters = dict(letters_count_tup_sort)  # массив кортежей преобразуем в словарь
# print(list_letters)

find_letter = max(list_letters, key=list_letters.get)
print(f"Самая частая буква в тексте - {find_letter}")




