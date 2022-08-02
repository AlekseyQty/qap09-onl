# Exercise_1. Заменить символ "#" на символ "/" в строке 'www.my_site.com#about'.

my_str = "www.my_site.com#about"
my_str1 = (my_str.replace("#", "/"))
print("Exercise_1:", my_str1)


# Exercise_2. Option_1. Напишитие программу, которая добавляет 'ing' к словам.

list_1 = my_str1.split(".")
print("Exercise_2_list_1:", type(list_1), list_1)
res_1 = list_1[0] + "ing"
res_2 = list_1[1] + "ing"

list_2 = list_1[-1].split("/")
print("Exercise_2_list_2:",type(list_2), list_2)
res_3 = list_2[0] + "ing"
res_4 = list_2[1] + "ing"
print("Exercise_2_option_1:", res_1, res_2, res_3, res_4)


# Exercise_2. Option_2. Напишитие программу, которая добавляет 'ing' к словам.

list_2_2 = "try to do this exercise"
split_1 = list_2_2.split(" ")
print("Exercise_2_option_2:", type(split_1), split_1)
add_1 = split_1[0] + "ing"
add_2 = split_1[1] + "ing"
add_3 = split_1[2] + "ing"
add_4 = split_1[3] + "ing"
add_5 = split_1[4] + "ing"
print("Exercise_2_option_2:", add_1, add_2, add_3, add_4, add_5)


# Exercise_2. Option_3. Напишитие программу, которая добавляет 'ing' к слову.

str_2_3 = "start"
print(f"Exercise_2_option_3:", (str_2_3) + "ing")


# Exercise_3. В строке "Ivanou Ivan" поменяйте местами слова => "Ivan Ivanou".

my_list = "Ivanou Ivan"
print("Exercise_3:", type(my_list), my_list)
my_list_1 = my_list.split(" ")
print("Exercise_3:", type(my_list_1), my_list_1)
last_name = my_list_1[0]
first_name = my_list_1[1]
print("Exercise_3:", first_name + " " + last_name)


# Exercise_4. Напишите программу, которая удаляет пробел в начале и конце строки.

str_4 = " Exercise 4 "
print("Exercise_4:", str_4.startswith(" "))
print("Exercise_4:", str_4.endswith(" "))
split_4 = str_4.split(" ")
print("Exercise_4:", type(split_4), split_4)
del split_4[0]
print("Exercise_4:", split_4)
del split_4[-1]
print("Exercise_4:", split_4)
str_4_new = str(split_4)
print(type(str_4_new), str_4_new)


# Exercise_4. Option_2. Напишите программу, которая удаляет пробел в начале и конце строки.

print(("-"*25) + "Exercise_4. Option_2" + ("-"*25))

str_4_2 = " Exercise 4 "
print(len(str_4_2))
print(str_4.startswith(" "))
print(str_4.endswith(" "))
print(str_4_2[1:11])




