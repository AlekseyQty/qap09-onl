"""Напишите декоратор, который проверял бы тип параметров функции, конвертировал их
если надо и складывал:"""


def my_parametrized_dec(type):

    def my_dec(func):

        def wrapper(*args):
            b = 0
            c = ""
            if type == int:
                for item in args:
                    b += type(item)
                return b
            else:
                for item in args:
                    c += type(item)
                return c

        return wrapper

    return my_dec


@my_parametrized_dec(type=str)
def add_two_symbols(a, b):
    return a + b


print(add_two_symbols(5, "2"))


@my_parametrized_dec(type=int)
def add_three_symbols(a, b, c):
    return a+b+c


print(add_three_symbols("3", 5, 0))
