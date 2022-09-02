import func

operation = func.Operations()

choose_operation = int(input("Please, choose operation: "
                             " \n1.Addition \n2.Subtraction \n3.Multiplication \n4.Division \n "))
first_number = int(input("Please, enter the first number: "))
second_number = int(input("Please, enter the second number: "))

try:
    if choose_operation == 1:
        print(f"Result of operation is: {operation.addition(first_number, second_number)}")
    elif choose_operation == 2:
        print(f"Result of operation is: {operation.subtraction(first_number, second_number)}")
    elif choose_operation == 3:
        print(f"Result of operation is: {operation.multiplication(first_number, second_number)}")
    elif choose_operation == 4:
        print(f"Result of operation is: {operation.division(first_number, second_number)}")
    else:
        print("Please, enter the correct number of operation")
except ZeroDivisionError as err:
    print("You can't divide by zero ")
