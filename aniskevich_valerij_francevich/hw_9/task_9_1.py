# 1.Библиотека
# Создайте класс book с именем книги, автором, кол-м страниц, ISBN, флагом,
# зарезервирована ли книги или нет. Создайте класс пользователь который может брать
# книгу, возвращать, бронировать. Если другой пользователь хочет взять
# зарезервированную книгу(или которую уже кто-то читает - надо ему про это сказать).

class Book:

    def __init__(self, name_book, author, pages, isbn, reserded=False):
        self.name_book = name_book
        self.author = author
        self.pages = pages
        self.isbn = isbn
        self.reserved = reserded


class User:
    def __init__(self, name_user, book=None):
        self.name_user = name_user
        self.book = book

    def take(self, book):
        if book.reserved == False:
            book.reserved = True
            print(f"{self.name_user}, книга '{book.name_book}' взята успешно!")
        else:
            print("Извините, книга забронирована")

    def to_return(self, book):
        book.reserved = False
        print(f"Книга '{book.name_book}' возвращена! Спасибо!")


motivation = Book("Motivation", "Brain Tracy", "144", "9785000571002")
negotiation = Book("Negotiation", "Brain Tracy", "144", "9785000571026")
valera = User("Valera")
valera.take(motivation)
valera.to_return(motivation)
andrei = User("Andrei")
andrei.take(motivation)
