'''
Перевести строку в массив
"Robin Singh" => ["Robin”, “Singh"]
"I love arrays they are my favorite" => ["I", "love", "arrays", "they", "are", "my",
"favorite"]
'''
name = "Robin Singh"
print(f"{name.split()}")
arr = "I love arrays they are my favorite"
print(f"{arr.split()}")
