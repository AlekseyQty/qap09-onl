def calc():
    """Простой калькулятор"""
    operation = int(input("Выберите операцию: \n  1.Сложение\n  2.Вычитание\n  3.Умножение\n  4.Деление\n\t"
                          "Введите номер пункта меню: "))
    if operation < 5:
        first_number = int(input("Введите первое число: "))
        second_number = int(input("Введите второе число: "))
        if operation == 1:
            print(first_number + second_number)
        elif operation == 2:
            print(first_number - second_number)
        elif operation == 3:
            print(first_number * second_number)
        elif operation == 4:
            print(first_number / second_number)
    else:
        print("Ошибка, номера такой операции не существует.")


calc()
