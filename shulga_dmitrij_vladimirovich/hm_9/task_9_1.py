# Создайте класс book с именем книги, автором, кол-м страниц, ISBN, флагом, зарезервирована ли книги или нет.
# Создайте класс пользователь который может брать книгу, возвращать, бронировать. Если другой пользователь хочет взять
# зарезервированную книгу(или которую уже кто-то читает - надо ему про это сказать).

name_reader = ""
list_riders = {}
status_reserved = ['Free', 'Free', 'Free']
while name_reader != "quit":
    name_reader = input("Please enter your namer and 'quit' if you want exit: ")
    if name_reader == "quit":
        print("Goodbye")
        break
    else:

        class Reader:

            def __init__(self, name_reader, number_book, status_book):
                self.name_reader = name_reader
                self.number_book = number_book
                self.status_book = status_book

            def reader_choice(self):

                if self.number_book == 1:
                    self.number_book = "Three Comrades"
                elif self.number_book == 2:
                    self.number_book = "All Quiet on the Western Front"
                elif self.number_book == 3:
                    self.number_book = "Heaven Has No Favorites"

                if self.number_book == "Three Comrades" and status_reserved[0] == 'Reserved':
                    if self.name_reader in list_riders.keys():
                        for v in list_riders[self.name_reader]:
                            if v == self.number_book:
                                print("You have already reserved this book")
                                my_answer = input("You want to give it up: yes/no?: ")
                                if my_answer == "yes":
                                    status_reserved[0] = "Free"
                                    self.number_book = "Empty"
                                    del list_riders[self.name_reader]
                                    print("You want to cancel your booking")
                    else:
                        print("Sory book was reserved")

                elif self.number_book == "Three Comrades" and status_reserved[0] == 'Taken':
                    if self.name_reader in list_riders.keys():
                        for v in list_riders[self.name_reader]:
                            if v == self.number_book:
                                print("You have already taken this book")
                                my_answer = input("You want to give it up: yes/no?: ")
                                if my_answer == "yes":
                                    status_reserved[0] = "Free"
                                    self.number_book = "Empty"
                                    del list_riders[self.name_reader]
                                    print("You return this book")
                    else:
                        print("Sory book was taken")

                elif self.number_book == "All Quiet on the Western Front" and status_reserved[1] == 'Reserved':
                    if self.name_reader in list_riders.keys():
                        for v in list_riders[self.name_reader]:
                            if v == self.number_book:
                                print("You have already reserved this book")
                                my_answer = input("You want to give it up: yes/no?: ")
                                if my_answer == "yes":
                                    status_reserved[1] = "Free"
                                    self.number_book = "Empty"
                                    del list_riders[self.name_reader]
                                    print("You want to cancel your booking")
                    else:
                        print("Sory book was reserved")

                elif self.number_book == "All Quiet on the Western Front" and status_reserved[1] == 'Taken':
                    if self.name_reader in list_riders.keys():
                        for v in list_riders[self.name_reader]:
                            if v == self.number_book:
                                print("You have already taken this book")
                                my_answer = input("You want to give it up: yes/no?: ")
                                if my_answer == "yes":
                                    status_reserved[1] = "Free"
                                    self.number_book = "Empty"
                                    del list_riders[self.name_reader]
                                    print("You return this book")
                    else:
                        print("Sory book was taken")

                elif self.number_book == "Heaven Has No Favorites" and status_reserved[2] == 'Reserved':
                    if self.name_reader in list_riders.keys():
                        for v in list_riders[self.name_reader]:
                            if v == self.number_book:
                                print("You have already reserved this book")
                                my_answer = input("You want to give it up: yes/no?: ")
                                if my_answer == "yes":
                                    status_reserved[2] = "Free"
                                    self.number_book = "Empty"
                                    del list_riders[self.name_reader]
                                    print("You want to cancel your booking")
                    else:
                        print("Sory book was reserved")

                elif self.number_book == "Heaven Has No Favorites" and status_reserved[2] == 'Taken':
                    if self.name_reader in list_riders.keys():
                        for v in list_riders[self.name_reader]:
                            if v == self.number_book:
                                print("You have already taken this book")
                                my_answer = input("You want to give it up: yes/no?: ")
                                if my_answer == "yes":
                                    status_reserved[2] = "Free"
                                    self.number_book = "Empty"
                                    del list_riders[self.name_reader]
                                    print("You return this book")
                    else:
                        print("Sory book was taken")

                else:
                    print("Choice what you want:")
                    print("   a - I want take book")
                    print("   b - I wan reserved book")

                    self.status_book = input("Please select an action: ")

                    if self.status_book == "a" and self.number_book == "Three Comrades":
                        self.status_book = "Taken"
                        status_reserved[0] = 'Taken'
                        print("You take this book")

                    elif self.status_book == "a" and self.number_book == "All Quiet on the Western Front":
                        self.status_book = "Taken"
                        status_reserved[1] = 'Taken'
                        print("You take this book")

                    elif self.status_book == "a" and self.number_book == "Heaven Has No Favorites":
                        self.status_book = "Taken"
                        status_reserved[2] = 'Taken'
                        print("You take this book")

                    elif self.status_book == "b" and self.number_book == "Three Comrades":
                        self.status_book = "Reserved"
                        status_reserved[0] = 'Reserved'
                        print("You reserved this book")

                    elif self.status_book == "b" and self.number_book == "All Quiet on the Western Front":
                        self.status_book = "Reserved"
                        status_reserved[1] = 'Reserved'
                        print("You reserved this book")

                    elif self.status_book == "b" and self.number_book == "Heaven Has No Favorites":
                        self.status_book = "Reserved"
                        status_reserved[2] = 'Reserved'
                        print("You reserved this book")

                list_riders[self.name_reader] = [self.number_book, self.status_book]


            def descriptive_reader(self):
                reader_count = 0
                print("List of readers")
                for key, value in list_riders.items():
                    reader_count += 1
                    print(f"   {reader_count} - {key}; Name book: {value[0]}; Status: {value[1]}")

        class Book:

            book_count = 1
            def __init__(self, name_book, author, number_pages, isbn, reserved):
                self.name_book = name_book
                self.author = author
                self.number_pages = number_pages
                self.isbn = isbn
                self.reserved = reserved

            def descriptive_book(self):
                book_name = f"   {Book.book_count} - {self.name_book}; {self.author}; {self.number_pages}; {self.isbn}"
                Book.book_count += 1
                return book_name


        print("Names books:")
        my_new_book_1 = Book("Three Comrades", "Remarque Erich Maria", 480, "ISBN: 978-5-17-004252-4",
        status_reserved[0])
        print(my_new_book_1.descriptive_book())
        my_new_book_2 = Book("All Quiet on the Western Front", "Remarque Erich Maria", 200, "ISBN: 978-5-17-088940-2",
        status_reserved[1])
        print(my_new_book_2.descriptive_book())
        my_new_book_3 = Book("Heaven Has No Favorites", "Remarque Erich Maria", 288, "ISBN: 978-5-17-081140-3",
        status_reserved[2])
        print(my_new_book_3.descriptive_book())


        number_book = input("Please select number book: ")
        number_book = int(number_book)
        my_reader = Reader(name_reader, number_book, "Free")
        my_reader.reader_choice()
        my_reader.descriptive_reader()
