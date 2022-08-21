# Создайте класс инвестиция. Который содержит необходимые поля и методы, например сумма инвестиция и его срок.
# Пользователь делает инвестиция в размере N рублей сроком на R лет под 10% годовых (инвестиция с возможностью ежемесячной
# капитализации - это означает, что проценты прибавляются к сумме инвестиции ежемесячно).
# Написать класс Bank, метод deposit принимает аргументы N и R, и возвращает сумму, которая будет на счету пользователя.

class Bank:

    def __init__(self, sum, term):
        self.sum = sum
        self.term = term

    def deposit(self):
        result = 0
        for i in range(self.term * 12):
            self.sum = (self.sum * 0.1)/12 + self.sum
            result = self.sum
        print(f"Result: {round(result, 2)}")

sum = input("Please enter your sum: ")
sum = int(sum)
term = input("Please enter your term in years: ")
term = int(term)

my_deposit = Bank(sum, term)
my_deposit.deposit()

