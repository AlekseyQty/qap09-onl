# 1.Факториал
# Написать программу, которая считает факториал произвольного числа.
# Не использовать метод для расчета факториала из стандартной библитоеки.
# Факториал считается как:
# 5! = 5 × 4 × 3 × 2 × 1 = 120

number = input("Please enter number: ")
number = int(number)
factorial = 1
for i in range(1, number+1):
    if i > 1:
        factorial *= i
    else:
        factorial = 1
print(factorial)


