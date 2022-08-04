# 1.Факториал

number = int(input())
factorial = 1
if number > 0:
    while number:
        factorial = factorial * number
        number -= 1
    print(factorial)
else:
    print("Error, please, input positive number.")
