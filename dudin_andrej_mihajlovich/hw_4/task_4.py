'''
Создайте список из 10 элементов, вставьте на 3-ю позицию новое значение,
удалите элемент из списка под индексом 6
'''
list = ["char_1", "char_2", "char_3", "char_4", "char_5", "char_6", "char_7", "char_8", "char_9", "char_10"]
list.insert(2, "new_element")
del(list[6])
print(list)