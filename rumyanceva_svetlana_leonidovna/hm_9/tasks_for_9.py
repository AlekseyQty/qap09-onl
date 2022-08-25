# 1. Библиотека. Создайте класс Book с именем книги, автором, кол-м страниц, ISBN, флагом, зарезервирована ли книги или
# нет. Создайте класс пользователь, который может брать книгу, возвращать, бронировать. Если другой пользователь хочет
# взять зарезервированную книгу(или которую уже кто-то читает - надо ему про это сказать).
class Book:

    def __init__(self, book_name, author, num_pages, isbn, is_reserved=None):
        self.book_name = book_name
        self.author = author
        self.num_pages = num_pages
        self.isbn = isbn
        self.is_reserved = is_reserved


class Reader:
    def __init__(self, reader_name, book=None):
        self.reader_name = reader_name
        self.book = book

    def take_book(self, book):
        if book.is_reserved == "no":
            book.is_reserved = "yes"
            return f"{self.reader_name}, you can take the book '{book.book_name}' by {book.author}"
        else:
            return f"{self.reader_name},you can't take the book '{book.book_name}' by {book.author}, it's not available"
        # return book.author

    def return_book(self, book):
        book.is_reserved = "no"
        return f"{self.reader_name} has returned the book '{book.book_name}' by {book.author}"

    def reserve_book(self, book):
        if book.is_reserved == "yes":
            return f"{self.reader_name}, you can't reserve the book '{book.book_name}' by {book.author}"
        else:
            book.is_reserved = "yes"
            return f"{self.reader_name}, you have reserved the book '{book.book_name}' by {book.author}"


book1 = Book("The Godfather", "Mario Puzo", "325", "1-2-266-11156-0", "yes")
book2 = Book("The Great Expectations", "Charles Dickens", "280", "978-3-16-148410-0", "no")
book3 = Book("The Great Gatsby", "Francis Scott Key Fitzgerald", "286", "0-3-42-15236-0", "no")
book4 = Book("The Catcher in the Rye", "Jerome David Salinger", "180", "0-2-356-18656-0", "yes")
book5 = Book("Treasure Island", "Robert Louis Balfour Stevenson", "190", "0-2-356-16521-0", "no")
book6 = Book("Dear John", "Nicholas Sparks", "230", "1-2-340-12540-0", "yes")

reader1 = Reader("Tom Scott")
reader2 = Reader("Jack Vilson")
reader3 = Reader("Ben Dodson")
print(reader1.take_book(book1))
print(reader2.return_book(book1))
print(reader1.reserve_book(book1))
print(reader3.reserve_book(book1))
print(reader1.take_book(book2))

print("-----Task2--------------")
# 2. Банковский вклад. Создайте класс инвестиция. Который содержит необходимые поля и методы, например сумма инвестиции
# и его срок. Пользователь делает инвестиция в размере N рублей сроком на R лет под 10% годовых (инвестиция с
# возможностью ежемесячной капитализации - это означает, что проценты прибавляются к сумме инвестиции ежемесячно).
# Написать класс Bank, метод deposit принимает аргументы N и R, и возвращает сумму, которая будет на счету пользователя.


class Bank:
    @staticmethod
    def deposit(invest):
        months = invest.years * 12
        for _ in range(1, months + 1):
            invest.amount += invest.amount * (0.1 / 12)
        return f"Total amount in the account is {invest.amount}"


class Investment:
    def __init__(self, amount, years):
        self.amount = amount
        self.years = years


invest1 = Investment(100000, 2)
print(Bank.deposit(invest1))
