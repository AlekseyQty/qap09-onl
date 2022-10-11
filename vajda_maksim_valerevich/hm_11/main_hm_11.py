import func_hm_11 as func


def my_calculator(calc_operation):
    if calc_operation in ['1', '2', '3', '4']:
        first_input = input('Введите первое число: ')
        second_input = input('Введите второе число: ')

        if first_input.isalpha() or second_input.isalpha():
            print('\nОшибка: Вы ввели букву')

        else:
            first_input = int(first_input)
            second_input = int(second_input)

            if calc_operation == '1':
                calc = func.Addition()
            elif calc_operation == '2':
                calc = func.Subtraction()
            elif calc_operation == '3':
                calc = func.Multiplication()
            elif calc_operation == '4':
                calc = func.Division()

            calc.operation(first_input, second_input)

    elif calc_operation == 'Q':
        print('Exit')
        quit()
    else:
        print('\nТакой операции не существует')





while True:
    my_calculator((input('\nВыберите операцию:\n'
                         '1. Сложение\n'
                         '2. Вычитание\n'
                         '3. Умножение\n'
                         '4. Деление\n'
                         'Q - Для выхода\n'
                         'Введите номер пункта меню: ')))

