import func

print("1. Сложение \n2. Вычитание \n3. Умножение \n4. Деление \n")
operation_input = int(input("Выберите операцию (номер):"))

if operation_input == 1:
    func.Addition()
elif operation_input == 2:
    func.Subtraction()
elif operation_input == 3:
    func.Multiplication()
elif operation_input == 4:
    func.Division()
