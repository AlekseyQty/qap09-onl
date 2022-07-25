# 1.	Заменить символ “#” на символ “/” в строке 'www.my_site.com#about'

case_1 = "www.my_site.com#about"
print(case_1.replace("#", "/"))


# 2.	Напишите программу, которая добавляет ‘ing’ к словам

case_2 = "Push"
print(f"{case_2}ing")

# 3.	В строке “Ivanou Ivan” поменяйте местами слова => "Ivan Ivanou"

case_3 = "Ivan Ivanou"
print(" ".join(case_3.split()[::-1]))

# 4.	Напишите программу которая удаляет пробел в начале, в конце строки

case_4 = " London is the capital of Great Britain. "
print(case_4.strip())

