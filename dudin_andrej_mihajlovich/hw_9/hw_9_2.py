'''Создайте класс инвестиция. Который содержит необходимые поля и методы, например сумма инвестиция и его срок.
Пользователь делает инвестиция в размере N рублей сроком на R лет под 10% годовых (инвестиция с возможностью
ежемесячной капитализации - это означает, что проценты прибавляются к сумме инвестиции ежемесячно).
Написать класс Bank, метод deposit принимает аргументы N и R, и возвращает сумму, которая будет на счету пользователя
'''


class Investment:
    def __init__(self, summ_investment, period, percent=10):
        '''
        :param summ_investment: N
        :param period: R
        :param percent:
        '''
        self.summ_investment = summ_investment
        self.period = period
        self.percent = percent


class Bank:
    """
    Сумма на счету пользователя с учетом ежемесячной капитализации
    balance = summ_investment * (1 + percent / 100 / 12) ** (period * 12)
    """

    @staticmethod
    def deposit(user_invest):
        balance = int(user_invest.summ_investment * (1 + user_invest.percent / 100 / 12) ** (user_invest.period * 12))
        return f"Your balance is {balance} after {user_invest.period} years of investment {user_invest.percent}% per month"


user_invest = Investment(1000, 5)
bank = Bank()
print(bank.deposit(user_invest))
