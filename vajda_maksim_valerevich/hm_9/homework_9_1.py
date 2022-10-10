# 1.Библиотека
# Создайте класс book с именем книги, автором, кол-м страниц, ISBN, флагом,
# зарезервирована ли книги или нет. Создайте класс пользователь который может брать
# книгу, возвращать, бронировать. Если другой пользователь хочет взять
# зарезервированную книгу(или которую уже кто-то читает - надо ему про это сказать).


class Book:

    def __init__(self, name, author, pages, isbn, reserved, taken):
        self.name = name
        self.author = author
        self.pages = pages
        self.isbn = isbn
        self.reserved = reserved
        self.taken = taken

    def user_reserved(self, reserved):
        self.reserved = reserved

    def user_taken(self, taken):
        self.taken = taken


class User:

    @staticmethod
    def take_book(book):
        if book.taken or book.reserved is True:
            print(f'Book: <{book.name} - {book.author}> is not available')
        else:
            print(f'You took the book: <{book.name} - {book.author}>')
            book.user_taken(True)

    @staticmethod
    def return_book(book):
        book.user_taken(False)
        print(f'You returned book: <{book.name} - {book.author}>')

    @staticmethod
    def reserve_book(book):
        book.user_reserved(True)
        print(f'You reserved book: <{book.name} - {book.author}>')


user_1 = User()
user_2 = User()
user_3 = User()

book_1 = Book('1984', 'George Orwell', 328, 9789857210565, False, False)
book_2 = Book('Мы', 'Евгений Замятин', 429, 9785080057847, False, False)
book_3 = Book('Fahrenheit 451', 'Ray Bradbury', 256, 9780743247221, False, False)

user_1.reserve_book(book_3)
user_2.take_book(book_2)
user_3.return_book(book_1)
user_3.take_book(book_3)
user_1.take_book(book_2)
