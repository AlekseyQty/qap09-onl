#Написать программу, которая считает факториал произвольного числа. Не
#использовать метод для расчета факториала из стандартной библитоеки.
#Факториал считается как:
#5! = 5 × 4 × 3 × 2 × 1 = 120

my_int = int(input('put ur number: '))
my_int = list(range(1, (my_int+1)))

factorial = 1

for i in my_int:
    factorial *= i

print(factorial)