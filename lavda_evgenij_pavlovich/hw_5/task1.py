"""Написать программу, которая считает факториал произвольного числа. Не
использовать метод для расчета факториала из стандартной библитоеки.
Факториал считается как:
5! = 5 × 4 × 3 × 2 × 1 = 120"""

your_number = int(input("Enter your number: "))
factorial = 1
for i in range(2, your_number + 1):
    factorial = factorial * i
print(f"Your factorial: {factorial}")
