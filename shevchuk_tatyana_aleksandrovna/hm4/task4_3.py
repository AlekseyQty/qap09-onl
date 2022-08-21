# 3 Дан список ["I", "love", "arrays", "they", "are", "my", "favorite"] сделайте из него
# строку => "I love arrays they are my favorite"

list1 = ["I", "love", "arrays", "they", "are", "my", "favorite"]
list1 = (" ".join(list1))
print(f'{type(list1)}, {list1}')
