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
name = "Ivan"
last_name = "Ivanov"
print(f"My name is {name} {last_name}")

#4.Напишите программу, которая удаляет пробел в начале, в конце строки
first_string = " This my first strings "
print(first_string)
print(first_string.strip())