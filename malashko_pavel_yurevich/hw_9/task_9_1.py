class Book:
    def __init__(self, book_name, author_name, page_count, isbn, book_is_reserved=False, book_is_taken=False):
        self.book_name = book_name
        self.author_name = author_name
        self.page_count = page_count
        self.isbn = isbn
        self.book_is_reserved = book_is_reserved
        self.book_is_taken = book_is_taken


class User:
    def __init__(self, name, book=None):
        self.name = name
        self.book = book

    def take_book(self, book):
        if book.book_is_taken or book.book_is_reserved:
            print(f"Sorry, book {book.book_name} - {book.author_name} isn't available now.\nYou can take next books:")
            for book in books:
                if book.book_is_taken is False and book.book_is_reserved is False:
                    print(f"\t{book.book_name} - {book.author_name}")
        else:
            print(f'You have taken {book.book_name} - {book.author_name}')
            self.book = book
            book.book_is_taken = True
            book.book_is_reserved = True

    def return_book(self, book):
        self.book = None
        book.book_is_taken = False
        book.book_is_reserved = False

    @staticmethod
    def reserve_book(book):
        if book.book_is_taken or book.book_is_reserved:
            print(f"Sorry, book {book.book_name} - {book.author_name} isn't available now.\nYou can reserve next books:")
            for book in books:
                if book.book_is_taken is False and book.book_is_reserved is False:
                    print(f"\t{book.book_name} - {book.author_name}")
        else:
            print(f'You have reserved {book.book_name} - {book.author_name}')
            book.book_is_reserved = True


books = [Book("War and Peace", "Leo Tolstoy", 1408, "0-4329-8854-8"),
         Book("The master and Margarita", "Mikhail Bulgakov", 345, "1-1529-1858-7"),
         Book("1984", "George Orwell", 321, "2-3421-1471-6"),
         Book("Three laws of Robotics", "Isaac Asimov", 286, "1-1529-1858-7")]

user1 = User("Pasha")
user2 = User("Misha")


user2.take_book(books[1])
user1.reserve_book(books[3])
user1.take_book(books[2])
user1.return_book(books[2])

print(user2.book.book_name)
print(user1.book)



