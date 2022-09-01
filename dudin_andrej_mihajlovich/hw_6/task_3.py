print("Выберите операцию\n 1. Сложение\n 2. Вычитание \n 3. Умножение \n 4. Деление \n ")
operation = str(input("Введите номер пункта меню "))
first_number = int(input("Введите первое число "))
second_number = int(input("Введите второе число "))
result = 0
if operation == "1":
    result = first_number + second_number
    print(f"Результат сложения {first_number} + {second_number} = {result}")
elif operation == "2":
    result = first_number - second_number
    print(f"Результат разности {first_number} - {second_number} = {result}")
elif operation == "3":
    result = first_number * second_number
    print(f"Результат умножения {first_number} * {second_number} = {result}")
elif operation == "4":
    if second_number != 0:
        result = first_number / second_number
        int_part = int(result)
        ostatok = int(round(result - int_part, 1)*10)
        print(f"Частное: {int_part}, Остаток: {ostatok}")
    else:
        print("Второе число не должно равняться нулю")
else:
    print("Вы ввели операцию не из списка")
