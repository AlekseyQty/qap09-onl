# Создайте класс инвестиция. Который содержит необходимые поля и методы, например сумма инвестиция и его срок.
# Пользователь делает инвестиция в размере N рублей сроком на R лет под 10% годовых (инвестиция с возможностью ежемесячной
# капитализации - это означает, что проценты прибавляются к сумме инвестиции ежемесячно).
# Написать класс Bank, метод deposit принимает аргументы N и R, и возвращает сумму, которая будет на счету пользователя.

class Investment:

    def __init__(self, sum, term):
        self.sum = sum
        self.term = term


class Bank:
    def __init__(self, invest):
        self.invest = invest

    def deposit(self):

        result = 0
        for i in range(self.invest.term * 12):
            self.invest.sum = (self.invest.sum * 0.1)/12 + self.invest.sum
            result = self.invest.sum
        print(f"Result: {round(result, 2)}")


my_sum = input("Please enter your sum: ")
my_sum = int(my_sum)
my_term = input("Please enter your term in years: ")
my_term = int(my_term)

my_deposit = Investment(my_sum, my_term)
my_bank = Bank(my_deposit)
my_bank.deposit()


