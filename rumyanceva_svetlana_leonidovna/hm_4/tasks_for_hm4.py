print("--------task1_start--------")
# HW_4 tasks 1: Перевести строку в массив "Robin Singh" => ["Robin”, “Singh"], "I love arrays they are my favorite" =>
#  ["I", "love", "arrays", "they", "are", "my", "favorite"]

print(f"Our string/sentence consists of the next words {input('Enter any string/sentence: ').split()}.")

print("--------task1_end----------")

print("--------task2_start--------")

#  HW_4 tasks 2: Дан список: [‘Ivan’, ‘Ivanov’], и 2 строки: Minsk, Belarus.
#  Напечатайте текст: “Привет, Ivan Ivanov! Добро пожаловать в Minsk Belarus”
try:
    full_name = input("Enter space-separated first name and then last name: ").title().split()
    country_name = input("Enter any country name: ").title()
    city_name = input(f"Enter any city name, which is in {country_name}: ").title()
    print(f"Привет, {full_name[0]} {full_name[1]}! Добро пожаловать в {city_name} {country_name}.")
except IndexError:
    print("Oops! You was wrong to enter the words: space-separated first name and last name. "
          "Maybe you forgot to enter first name or last name or to put a space between them.")

print("--------task2_end----------")

print("--------task3_start--------")

#  HW_4 tasks 3:Дан список ["I", "love", "arrays", "they", "are", "my", "favorite"] сделайте из него
# строку => "I love arrays they are my favorite"

words_list = ["I", "love", "arrays", "they", "are", "my", "favorite"]
print(" ".join(words_list))

print("--------task3_end----------")

print("--------task4_start--------")

#  HW_4 tasks 4: Создайте список из 10 элементов, вставьте на 3-ю позицию новое значение,
#  удалите элемент из списка под индексом 6.
# my_array = input("Enter any 10 space-separated elements of any types: ").split()
my_array = [input("Enter one element of 10 elements: ") for _ in range(10)]
my_array.insert(3, input("Add any element in the list on position 3: "))
del my_array[6]
print(*my_array)
print("--------task4_end----------")

print("--------task5_start--------")
# HW_4 tasks 5: Есть 2 словаря a = {'a': 1, 'b': 2, 'c': 3} и b = {'c': 3, 'd': 4, 'e': 5}
# Необходимо их объединить по ключам, а значения ключей поместить в список, если у одного словаря есть ключ "а",
# а у другого нет, то поставить значение None на соответствующую позицию (1-я позиция для 1-ого словаря, вторая для
# 2-ого)  ab = {'a': [1, None], 'b': [2, None], 'c': [3, 3], 'd': [None, 4], 'e': [None, 5]}
my_dict1 = {'a': 1, 'b': 2, 'c': 3}
my_dict2 = {'c': 3, 'd': 4, 'e': 5}
result_dict = my_dict1 | my_dict2
keys_list = list(result_dict.keys())
result_dict = {}
for k in keys_list:
    if k in my_dict1 and k in my_dict2:
        result_dict[k] = [my_dict1[k], my_dict2[k]]
    elif k in my_dict1 and k not in my_dict2:
        result_dict[k] = [my_dict1[k], None]
    else:
        result_dict[k] = [None, my_dict2[k]]
print(result_dict)
print("--------task5_end--------")
