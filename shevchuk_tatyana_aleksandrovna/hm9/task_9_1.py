# Создайте класс book с именем книги, автором, кол-м страниц, ISBN, флагом,
# зарезервирована ли книга или нет. Создайте класс пользователь который может
# брать книгу, возвращать, бронировать. Если другой пользователь хочет взять
# зарезервированную книгу (или которую уже кто-то читает - надо ему про это сказать)


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
            return f"You can't reserve the book {book.book_name}. " \
                   f"Sorry, this book is reserved. "
        else:
            book.book_is_reserved(True)
            return f"You reserved the book {book.book_name}"

    def user_take_a_book(self, book):
        if book.reserved or book.taken is True:
            return f"The book {book.book_name} was taken by other user. You have to wait"
        else:
            book.book_is_taken(True)
            self.book = book
            return f"You took the book {book.book_name} by {book.author}"

    def return_a_book(self, book):
        book.book_is_taken(False)
        self.book = None
        return f"You returned the book {book.book_name} by {book.author}"


book_1 = Book("The 7 Habits of Highly Effective People", "Stephen Covey", 9780747532743)
book_2 = Book("Thinking, Fast and Slow", "Daniel Kahneman")
book_3 = Book("Man's Search for Meaning", "Viktor E. Frankl", 355, 1503222683)
book_4 = Book("The Subtle Art of Not Giving a F*ck", "Mark Manson")

user_1 = User("Tanya")
user_2 = User("Alex")
user_3 = User("Elena")

print(user_2.user_take_a_book(book_1))
print(user_1.user_take_a_book(book_1))
print(user_1.user_reserve_a_book(book_4))
print(user_3.user_reserve_a_book(book_4))
print(user_2.return_a_book(book_3))
