import func

try:
    num1 = float(input('Enter the first number: '))
    num2 = float(input('Enter the second number: '))

except ValueError:
    print('You select invalid input. Try adain')
else:
    operation = input('Select the number of operation: 1-Addiction, 2-Substraction, 3-Multiplication, 4-Division ')
    if operation not in ("1", "2", "3", "4"):
        print('You select invalid operation. Try again')
    all_operations = {"1": func.operation.addition(num1, num2),
                      "2": func.operation.subtraction(num1, num2),
                      "3": func.operation.multiplication(num1, num2),
                      "4": func.operation.division(num1, num2)}
finally:
    print('I have done it, but it was so complicated')

print(all_operations.get(operation))