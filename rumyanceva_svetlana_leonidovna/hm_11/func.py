from abc import abstractmethod, ABC


class Calculator(ABC):
    @abstractmethod
    def calculate_smth(self):
        print("in order to calculate any actions with numbers")


class Methods(Calculator):
    @abstractmethod
    def calculate_smth(self):
        print("in order to calculate any actions with numbers")

    @abstractmethod
    def add(self, first_number, second_number):
        print("Add the numbers")

    @abstractmethod
    def multiply(self, first_number, second_number):
        print("Multiply the numbers")

    @abstractmethod
    def subtract(self, first_number, second_number):
        print("Subtract the numbers")

    @abstractmethod
    def divide(self, first_number, second_number):
        print("Divide the numbers")


class Actions(Methods):
    def calculate_smth(self):
        print("you can calculate any actions with numbers")

    def add(self, first_number, second_number):
        return first_number + second_number

    def multiply(self, first_number, second_number):
        return first_number * second_number

    def subtract(self, first_number, second_number):
        return first_number - second_number

    def divide(self, first_number, second_number):
        try:
            result = first_number / second_number
        except ZeroDivisionError:
            return "Division by zero!"

        else:
            return result


act = Actions()
