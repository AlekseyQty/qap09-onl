# 2.Банковский вклад
# Создайте класс инвестиция. Который содержит необходимые поля и методы, например
# сумма инвестиция и его срок.
# Пользователь делает инвестиция в размере N рублей сроком на R лет под 10% годовых
# (инвестиция с возможностью ежемесячной капитализации - это означает, что проценты
# прибавляются к сумме инвестиции ежемесячно).
# Написать класс Bank, метод deposit принимает аргументы N и R, и возвращает сумму,
# которая будет на счету пользователя.


class Investment:
    def __init__(self, money, year, percent):
        self.money = money
        self.year = year
        self.percent = percent


class Bank:
    """
    Monthly capitalization:
    total = money * (1 + percent/100/12)**(year*12)
    """

    @staticmethod
    def deposit(invest):
        total = invest.money * (1 + invest.percent / 100 / 12) ** (invest.year * 12)
        return f'Your {invest.money} deposit ' \
               f'after {invest.year} years of investment' \
               f' at {invest.percent}% per month: < {total} >'


investor = Investment(5000, 10, 10)
bank = Bank()
print(bank.deposit(investor))
