"""Есть 2 словаря
a = { 'a': 1, 'b': 2, 'c': 3}
b = { 'c': 3, 'd': 4,'e': 5}
Необходимо их объединить по ключам, а значения ключей поместить в список,
если у одного словаря есть ключ "а", а у другого нету, то поставить значение
None на соответствующую позицию(1-я позиция для 1-ого словаря, вторая для
2-ого)
ab = {'a': [1, None], 'b': [2, None], 'c': [3, 3], 'd': [None, 4], 'e': [None, 5]}"""

a = {'a': 1,
     'b': 2,
     'c': 3}

b = {'c': 3,
     'd': 4,
     'e': 5}

ab = {key: [a.get(key), b.get(key)] for key in a | b}
print(ab)