# Написать программу, которая считает факториал произвольного числа. Не
# использовать метод для расчета факториала из стандартной библитоеки.


my_num = int(input())
factorial = 1
for i in range(1, my_num + 1):
    if my_num < 1:
        factorial = 1
    elif my_num > 1:
        factorial *= i
print(factorial)
