#1.Библиотека

class Book:
    def __init__(self, name, author, papers, isbn, reserved = False, taken = False):
        self.name = name
        self.author = author
        self.papers = papers
        self.isbn = isbn
        self.reserved = reserved
        self.taken = taken

    def user_reserv(self, reserved):
        self.reserved = reserved

    def user_tak(self, taken):
        self.taken = taken

class User_book:
    def __init__(self, name, book = None):
        self.name = name
        self.book = book

    def take_book(self, book):
        if book.taken or book.reserved is True:
            print('No book distribution')

        else:
            print('You took the book')
            self.book = book
            book.user_tak(True)

    def return_book(self, book):
        book.user_tak(False)
        self.book = None
        print('You returned book')

    @staticmethod
    def reserve_book(book):
        if book.taken or book.reserved is True:
            print('All books reserved')

        else:
            print('You reserved book')
            book.user_reserv(True)

user_1 = User_book("Bob")
user_2 = User_book("Jone")

book_1 = Book('Post Office', 'Charles Bukowski', 224, 9785699908929, False, False)
book_2 = Book('Picture of Dorian Gray', 'Oscar Wilde', 320, 9785179829188, False, False)

user_1.reserve_book(book_2)
user_2.take_book(book_1)
user_1.take_book(book_1)

#2.Банковский вклад

class Investment:
    def __init__(self, money, year, percent):
        self.money = money
        self.year = year
        self.percent = percent

class Bank:

    @staticmethod
    def deposit(invest):
        total = invest.money * (1 + invest.percent / 100 / 12) ** (invest.year * 12)
        return f'Your {invest.money} deposit' \
               f'afret {invest.year} years of investment' \
               f'at {invest.percent}% per month: <{total}>'


investor = Investment(5000, 10, 10)
bank = Bank()
print(bank.deposit(investor))