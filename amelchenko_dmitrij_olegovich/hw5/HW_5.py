# 1.Факториал
from random import randrange

a = randrange(2, 20)

factorial = 1

for i in range(2, a+1):
    factorial *= i
    print(f'Factorial: {a}', factorial)

#2.BuzzFuzz

for i in range(1,101):
    if i % 3 == 0:
        print('Fuzz')
    elif i % 5 == 0:
        print('Buzz')
    elif i % 3 == 0 or i % 5 == 0:
        print('FuzzBuzz')
    else: 
        print(i)

