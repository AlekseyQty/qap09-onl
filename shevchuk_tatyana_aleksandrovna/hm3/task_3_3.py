# В строке “Ivanou Ivan” поменяйте местами слова => "Ivan Ivanou"


surname_name = "Ivanou Ivan"
surname_name = surname_name.split(" ")
surname = surname_name[0]
name = surname_name[1]
print(f'{name + " " + surname}')