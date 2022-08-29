import func_11

# Написать калькулятор. Программа должна содержать 4 функции принимающие два аргумента и возвращающие результаты
# сложения, вычитания, умножения и деления. Реализовать пользовательский интерфейс Methods. От него унаследовать
# математические методы и реализовать их.
# Добавить валидацию входных данных. Программа должна состоять из двух файлов (main.py, func.py).

try:
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
except ValueError:
    print("You selected invalid input. Try again")
else:
    operation = input("Select the number of operation: 1-Addition, 2-Subtraction, 3-Multiplication, 4-Division ")
    if operation not in ("1", "2", "3", "4"):
        print("You selected invalid operation. Try again")
    all_operations = {"1": func_11.operation.addition(num1, num2),
                      "2": func_11.operation.subtraction(num1, num2),
                      "3": func_11.operation.multiplication(num1, num2),
                      "4": func_11.operation.division(num1, num2)}
finally:
    print("I have done it, but it was so complicated")

print(all_operations.get(operation))
