from abc import ABC, abstractmethod


class Calculator(ABC):
    @abstractmethod
    def calculate_numbers(self):
        print("Calculate some numbers")


class Methods(Calculator):
    @abstractmethod
    def calculate_numbers(self):
        print("Calculate some numbers")

    @abstractmethod
    def addition(self, num1, num2):
        print("Add some numbers")

    @abstractmethod
    def subtraction(self, num1, num2):
        print("Subtract some numbers")

    @abstractmethod
    def multiplication(self, num1, num2):
        print("Multiply some numbers")

    @abstractmethod
    def division(self, num1, num2):
        print("Divide some numbers")


class Operations(Methods):
    def calculate_numbers(self):
        print("Calculate num1 and num2")

    def addition(self, num1, num2):
        return f"Result of addition: {num1 + num2}"

    def subtraction(self, num1, num2):
        return f"Result of subtraction: {num1 - num2}"

    def multiplication(self, num1, num2):
        return f"Result of multiplication: {num1 * num2}"

    def division(self, num1, num2):
        try:
            result = num1 / num2
        except ZeroDivisionError:
            return f"The num2 is zero. Can not be divided by zero"
        else:
            return f"Result of division: {result}"


operation = Operations()