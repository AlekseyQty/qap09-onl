#Вам передан массив чисел. Известно, что каждое число в этом массиве имеет
#пару, кроме одного:
list_1 = [1, 5, 2, 9, 2, 9, 1]
count = {}
for item in list_1:
    count[item] = count.get(item, 0) + 1

print(count)
result = None
for key, value in count.items():
    if value % 2 == 1:
        result = key
        break

print(result)
#Напишите программу, которая будет выводить уникальное число