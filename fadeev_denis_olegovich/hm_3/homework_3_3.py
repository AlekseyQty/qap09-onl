# В строке "Ivanou Ivan" поменяйте местами слова => "Ivan Ivanou"
name = "Ivanou Ivan"
name = name.split(' ')
name = name[::-1]
name = ' '.join(name)
print(name)