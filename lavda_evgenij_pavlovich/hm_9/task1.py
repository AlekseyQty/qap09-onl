""" Создайте класс book с именем книги, автором, кол-м страниц, ISBN, флагом,
зарезервирована ли книги или нет. Создайте класс пользователь который может брать
книгу, возвращать, бронироать. Если другой пользователь ховчет взять
зарезервированную книгу(или которую уже кто-то читает - надо ему про это сказать)."""


class Book:
    def __init__(self, name, author, leight, isbn, reserved=False):
        self.name = name
        self.author = author
        self.leight = leight
        self.isbn = isbn
        self.reserved = reserved


dostoevski = Book("Idiot", "Dostoevski", 199, 2323)


class User:

    book_list = []
    reserved_list = []

    def get_book(self, book):
        self.book_list.append(book)

    def reserve_book(self, book):
        if book.reserved is False:
            self.book_list.append(book)
            book.reserved = True
        else:
            print("Книга занята")

    def return_book(self, book):
        self.book_list.remove(book)
        book.reserved = False


john = User()
print(john)
john.reserve_book(dostoevski)

print(john.book_list)
