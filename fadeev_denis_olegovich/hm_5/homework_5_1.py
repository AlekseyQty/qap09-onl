# Написать программу, которая считает факториал произвольного числа. Не
# использовать метод для расчета факториала из стандартной библитоеки.
# Факториал считается как:
# 5! = 5 × 4 × 3 × 2 × 1 = 120

n = int(input())
factorial = 1
if n % 1 == 0 and n >= 0:
    for i in range(1, n + 1):
        factorial = factorial * i
    print(f"{n}! = {factorial}")
