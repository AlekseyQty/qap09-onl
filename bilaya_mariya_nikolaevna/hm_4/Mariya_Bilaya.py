# Exercise_1. Перевести строку в массив
# "Robin Singh" => ["Robin”, “Singh"]
# "I love arrays they are my favorite" => ["I", "love", "arrays", "they", "are", "my", "favorite"]

print(("-" * 25) + "Exercise_1" + ("-" * 25))

str_1_1 = "Robin Singh"
array_1_1 = str_1_1.split()
print(type(str_1_1), str_1_1)
print(type(array_1_1), array_1_1)

str_1_2 = "I love arrays they are my favorite"
array_1_2 = str_1_2.split()
print(type(str_1_2), str_1_2)
print(type(array_1_2), array_1_2)


# Exercise_2. Дан список: ["Ivan", "Ivanou"], и 2 строки: Minsk, Belarus. Напечатайте текст:
# "Привет, Ivan Ivanou! Добро пожаловать в Minsk Belarus"

print(("-" * 25) + "Exercise_2" + ("-" * 25))

list_2_1 = ["Ivan", "Ivanou"]
str_2_1 = "Minsk"
str_2_2 = "Belarus"
index_0 = list_2_1[0]
index_1 = list_2_1[1]
print(f"Привет, {index_0} {index_1}! Добро пожаловать в {str_2_1} {str_2_2}")


# Exercise_3. Дан список ["I", "love", "arrays", "they", "are", "my", "favorite"]. Сделайте
# из него строку => "I love arrays they are my favorite"

print(("-" * 25) + "Exercise_3" + ("-" * 25))

list_3 = ["I", "love", "arrays", "they", "are", "my", "favorite"]
list_3_copy = list_3.copy()
print(id(list_3), list_3)
print(id(list_3_copy), list_3_copy)
print(" ".join(list_3_copy))


# Exercise_4. Создайте список из 10 элементов, вставьте на 3-ю позицию новое значение,
# удалите элемент из списка под индексом 6

print(("-" * 25) + "Exercise_4" + ("-" * 25))

list_4 = list(["cherry", 7, "apple", "onion", "garlic", 0.2, 3, "grape", "orange", "melon"])
list_4_copy = list_4.copy()
print(id(list_4), list_4)
print(id(list_4_copy), list_4_copy, len(list_4_copy))
list_4_copy.insert(2, "cat")
del list_4_copy[6]
print(list_4_copy)

# Есть 2 словаря a = { 'a': 1, 'b': 2, 'c': 3} и b = { 'c': 3, 'd': 4,'e': 5}.
# Необходимо их объединить по ключам, а значения ключей поместить в список. Если у одного словаря
# есть ключ "а", а у другого нету, то поставить значение None на соответствующую позицию
# (1-я позиция для 1-ого словаря, вторая для 2-ого)
# ab = {'a': [1, None], 'b': [2, None], 'c': [3, 3], 'd': [None, 4], 'e': [None, 5]}

print(("-" * 25) + "Exercise_5" + ("-" * 25))

a = {"a": 1, "b": 2, "c": 3}
b = {"c": 3, "d": 4, "e": 5}
dict_ab = {**a, **b}
print(dict_ab)
for k in dict_ab.keys():
    dict_ab[k] = [a.get(k), b.get(k)]
print(dict_ab)












