# 1 Перевести строку в массив
# "Robin Singh" => ["Robin”, “Singh"]
# "I love arrays they are my favorite" => ["I", "love", "arrays", "they", "are", "my", "favorite"]

task_str1 = 'Robin Singh'
task_str2 = 'I love arrays they are my favorite'

print('Task_1: ')
print(task_str1.split(' '))
print(task_str2.split(' '))

# 2 Дан список: [‘Ivan’, ‘Ivanou’], и 2 строки: Minsk, Belarus
# Напечатайте текст: “Привет, Ivan Ivanou! Добро пожаловать в Minsk Belarus”

task2_list = ['Ivan', 'Ivanou']
task2_city = 'Minsk'
task2_country = 'Belarus'
name = ' '.join(task2_list)

print('Task_2: ')
print(f'Привет, {name}! Добро пожаловать в {task2_city} {task2_country}')

# 3 Дан список ["I", "love", "arrays", "they", "are", "my", "favorite"] сделайте из него строку =>
# "I love arrays they are my favorite"

task3_list = ["I", "love", "arrays", "they", "are", "my", "favorite"]

print('Task_3: ')
print(' '.join(task3_list))

# 4 Создайте список из 10 элементов, вставьте на 3-ю позицию новое значение, удалите элемент из списка под индексом 6

new_list_10 = list(range(0, 100, 10))
new_list_10.insert(2, 9999)
del new_list_10[6]

print('Task_4: ')
print(new_list_10)

"""
5. Есть 2 словаря
a = { 'a': 1, 'b': 2, 'c': 3}
b = { 'c': 3, 'd': 4,'e': 5}
Необходимо их объединить по ключам, а значения ключей поместить в список,
если у одного словаря есть ключ "а", а у другого нету, то поставить значение
None на соответствующую позицию(1-я позиция для 1-ого словаря, вторая для 2-ого)
ab = {'a': [1, None], 'b': [2, None], 'c': [3, 3], 'd': [None, 4], 'e': [None, 5]}
"""
a = {'a': 1, 'b': 2, 'c': 3}
b = {'c': 3, 'd': 4, 'e': 5}
net = None
a_b = {**a, **b}

if 'a' in a and 'a' in b:
    a_b['a'] = [a_b['a'], a_b['a']]
elif 'a' in b:
    a_b['a'] = [net, a_b['a']]
else:
    a_b['a'] = [a_b['a'], net]

if 'b' in a and 'b' in b:
    a_b['b'] = [a_b['b'], a_b['b']]
elif 'b' in b:
    a_b['b'] = [net, a_b['b']]
else:
    a_b['b'] = [a_b['b'], net]

if 'c' in a and 'c' in b:
    a_b['c'] = [a_b['c'], a_b['c']]
elif 'c' in b:
    a_b['c'] = [net, a_b['c']]
else:
    a_b['c'] = [a_b['c'], net]

if 'd' in a and 'd' in b:
    a_b['d'] = [a_b['d'], a_b['d']]
elif 'd' in b:
    a_b['d'] = [net, a_b['d']]
else:
    a_b['d'] = [a_b['d'], net]

if 'e' in a and 'e' in b:
    a_b['e'] = [a_b['e'], a_b['e']]
elif 'e' in b:
    a_b['e'] = [net, a_b['e']]
else:
    a_b['e'] = [ a_b['e'],net]

print('Task_5: ')
print("True answer: {'a': [1, None], 'b': [2, None], 'c': [3, 3], 'd': [None, 4], 'e': [None, 5]}")
print(f"My answer:  {a_b}")

print(f'{"-"*20} TASK *1 {"-"*20}')

"""
*1) Вам передан массив чисел. Известно, что каждое число в этом массиве имеет
пару, кроме одного: [1, 5, 2, 9, 2, 9, 1] => 5
Напишите программу, которая будет выводить уникальное число
"""
array_start = [1, 5, 2, 9, 2, 9, 1]


for i in range(len(array_start)):
    amount = array_start.count(array_start[i])
    if amount == 1:
        print(f'Task*1: {array_start[i]}')
