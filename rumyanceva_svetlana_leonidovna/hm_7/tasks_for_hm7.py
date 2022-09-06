import numpy as np
print("--------task1_start--------")
# Task1 Напишите функцию, которая принимает на вход одномерный массив и два числа - размеры выходной матрицы. На
# выход программа должна подавать матрицу нужного размера, сконструированную из элементов массива.
# reshape([1, 2, 3, 4, 5, 6], 2, 3) => [
#    [1, 2, 3],
#    [4, 5, 6]]
# reshape([1, 2, 3, 4, 5, 6, 7, 8,], 4, 2) =>
# [[1, 2],
#    [3, 4],
#    [5, 6],
#   [7, 8]]

given_list1 = [1, 17, 0, 4, -2, 6]
b = np.asarray(given_list1).reshape(2, 3)  # from the one-dimensional list to the two-dimensional list!!!!!!!!!!!!!
print(b)

print("--------task1_end--------")
print("--------task2_start--------")
# Генераторы: 1)Напишите генератор, который принимает список numbers = [34.6, -203.4, 44.9, 68.3, -12.2, 44.6, 12.7]
# и возвращает новый список только с положительными числами
# 2)Необходимо составить список чисел, которые указывают на длину слов в строке:
# sentence = "the quick brown fox jumps over the lazy dog", но только если слово не "the".

my_list = [34.6, -203.4, 44.9, 68.3, -12.2, 44.6, 12.7]
new_list = [elem for elem in my_list if elem > 0]
print(new_list)
my_list1 = list(map(int, input("Enter any space-separated integer numbers: ").split()))
new_list1 = [elem for elem in my_list1 if elem > 0]
print(new_list1)


length_letters_list = [len(elem) for elem in input("Enter any sentence: ").split() if not elem == "the"]
print(length_letters_list)
print("--------task2_end--------")
