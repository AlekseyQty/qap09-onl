class Investment:
    def __init__(self, money, term):
        self.money = money
        self.term = term


class Bank:
    @staticmethod
    def deposit(invest):
        return invest.money * (1 + 10 / 100 / 12) ** (invest.term * 12)


invest1 = Investment(1000, 1)
print(Bank.deposit(invest1))