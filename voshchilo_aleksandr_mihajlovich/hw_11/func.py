from abc import ABC, abstractmethod


class Methods(ABC):

    @abstractmethod
    def addition(self, a, b):
        raise NotImplemented

    @abstractmethod
    def subtraction(self, a, b):
        raise NotImplemented

    @abstractmethod
    def multiplication(self, a, b):
        raise NotImplemented

    @abstractmethod
    def division(self, a, b):
        raise NotImplemented


class Math_functions(Methods):

    def addition(self, a, b):
        sum_ab = a + b
        print(f"Результат: {sum_ab}")

    def subtraction(self, a, b):
        sub_ab = a - b
        print(f"Результат: {sub_ab}")

    def multiplication(self, a, b):
        mult_ab = a * b
        print(f"Результат: {mult_ab}")

    def division(self, a, b):
        try:
            div_ab = a / b
        except ZeroDivisionError:
            print("Division by zero!!!")
        else:
            print(f"Результат: {div_ab}")
