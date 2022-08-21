# 1.Библиотека

class Book:

    def __init__(self, name_book, author, number_of_pages, ISBN, reserved=False):
        self.name = name_book
        self.author = author
        self.number_of_pages = number_of_pages
        self.ISBN = ISBN
        self.reserved = reserved


class Reader:
    def __init__(self, name, book=None):
        self.name = name
        self.book = book

    def take_book(self, the_book):
        self.the_book = the_book
        if the_book.reserved is True:
            print(f"{the_book.name} is unavailable!")
        else:
            the_book.reserved = True
            self.book = the_book
            print(f"{the_book.name} is added to {self.name}")

    def return_book(self, the_book):
        self.the_book = the_book
        if self.book == the_book:
            the_book.reserved = False
            self.book = None
            print(f"{the_book.name} is returned by {self.name}")
        else:
            print("It's nothing to return!")

    def reserve_book(self, the_book):
        self.the_book = the_book
        if the_book.reserved is False:
            the_book.reserved = True
            self.book = the_book
            print(f"{the_book.name} is reserved by {self.name}")
        else:
            print(f"{the_book.name} is unavailable!")


my_book = Book("Best book ever!", "Anjei", 300, 2266111566)
Alex_reader = Reader("Alex")
Boris_reader = Reader("Boris")


# 2.Банковский вклад

class Investment:
    def __init__(self, summ_investment, time_investment):
        self.summ_investment = summ_investment
        self.time_investment = time_investment


class Bank:
    def __init__(self, annual_interest):
        self.annual_interest = annual_interest

    def deposit(self, investment):
        self.investment = investment
        for i in range(investment.time_investment):
            investment.summ_investment = ((investment.summ_investment * (self.annual_interest / 100)) / 12) \
                                         + investment.summ_investment
        total = round(investment.summ_investment, 2)
        print(f"Deposit amount {total}, at the expiration of {investment.time_investment} month.")


my_investment = Investment(1000, 9)
my_bank = Bank(10)
my_bank.deposit(my_investment)
