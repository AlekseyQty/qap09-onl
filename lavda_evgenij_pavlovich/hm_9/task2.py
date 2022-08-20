"""Создайте класс инвестиция. Который содержит необходимые поля и методы, например
сумма инвестиция и его срок.
Пользователь делает инвестиция в размере N рублей сроком на R лет под 10% годовых
(инвестиция с возможностью ежемесячной капитализации - это означает, что проценты
прибавляются к сумме инвестиции ежемесячно).
Написать класс Bank, метод deposit принимает аргументы N и R, и возвращает сумму,
которая будет на счету пользователя.
формула капитализации S = D * (1+n / 100 / L) T,"""


class Investment:
    def __init__(self, investment_size, deposit_term):
        self.investmet_size = float(investment_size)
        self.deposit_term = float(deposit_term)


my_first = Investment(10000, 12)
print(my_first.investmet_size)


class Bank:
    depisit = []

    @staticmethod
    def get_deposit(investment_size, deposit_tern, investment_rate):
        s = investment_size * (1 + investment_rate / 100 / 12) ** deposit_tern
        return Bank.depisit.append(round(s))


Bank.get_deposit(my_first.investmet_size, 1, 12)
print(Bank.depisit)
