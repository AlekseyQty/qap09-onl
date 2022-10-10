# Создайте класс book с именем книги, автором, кол-м страниц, ISBN, флагом, зарезервирована ли книги или нет.
# Создайте класс пользователь который может брать книгу, возвращать, бронировать. Если другой пользователь хочет взять
# зарезервированную книгу(или которую уже кто-то читает - надо ему про это сказать).

class Reader:

    def __init__(self, name_reader, number_book=None):
        self.name_reader = name_reader
        self.number_book = number_book

    def reader_choice(self, number_book):
        if number_book.is_reserved is True:
            if self.name_reader in list_riders.keys():
                for v in list_riders[self.name_reader]:
                    if v == number_book.name_book:
                        print("You have already reserved this book")
                        my_answer = input("You want to give it up: yes/no?: ")
                        if my_answer == "yes":
                            number_book.is_reserved = False
                            self.number_book = None
                            del list_riders[self.name_reader]
                            print("You want to cancel your booking")
            else:
                print("Sorry book was reserved")

        elif number_book.is_taken is True:
            if self.name_reader in list_riders.keys():
                for v in list_riders[self.name_reader]:
                    if v == number_book.name_book:
                        print("You have already reserved this book")
                        my_answer = input("You want to give it up: yes/no?: ")
                        if my_answer == "yes":
                            number_book.is_taken = False
                            self.number_book = None
                            del list_riders[self.name_reader]
                            print("You want to cancel your booking")
            else:
                print("Sorry book was taken")
                list_riders[self.name_reader] = [None, None, None]

        else:
            print("Choice what you want:")
            print("   a - I want take book")
            print("   b - I wan reserved book")

            status_book = input("Please select an action: ")

            if status_book == "a":
                number_book.is_taken = True
                print("You take this book")
                list_riders[self.name_reader] = [number_book.name_book, number_book.is_taken, number_book.is_reserved]

            elif status_book == "b":
                number_book.is_reserved = True
                print("You reserved this book")
                list_riders[self.name_reader] = [number_book.name_book, number_book.is_taken, number_book.is_reserved]

    @staticmethod
    def descriptive_reader():
        reader_count = 0
        print("List of readers")
        for key, value in list_riders.items():
            reader_count += 1
            print(f"   {reader_count} - {key}; Name book: {value[0]}; Is taken: {value[1]}; "
                  f"Is reserved: {value[2]}")


class Book:

    book_count = 1

    def __init__(self, name_book, author, number_pages, isbn, is_reserved=False, is_taken=False):
        self.name_book = name_book
        self.author = author
        self.number_pages = number_pages
        self.isbn = isbn
        self.is_reserved = is_reserved
        self.is_taken = is_taken

    def descriptive_book(self):
        book_name = f"   {Book.book_count} - {self.name_book}; {self.author}; {self.number_pages}; {self.isbn}"
        Book.book_count += 1
        print(book_name)
        return book_name


print("Names books:")
my_new_book_1 = Book("Three Comrades", "Remarque Erich Maria", 480, "ISBN: 978-5-17-004252-4")
my_new_book_1.descriptive_book()
my_new_book_2 = Book("All Quiet on the Western Front", "Remarque Erich Maria", 200, "ISBN: 978-5-17-088940-2")
my_new_book_2.descriptive_book()
my_new_book_3 = Book("Heaven Has No Favorites", "Remarque Erich Maria", 288, "ISBN: 978-5-17-081140-3")
my_new_book_3.descriptive_book()

name = ""
list_riders = {}
while name != "quit":
    name = input("Please enter your namer and 'quit' if you want exit: ")
    if name == "quit":
        print("Goodbye")
        break
    else:

        my_book = input("Please select number book: ")
        my_book = int(my_book)
        my_reader = Reader(name)
        if my_book == 1:
            my_reader.reader_choice(my_new_book_1)
            my_reader.descriptive_reader()
        elif my_book == 2:
            my_reader.reader_choice(my_new_book_2)
            my_reader.descriptive_reader()
        elif my_book == 3:
            my_reader.reader_choice(my_new_book_3)
            my_reader.descriptive_reader()

