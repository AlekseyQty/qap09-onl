from funck import Methods


def calculator():
    print("Это простой калькулятор на Python")
    while True:
        print("Выберите действие которое хотите сделать:\n"
              "Сложить: +\n"
              "Вычесть: -\n"
              "Умножить: *\n"
              "Поделить: /\n"
              "Выйти: q\n")
        action = input("Действие: ")

        if action == "q":
            print("Выход из программы")
            break
        if action in ('+', '-', '*', '/'):
            x = float(input("x = "))
            y = float(input("y = "))
            if action == '+':
                Methods.addition(x, y)
            elif action == '-':
                Methods.subtaraction(x, y)
            elif action == '*':
                Methods.multiplication(x, y)
            elif action == '/':
                Methods.division(x, y)


calculator()
