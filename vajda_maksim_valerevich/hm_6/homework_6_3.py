print(f'{"̅" * 26}{"̅" * 26}')
print(f'{" " * 20} THIRD TASK {" " * 20}')
print(f'{" " * 20} CALCULATOR {" " * 20}')
print(f'{"̅" * 26}{"̅" * 26}')
"""
3. Простейший калькулятор v0.1
Реализуйте программу, которая спрашивала у пользователя, какую операцию он хочет
произвести над числами, а затем запрашивает два числа и выводит результат
Проверка деления на 0 Реализовать программу нужно с использованием функций.
Пример
Выберите операцию:
1 Сложение
2 Вычитание
3 Умножение
4 Деление
Введите номер пункта меню:
>>> 4
Введите первое число:
>>> 10
Введите второе число:
>>> 3
Частное: 3, Остаток: 3
"""
calc_start = int(input('Выберите операцию:\n'
                       '1. Сложение\n'
                       '2. Вычитание\n'
                       '3. Умножение\n'
                       '4. Деление\n'
                       'Введите номер пункта меню: '))

if calc_start not in [1, 2, 3, 4]:
    print('Такой операции не существует, приходите позже')
    print(f'{"̅" * 26}{"̅" * 26}')
    quit()


def calculator(first_input, second_input):
    result = None
    if calc_start == 1:
        result = first_input + second_input
    elif calc_start == 2:
        result = first_input - second_input
    elif calc_start == 3:
        result = first_input * second_input
    elif calc_start == 4:
        if second_input == 0:
            result = '\nОшибка: на < 0 > делить нелья'
        else:
            result = (f'\nЧастное : {int(first_input // second_input)}, Остаток: {int(first_input % second_input)}')

    return (f'Результат вашей операции: {result}')


print(calculator(int(input('Введите первое число: ')), int(input('Введите второе число: '))))
print(f'{"̅" * 26}{"̅" * 26}')
