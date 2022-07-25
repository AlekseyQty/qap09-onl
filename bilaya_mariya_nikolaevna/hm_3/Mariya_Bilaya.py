# Exercise_1. Заменить символ "#" на символ "/" в строке 'www.my_site.com#about'


my_str = "www.my_site.com#about"
my_str1 = (my_str.replace("#", "/"))
print("Exercise_1:", my_str1)


# Exercise_2. Option_1 Напишитие программу, которая добавляет 'ing' к словам


words = my_str1.split(".")
print("Exercise_2_words:", type(words), words)
res_1 = words[0] + "ing"
res_2 = words[1] + "ing"

words1 = words[-1].split("/")
print("Exercise_2_words_1:",type(words1), words1)
res_3 = words1[0] + "ing"
res_4 = words1[1] + "ing"
print("Exercise_2_option_1:", res_1, res_2, res_3, res_4)


# Exercise_2.Option_2 Напишитие программу, которая добавляет 'ing' к словам


string_2_2 = "try to do this exercise"
split_1 = string_2_2.split(" ")
print("Exercise_2_option_2:", type(split_1), split_1)
add_1 = split_1[0] + "ing"
add_2 = split_1[1] + "ing"
add_3 = split_1[2] + "ing"
add_4 = split_1[3] + "ing"
add_5 = split_1[4] + "ing"
print("Exercise_2_option_2:", add_1, add_2, add_3, add_4, add_5)


# Exercise_3. В строке "Ivanou Ivan" поменяйте местами слова => "Ivan Ivanou"


last_name = "Ivanou"
first_name = "Ivan"
str_3 = last_name + first_name
print("Exercise_3:",type(str_3), str_3)

str_1 = "Ivanou Ivan"
print("Exercise_3:",type(str_1), str_1)


# Exercise_4. Напишите программу, которая удаляет пробел в начале и конце строки


str_4 = " Exercise 4 "
print("Exercise_4:", str_4.startswith(" "))
print("Exercise_4:", str_4.endswith(" "))
split_4 = str_4.split(" ")
print("Exercise_4:", type(split_4), split_4)
del split_4[0]
print("Exercise_4:", split_4)
del split_4[-1]
print("Exercise_4:", split_4)




