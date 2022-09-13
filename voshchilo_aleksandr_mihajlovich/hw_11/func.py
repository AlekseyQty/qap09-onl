class Methods():
    a = 0
    b = 0

    def __init__(self):
        self.a = float(input("Введите первое число:"))
        self.b = float(input("Введите второе число:"))
        Methods.a = self.a
        Methods.b = self.b


class Addition(Methods):

    def __init__(self):
        super().__init__()
        a = Methods.a
        b = Methods.b
        sum_ab = a + b
        print(sum_ab)


class Subtraction(Methods):

    def __init__(self):
        super().__init__()
        a = Methods.a
        b = Methods.b
        sub_ab = a - b
        print(sub_ab)


class Multiplication(Methods):

    def __init__(self):
        super().__init__()
        a = Methods.a
        b = Methods.b
        mult_ab = a * b
        print(mult_ab)


class Division(Methods):

    def __init__(self):
        super().__init__()
        a = Methods.a
        b = Methods.b
        try:
            div_ab = a / b
        except ZeroDivisionError:
            print("Division by zero!!!")
        else:
            print(div_ab)


