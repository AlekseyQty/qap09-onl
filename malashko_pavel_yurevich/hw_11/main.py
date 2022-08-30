import func

operation = func.Operations()

print("This calculator can perform next operations:\n1.Addition\n2.Subtraction\n3.Multiplication\n4.Division")
num = int(input("Please, choose operation, which you want to perform: "))
first_number = int(input("Input the first number: "))
second_number = int(input("Input the second number: "))


try:
    if num == 1:
        print(f"Result of operation is: {operation.addition(first_number, second_number)}")
    elif num == 2:
        print(f"Result of operation is: {operation.subtraction(first_number, second_number)}")
    elif num == 3:
        print(f"Result of operation is: {operation.multiplication(first_number, second_number)}")
    elif num == 4:
        print(f"Result of operation is: {operation.division(first_number, second_number)}")
    else:
        print("Please, enter the correct number of operation")
except ZeroDivisionError as err:
    print("You can't divide by zero :(")

