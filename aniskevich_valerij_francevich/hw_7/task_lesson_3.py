# 3 Напишите программу, принимающую зубчатый массив любого типа и
# возвращающего его "плоскую" копию.
# flatten([1, 2, [3, 4, [5, 6], 7], [8, [9, [10]]]])
# [1, 2, [3, 4, [5, 6], 7], [8, [9, [10]]] => [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
new_list = []
flatten = [1, 2, [3, [4], [5, [6]], 7], [8, [9, [10], 11], 12], 13]


def raspakovka(my_list: list):
    for i in my_list:
        if type(i) == list:
            raspakovka(i)
        else:
            new_list.append(i)
    return new_list


print(raspakovka(flatten))
