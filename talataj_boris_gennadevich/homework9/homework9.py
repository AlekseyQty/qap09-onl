#1.Библиотека
# Создайте класс book с именем книги, автором, кол-м страниц, ISBN, флагом,
# зарезервирована ли книги или нет. Создайте класс пользователь который может брать
# книгу, возвращать, бронировать. Если другой пользователь хочет взять
# зарезервированную книгу(или которую уже кто-то читает - надо ему про это сказать).

class Book:
    def __init__(self, name, author, pages, number, reserved = False, taken = False):
        self.name = name
        self.author = author
        self.pages = pages
        self.number = number
        self.reserved = reserved
        self.taken = taken

    def user_reserved(self, reserved):
        self.reserved = reserved

    def user_taken(self, taken):
        self.taken = taken

class User:
    def __init__(self, name, book=None):
        self.name = name
        self.book = book

    def take_book(self, book):
        if book.taken or book.reserved is True:
            print(f'Book: <{book.name} - {book.author}> is not available')
        else:
            print(f'You took the book: <{book.name} - {book.author}>')
            self.book = book
            book.user_taken(True)

    def return_book(self, book):
        book.user_taken(False)
        self.book = None
        print(f'You return book: <{book.name} - {book.author}>')

    @staticmethod
    def reserve_book(book):
        book.user_reserved(True)
        print(f'You reserved book: <{book.name} - {book.author}>')

user_1 = User("Boris")
user_2 = User("Alex")
user_3 = User("John")

book_1 = Book('Пигмей', 'Чак Паланик', 317, 978517097605-8, False, False)
book_2 = Book('Зов Ктулху, Говард Филлипс Лавкрафт', 633, 978-5-38906607-7, False, False)
book_3 = Book('Война и мир книга 2, Л.Н. Толостой', 718, 4702010100096, False,False)

user_1.reserve_book(book_3)
user_2.take_book(book_2)
user_3.return_book(book_1)
user_3.take_book(book_3)
user_1.take_book(book_2)


#2.Банковский вклад. Создайте класс инвестиция. Который содержит необходимые поля и методы, например
# сумма инвестиция и его срок. Пользователь делает инвестиция в размере N рублей сроком на R лет под 10% годовых
# (инвестиция с возможностью ежемесячной капитализации - это означает, что проценты
# прибавляются к сумме инвестиции ежемесячно).
# Написать класс Bank, метод deposit принимает аргументы N и R, и возвращает сумму, которая будет на счету пользователя.

class Investment:
    def __init__(self, money, year, percent):
        self.money = money
        self.year = year
        self.percent = percent

class Bank:
    @staticmethod
    def deposit(invest):
        total = invest.money * (1 + invest.percent / 100 / 12) ** (invest.year * 12)
        return f'Your {invest.money} deposit'\
               f'after {invest.year} years of investment'\
               f'at {invest.percent} % per month: < {total} >'

investor = Investment(7500, 10, 10)
bank = Bank()
print(bank.deposit(investor))

