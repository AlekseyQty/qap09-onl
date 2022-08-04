# 1Перевести строку в массив
# "Robin Singh" => ["Robin”, “Singh"]
# "I love arrays they are my favorite" => ["I", "love", "arrays", "they", "are", "my",
# "favorite"]

string1 = ("Robin Singh")
print(string1)
array1 = ["Robin", "Singh"]
print(array1)
string2 = "I love arrays they are my favorite"
print(string2)
array2 = ["I", "love", "arrays", "they", "are", "my", "favorite"]
print(array2)

# 2 Дан список: [‘Ivan’, ‘Ivanou’], и 2 строки: Minsk, Belarus
# Напечатайте текст: “Привет, Ivan Ivanou! Добро пожаловать в Minsk Belarus”
array3 = ["Ivan", "Ivanov"]
string3 = ("Minsk")
string4 = ("Belarus")
print(" ".join(array3) + " " + "Welcome to" + " " + string3 + " " + string4)

# 3Дан список ["I", "love", "arrays", "they", "are", "my", "favorite"] сделайте из него
# строку => "I love arrays they are my favorite"
new_array = ["I", "love", "arrays", "they", "are", "my", "favorite"]
print(" ".join(new_array))

# 4Создайте список из 10 элементов, вставьте на 3-ю позицию новое значение,
# удалите элемент из списка под индексом 6

new_array2 = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]
print(new_array2)
new_array2.insert(2, "new")
print(new_array2)
del new_array2[6]
print(new_array2)

# 5Есть 2 словаря
# a = { 'a': 1, 'b': 2, 'c': 3}
# b = { 'c': 3, 'd': 4,'e': 5}
# Необходимо их объединить по ключам, а значения ключей поместить в список,
# если у одного словаря есть ключ "а", а у другого нету, то поставить значение
# None на соответствующую позицию(1-я позиция для 1-ого словаря, вторая для
# 2-ого)
# ab = {'a': [1, None], 'b': [2, None], 'c': [3, 3], 'd': [None, 4], 'e': [None, 5]}

a = {'a': 1, 'b': 2, 'c': 3}
b = {'c': 3, 'd': 4, 'e': 5}
ab = {**a, **b}

for key in ab.keys():
    ab[key] = [a.get(key), b.get(key)]
print(ab)