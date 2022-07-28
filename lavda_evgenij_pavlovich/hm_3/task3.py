"""В строке “Ivanou Ivan” поменяйте местами слова => "Ivan Ivanou"""
my_string = "Ivanou Ivan"
my_string_without_space = my_string.split()
my_new_string = my_string_without_space[:: -1]
print(" ".join(my_new_string))
