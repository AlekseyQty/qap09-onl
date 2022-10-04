# 2.Банковский вклад
# Создайте класс инвестиция. Который содержит необходимые поля и методы, например
# сумма инвестиция и его срок.
# Пользователь делает инвестиция в размере N рублей сроком на R лет под 10% годовых
# (инвестиция с возможностью ежемесячной капитализации - это означает, что проценты
# прибавляются к сумме инвестиции ежемесячно).
# Написать класс Bank, метод deposit принимает аргументы N и R, и возвращает сумму,
# которая будет на счету пользователя.
class Investment:
    def __init__(self, sum, term):
        self.sum = sum
        self.term = term


class Bank:
    def deposit(self, investment):
        self.sum = investment.sum
        self.term = investment.term
        for i in range(self.term*12):
            self.sum = self.sum + self.sum*0.10/12
        self.income = int(self.sum)
        print(f"Your investment:{investment.sum}$ will make a profit:{self.income}$ in {self.term} years ")


valera = Investment(3000, 6)
investment = Bank()
investment.deposit(valera)

