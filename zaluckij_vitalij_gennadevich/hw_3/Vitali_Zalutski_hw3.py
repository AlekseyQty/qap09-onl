# 1.Заменить символ "#" на символ "/" в строке 'www.my site.com#about'
first = "www.my site.com#about"
print(first.replace("#", "/"))

#2. Напишете программу, которая добавляет 'ing' к словам
word1 = "try"
word2 = "read"
word3 = "cheat"
the_ending = "ing"
print(word1 + the_ending, word2 + the_ending, word3 + the_ending)

# 3.В строке «Иванов Иван» поменяйте местами слова => «Иван Иванов»
full_name = ("Ivanov Ivan")
full_name = full_name.split(" ")
full_name = full_name[::-1]
full_name = " ".join(full_name)
print(full_name)

#4.Напишите программу, которая удаляет пробел в начале, в конце строки
first_string = " This my first strings "
print(first_string)
print(first_string.strip())