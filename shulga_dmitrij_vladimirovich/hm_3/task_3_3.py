# 3.В строке “Ivanou Ivan” поменяйте местами слова => "Ivan Ivanou"

string = 'Ivanou Ivan'
print(f' Reverse "Ivanou Ivan" - "{string[7:] + " " + string[:6]}"')

