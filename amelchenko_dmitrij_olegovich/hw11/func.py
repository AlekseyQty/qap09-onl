from abc import ABC, abstractmethod


class Methods(ABC):

    @abstractmethod
    def math_func(self, arg1, arg2):
        self.arg1 = arg1
        self.arg2 = arg2

class Sum_num(Methods):
    def math_func(self, arg1, arg2):
        return float(arg1) + float(arg2)

class Calc_num(Methods):
    def math_func(self, arg1, arg2):
        return float(arg1) - float(arg2)

class Multip_num(Methods):
    def math_func(self, arg1, arg2):
        return float(arg1) * float(arg2)

class Divi_num(Methods):
    def math_func(self, arg1, arg2):
        return float(arg1) / float(arg2)

