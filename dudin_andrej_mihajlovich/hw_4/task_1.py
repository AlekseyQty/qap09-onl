'''
Перевести строку в массив
"Robin Singh" => ["Robin”, “Singh"]
"I love arrays they are my favorite" => ["I", "love", "arrays", "they", "are", "my",
"favorite"]
'''
string_1 = "Robin Singh"
string_2 = "I love arrays they are my favorite"

list_string_1 = string_1.split()
list_string_2 = string_2.split()

print(list_string_1)