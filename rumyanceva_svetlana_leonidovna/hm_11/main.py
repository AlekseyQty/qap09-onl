# Цель: Закрепить знания по ООП. Интерфейсы. Абстрактные классы.
# Задание 1. Написать калькулятор. Программа должна содержать 4 функции принимающие два аргумента и возвращающие
# результаты сложения, вычитания, умножения и деления. Реализовать пользовательский интерфейс Methods.
# От него унаследовать математические методы и реализовать их.
# Добавить валидацию входных данных. Программа должна состоять из двух файлов(main.py, func.py).
import func

try:
    first_number = float(input("Enter any first number: "))
    second_number = float(input("Enter any second number: "))
except ValueError:
    print("You have entered no number.")
    exit()
else:

    if __name__ == "__main__":
        sign = input("Choose and enter any action (+ - * /): "
                     "+ addition, " 
                     "- subtraction, " 
                     "* multiplication, " 
                     "/ division: ")
        action_dict = {"+": func.act.add(first_number, second_number),
                       "-": func.act.subtract(first_number, second_number),
                       "*": func.act.multiply(first_number, second_number),
                       "/": func.act.divide(first_number, second_number)}

        print(action_dict.get(sign, "No such action"))
