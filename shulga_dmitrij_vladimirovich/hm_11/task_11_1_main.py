#Написать калькулятор. Программа должна содержать 4 функции принимающие два аргумента и возвращающие результаты
# сложения, вычитания, умножения и деления. Реализовать пользовательский интерфейс Methods. От него унаследовать
# математические методы и реализовать их.
#Добавить валидацию входных данных. Программа должна состоять из двух файлов(main.py, func.py).

import task_11_1_func as func

print("Выберите операцию:")
print("1. Сложение")
print("2. Вычитание")
print("3. Умножение")
print("4. Деление")

my_choice = ""
while my_choice != "quit":
    my_choice = input("Введите желаемую математическую операцию: ")
    if my_choice == "quit":
        print("Goodbye")
    else:
        number_1 = input("Введите первое число: ")
        number_2 = input("Введите второе число: ")
        if number_1.isalpha() or number_2.isalpha():
            print("You entered a letter, repeat again")
        else:
            number_1 = int(number_1)
            number_2 = int(number_2)
            if my_choice == "1":
                sum_function = func.Math_functions()
                sum_function.summa(number_1, number_2)
            elif my_choice == "2":
                sum_function = func.Math_functions()
                sum_function.subtraction(number_1, number_2)
            elif my_choice == "3":
                sum_function = func.Math_functions()
                sum_function.multiplication(number_1, number_2)
            elif my_choice == "4":
                sum_function = func.Math_functions()
                sum_function.division(number_1, number_2)
            else:
                print("Попрубуйте еще раз!")


