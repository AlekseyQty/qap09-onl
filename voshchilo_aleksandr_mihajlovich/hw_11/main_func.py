import func

print("1. Сложение \n2. Вычитание \n3. Умножение \n4. Деление \n")
operation_input = int(input("Выберите операцию (номер): "))

a = float(input("Введите первое число: "))
b = float(input("Введите второе число: "))

if operation_input == 1:
    addition_func = func.Math_functions()
    addition_func.addition(a, b)
elif operation_input == 2:
    subtraction_func = func.Math_functions()
    subtraction_func.subtraction(a, b)
elif operation_input == 3:
    multiplication_func = func.Math_functions()
    multiplication_func.multiplication(a, b)
elif operation_input == 4:
    division_func = func.Math_functions()
    division_func.division(a, b)
