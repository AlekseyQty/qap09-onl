#Перевести строку в массив
# "Robin Singh" => ["Robin”, “Singh"]
# "I love arrays they are my favorite" => ["I", "love", "arrays", "they", "are", "my","favorite"]
string = 'Robin Singh'
arr = string.split()
print(arr)

string_2 = 'I love arrays they are my favorite'
arr_2 = string_2.split()
print(arr_2)

#Дан список: [‘Ivan’, ‘Ivanou’], и 2 строки: Minsk, Belarus
# Напечатайте текст: “Привет, Ivan Ivanou! Добро пожаловать в Minsk Belarus”
name = ['Ivan', 'Ivanou']
city = 'Minsk'
country = 'Belarus'
fullname = (" ".join(name))
print(f'"Привет,{fullname}! Добро пожаловать в {city} {country}"')


#Дан список ["I", "love", "arrays", "they", "are", "my", "favorite"]
# сделайте из него строку => "I love arrays they are my favorite"
my_arr = ["I", "love", "arrays", "they", "are", "my", "favorite"]
unpack = (" ".join(my_arr))
print(f"\"{unpack}\"")

#Создайте список из 10 элементов, вставьте на 3-ю позицию новое значение,
# удалите элемент из списка под индексом 6
my_arr2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
my_arr2[3] = 20
removed = my_arr2.pop(6)
print(my_arr2)
