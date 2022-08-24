from abc import ABC, abstractmethod

class Methods(ABC):
    @abstractmethod
    def summa(self, number_1, number_2):
        raise NotImplemented

    @abstractmethod
    def subtraction(self,number_1, number_2):
        raise NotImplemented

    @abstractmethod
    def multiplication(self, number_1, number_2):
        raise NotImplemented

    @abstractmethod
    def division(self, number_1, number_2):
        raise NotImplemented


class Math_functions(Methods):
    def summa(self, number_1, number_2):
        print(number_1 + number_2)

    def subtraction(self, number_1, number_2):
        print(number_1 - number_2)

    def multiplication(self, number_1, number_2):
        print(number_1 * number_2)

    def division(self, number_1, number_2):
        try:
            print(number_1 / number_2)
        except ZeroDivisionError:
            print("Вы не можете делить на ноль!")
