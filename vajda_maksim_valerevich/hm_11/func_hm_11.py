from abc import ABC, abstractmethod


class Methods(ABC):

    @abstractmethod
    def operation(self, first_input, second_input):
        raise NotImplemented


class Addition(Methods):

    def operation(self, first_input, second_input):
        print(f'\nРезультат вашей операции: {first_input + second_input}')


class Subtraction(Methods):

    def operation(self, first_input, second_input):
        print(f'\nРезультат вашей операции: {first_input - second_input}')


class Multiplication(Methods):

    def operation(self, first_input, second_input):
        print(f'\nРезультат вашей операции: {first_input * second_input}')


class Division(Methods):

    def operation(self, first_input, second_input):
        try:
            print(f'\nЧастное : {int(first_input // second_input)}, Остаток: {int(first_input % second_input)}')

        except ZeroDivisionError:
            print(f'\nОшибка: на < 0 > делить нелья')



