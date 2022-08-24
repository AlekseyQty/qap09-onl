# Создайте класс book с именем книги, автором, кол-м страниц, ISBN, флагом,
# зарезервирована ли книга или нет. Создайте класс пользователь который может
# брать книгу, возвращать, бронировать. Если другой пользователь хочет взять
# зарезервированную книгу (или которую уже кто-то читает - надо ему про это сказать)

print("-" * 25 + "Library" + "-" * 25)

class Book:
    def __init__(self, book_name, author, pages=None, isbn=None, reserved=False, taken=False):
        self.book_name = book_name
        self.author = author
        self.pages = pages
        self.isbn = isbn
        self.reserved = reserved
        self.taken = taken

    def book_is_taken(self, taken):
        self.taken = taken

    def book_is_reserved(self, reserved):
        self.reserved = reserved


class User:
    def __init__(self, user_name, book=None):
        self.user_name = user_name
        self.book = book

    @staticmethod
    def user_reserve_a_book(book):
        if book.reserved or book.taken is True:
            return f"You can not reserve the book {book.book_name}. " \
                   f"This book was reserved/taken by other user. " \
                   f"You have to wait"
        else:
            book.book_is_reserved(True)
            return f"You reserve the book {book.book_name}"

    def user_take_a_book(self, book):
        if book.reserved or book.taken is True:
            return f"The book {book.book_name} was taken by other user. You have to wait"
        else:
            book.book_is_taken(True)
            self.book = book
            return f"You take the book {book.book_name} by {book.author}"

    def return_a_book(self, book):
        book.book_is_taken(False)
        self.book = None
        return f"You return the book {book.book_name} by {book.author}"


book_1 = Book("Harry Potter and the Philosopher's Stone", "J. K. Rowling", 9780747532743)
book_2 = Book("The Wonderful Wizard of Oz", "L. Frank Baum")
book_3 = Book("Alice's Adventures in Wonderland", "Lewis Carroll", 70, 1503222683)
book_4 = Book("Winnie the Pooh", "A. Milne")

user_1 = User("Mary")
user_2 = User("Vitaliy")
user_3 = User("Max")

print(user_2.user_take_a_book(book_3))
print(user_1.user_take_a_book(book_3))
print(user_1.user_reserve_a_book(book_4))
print(user_3.user_reserve_a_book(book_4))
print(user_2.return_a_book(book_3))


# Создайте класс инвестиция. Который содержит необходимые поля и методы, например сумма инвестиция и его срок.
# Пользователь делает инвестиция в размере N рублей сроком на R лет под 10% годовых (инвестиция с возможностью
# ежемесячной капитализации - это означает, что проценты прибавляются к сумме инвестиции ежемесячно).
# Написать класс Bank, метод deposit принимает аргументы N и R, и возвращает сумму, которая будет на счету пользователя

print("-" * 25 + "Bank deposit" + "-" * 25)


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


investment = Investment(100, 5, 10)
bank = Bank()
print(bank.deposit(investment))