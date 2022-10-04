# 1.Библиотека
# Создайте класс book с именем книги, автором, кол-м страниц, ISBN, флагом,
# зарезервирована ли книги или нет. Создайте класс пользователь который может брать
# книгу, возвращать, бронировать. Если другой пользователь хочет взять
# зарезервированную книгу(или которую уже кто-то читает - надо ему про это сказать).

class Book:

    def __init__(self, reserded=False):
        self.name_book = "Motivation"
        self.author = "Brain Tracy"
        self.pages = 144
        self.isbn = 9785000571002
        self.reserved = reserded


class User:
    def take(self, book):
        if book.reserved == False:
            name_user = input("Введите своё имя \n")
            self.name_user = name_user
            self.book = book
            book.reserved = True
            print(f"{self.name_user}, книга '{book.name_book}' взята успешно!")
        else:
            print("Извините, книга забронирована")

    def to_return(self, book):
        book.reserved = False
        print(f"Книга '{book.name_book}' возвращена! Спасибо!")



motivation = Book()
user = User()
user.take(motivation)
user.to_return(motivation)
user2 = User()
user2.take(motivation)
