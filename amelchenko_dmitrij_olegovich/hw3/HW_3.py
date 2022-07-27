#1.Заменить символ “#” на символ “/” в строке 'www.my_site.com#about'

str = 'www.my_site.com#about'
print(str.replace('#', '/'))

#2. Напишите программу, которая добавляет ‘ing’ к словам

wd_1 = 'Read'
wd_2 = 'Go'

add_ing = 'ing'
print(wd_1+add_ing, wd_2+add_ing)

#3.В строке “Ivanou Ivan” поменяйте местами слова => "Ivan Ivanou"

full_name = "Ivanou Ivan"

print(" ".join(full_name.split()[::-1]))


#4. Напишите программу которая удаляет пробел в начале, в конце строки

task_4 = '   Hello world   '

print(task_4.strip())

