# 1Перевести строку в массив
# "Robin Singh" => ["Robin”, “Singh"]
# "I love arrays they are my favorite" => ["I", "love", "arrays", "they", "are", "my",
# "favorite"]
my_string = ("Robin Singh")
my_string2 = ("I love arrays they are my favorite")
my_list = my_string.split()
my_list2 = my_string2.split()
print(my_list)
print(my_list2)

# 2Дан список: [‘Ivan’, ‘Ivanou’], и 2 строки: Minsk, Belarus
# Напечатайте текст: “Привет, Ivan Ivanou! Добро пожаловать в Minsk Belarus”
new_list = ["Ivan", "Ivanou"]
string_Minsk = ("Minsk")
string_Belarus = ("Belarus")
print(f"Привет, {new_list[0]} {new_list[1]}! Добро пожаловать в {string_Minsk} {string_Belarus}")

# 3Дан список ["I", "love", "arrays", "they", "are", "my", "favorite"] сделайте из него
# строку => "I love arrays they are my favorite"
three_list = ["I", "love", "arrays", "they", "are", "my", "favorite"]
new_string = ' '.join(three_list)
print(new_string)

# 4Создайте список из 10 элементов, вставьте на 3-ю позицию новое значение,
# удалите элемент из списка под индексом 6
four_list = ["4", "17", "3", "11", "31", "43", "47", "22", "65", "84"]
four_list.insert(2, "77")
del four_list[6]
print(four_list)
