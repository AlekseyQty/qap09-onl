# 1.Заменить символ “#” на символ “/” в строке 'www.my_site.com#about'
message = "www.my_site.com#about"
print(message.replace("#", "/"))

# 2.Напишите программу, которая добавляет ‘ing’ к словам
my_list = ["swim", "go", "snow", "rain"]
for i in my_list:
    print(i + "ing")

# 3.В строке “Ivanou Ivan” поменяйте местами слова => "Ivan Ivanou"
my_name = "Ivanov Ivan"
changed_name = my_name.split()
final_name = changed_name[::-1]
print(" ".join(final_name))

# 4.Напишите программу которая удаляет пробел в начале, в конце строки
my_string = str(input("vvedite text"))
if my_string.startswith(" ") == True:
    new_string = my_string[1:]
else:
    new_string = my_string[::]
if new_string.endswith(" ") == True:
    final_string = new_string[0:-1]
    print(final_string)
else:
    print(new_string)
