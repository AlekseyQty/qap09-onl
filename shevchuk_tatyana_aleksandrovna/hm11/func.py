from abc import ABC, abstractmethod


class Calculator(ABC):
    @abstractmethod
    def calculation(self):
        print("This method can calculate two numbers")


class Methods(Calculator):
    @abstractmethod
    def calculation(self):
        print("Calculate some numbers")

    @abstractmethod
    def addition(self, num1, num2):
        print("Add two numbers")

    @abstractmethod
    def subtraction(self, num1, num2):
        print("Subtract two numbers")

    @abstractmethod
    def multiplication(self, num1, num2):
        print("Multiply two numbers")

    @abstractmethod
    def division(self, num1, num2):
        print("Divide two numbers")


class Operations(Methods):
    def calculation(self):
        print("Calculate num1 and num2")

    def addition(self, num1, num2):
        return num1 + num2

    def subtraction(self, num1, num2):
        return num1 - num2

    def multiplication(self, num1, num2):
        return num1 * num2

    def division(self, num1, num2):
        return num1 / num2
