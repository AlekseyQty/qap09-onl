'''
Создайте класс book с именем книги, автором, кол-м страниц, ISBN, флагом,
зарезервирована ли книги или нет. Создайте класс пользователь который может брать
книгу, возвращать, бронировать. Если другой пользователь хочет взять
зарезервированную книгу(или которую уже кто-то читает - надо ему про это сказать).
'''

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
        if book.reserved or book.taken:
            return f"You can not take this book '{book.book_name}' because reserved."

        else:
            book.book_is_reserved(reserved=True)
            return f"Done. You reserve the book '{book.book_name}'"

    def user_take_a_book(self, book):
        if book.reserved or book.taken:
            return f"The book '{book.book_name}' was taken by other user. You have to wait"
        else:
            book.book_is_taken(taken=True)
            self.book = book
            return f"You take the book '{book.book_name}' by {book.author}"

    def return_a_book(self, book):
        book.book_is_taken(taken=False)
        self.book = None
        return f"You return the book '{book.book_name}' by {book.author}"

user_1 = User("Джон")
user_2 = User("Мария")
user_3 = User("Сергей")

book_1 = Book("Война и мир", "Толстой Л.Н.", 223322)
book_2 = Book("Анна Каренина", "Толстой Л.Н.", 100,578678678)
book_3 = Book("Robinzon Cruzo", "Defo D.", pages=70)
book_4 = Book(author="М. Митчелл", book_name="Унесенные ветром",)



print(user_1.user_take_a_book(book_1))
print(user_1.user_take_a_book(book_3))
print(user_2.user_reserve_a_book(book_4))
print(user_1.user_reserve_a_book(book_4))
print(user_2.return_a_book(book_1))


