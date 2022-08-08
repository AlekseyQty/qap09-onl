def generator(arr):
    for elem in arr:
        if elem > 0:
            yield elem


for number in generator([34.6, -203.4, 44.9, 68.3, -12.2, 44.6, 12.7]):
    print(number)
