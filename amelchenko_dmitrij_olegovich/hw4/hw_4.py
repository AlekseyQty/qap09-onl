#1.Перевести строку в массив

str_1 = "Robin Singh"
str_2 = "I love arrays they are my favorite"

str_1_list = str_1.split(' ')
str_2_list = str_2.split(' ')

print('Task 2: ',str_1_list, str_2_list)


#2.Создайте список из 10 элементов, вставьте на 3-ю позицию новое значение,удалите элемент из списка под индексом 6

list_task_2 = ['Ivan', 'Ivanov']
list_task_2_str = ' '.join(list_task_2)
str_task_2 = 'Minsk, Belarus'

print('Task 2: ', f'Привет, {list_task_2_str}! Добро пожаловать в {str_task_2}')


#3.Превести масив в строку

list_task_3 = ['I', 'love', 'arrays', 'they', 'are', 'my', 'favorite']
list_task_3_str = ' '.join(list_task_3)

print('Task 3: ',list_task_3_str)


#4.Создайте список из 10 элементов, вставьте на 3-ю позицию новое значение,удалите элемент из списка под индексом 6

list_task_4 =[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

list_task_4.insert(3, 11)
del list_task_4[6]

print('Task 4: ',list_task_4)


#5. 2 словаря необходимо их объединить по ключам, а значения ключей поместить в список,если у одного словаря есть ключ "а",
# а у другого нету, то поставить значение None на соответствующую позицию

a = { 'a': 1, 'b': 2, 'c': 3}
b = { 'c': 3, 'd': 4,'e': 5}

sotr_dict = sorted(list(set(list(a.keys()) + list(b.keys()))))

uni_keys = {}

for key in sotr_dict:
    uni_keys[key] = [a.get(key), b.get(key)]

print('Task 5: ',uni_keys)