# 1.	Заменить символ “#” на символ “/” в строке 'www.my_site.com#about'

String_1 = "www.my_site.com#about"
print(String_1.replace("#", "/"))


# 2.	Напишите программу, которая добавляет ‘ing’ к словам

String_2 = "Push"
print(f"{String_2}ing")

# 3.	В строке “Ivanou Ivan” поменяйте местами слова => "Ivan Ivanou"

String_3 = "Ivan Ivanou"
print(" ".join(String_3.split()[::-1]))

# 4.	Напишите программу которая удаляет пробел в начале, в конце строки

String_4 = " London is the capital of Great Britain. "
print(String_4.strip())

