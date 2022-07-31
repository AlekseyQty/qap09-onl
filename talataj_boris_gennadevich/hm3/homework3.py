# Заменить символ “#” на символ “/” в строке 'www.my_site.com#about'
my_str = 'www.my_site.com#about'
a = my_str.replace('#', '/')
print(a)

#Напишите программу, которая добавляет ‘ing’ к словам
s_1 = 'last'
s_2 = 'ing'
print(s_1 + s_2)

#В строке “Ivanou Ivan” поменяйте местами слова => "Ivan Ivanou"
s = 'Ivanov Ivan'
result = ' '.join(s.split(' ')[::-1])
print(result)

#Напишите программу которая удаляет пробел в начале, в конце строки
name = ' My name is Boris '
print(name.strip())
