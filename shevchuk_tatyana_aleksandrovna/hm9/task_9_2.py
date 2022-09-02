# Создайте класс инвестиция. Который содержит необходимые поля и методы, например сумма инвестиция и его срок.
# Пользователь делает инвестиция в размере N рублей сроком на R лет под 10% годовых (инвестиция с возможностью
# ежемесячной капитализации - это означает, что проценты прибавляются к сумме инвестиции ежемесячно).
# Написать класс Bank, метод deposit принимает аргументы N и R, и возвращает сумму, которая будет на счету пользователя


class Investment:
    def __init__(self, sum_investment, year, percent):
        self.sum_investment = sum_investment
        self.year = year
        self.percent = percent


class Bank:

    """
    Расчет суммы, которая будет на счету пользователя, с учетом ежемесячной капитализации
    balance = sum_investment * (1 + percent / 100 / 12) ** (year * 12)
    """

    @staticmethod
    def deposit(money):
        balance = money.sum_investment * (1 + money.percent / 100 / 12) ** (money.year * 12)
        return f"Your balance is {balance} after {money.year} years of investment " \
               f"at {money.percent}% per month"


investment = Investment(150, 3, 10)
bank = Bank()
print(bank.deposit(investment))
