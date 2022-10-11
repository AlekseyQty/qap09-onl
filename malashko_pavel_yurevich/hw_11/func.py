from abc import ABC, abstractmethod


class Calculator(ABC):
    @abstractmethod
    def calculation(self):
        print("This method can calculate two numbers")


class Methods(Calculator):
    @abstractmethod
    def calculation(self):
        print("This method can calculate two numbers")

    @abstractmethod
    def addition(self, num1, num2):
        print("This method can add two numbers")

    @abstractmethod
    def subtraction(self, num1, num2):
        print("This method can subtract one number from another")

    @abstractmethod
    def multiplication(self, num1, num2):
        print("This method can multiple two numbers")

    @abstractmethod
    def division(self, num1, num2):
        print("This method can subtract one number from another")


class Operations(Methods):
    def calculation(self):
        print("This method can calculate two numbers")

    def addition(self, num1, num2):
        return num1 + num2

    def subtraction(self, num1, num2):
        return num1 - num2

    def multiplication(self, num1, num2):
        return num1*num2

    def division(self, num1, num2):
        return num1/num2

