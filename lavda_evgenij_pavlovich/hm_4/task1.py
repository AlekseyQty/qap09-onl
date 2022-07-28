"""Перевести строку в массив
"Robin Singh" => ["Robin”, “Singh"]
"I love arrays they are my favorite" => ["I", "love", "arrays", "they", "are", "my",
"favorite"]"""

my_string = "Robin Singh"
my_list = my_string.split()
print(type(my_list), my_list)

my_long_string = "I love arrays they are my favorite"
my_long_list = my_long_string.split()
print(type(my_long_list), my_long_list)
