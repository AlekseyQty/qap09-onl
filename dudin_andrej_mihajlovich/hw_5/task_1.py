max_number = int(input("Enter max step for factorial "))
n, factorial = 1, 1

while n <= max_number:
    factorial *=n
    n +=1
print(factorial)