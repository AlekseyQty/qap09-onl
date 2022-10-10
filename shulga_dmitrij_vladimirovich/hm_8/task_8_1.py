# Напишите декоратор, который проверял бы тип параметров функции, конвертировал их если надо и складывал:

def typed(type):

    def decorator(func):

        def wrapper(*args):

            new_arg = []
            for arg in args:
                arg = type(arg)
                new_arg.append(arg)

            func(*new_arg)

        return wrapper
    return decorator

@typed(type = str)
def add_two_symbols(a, b):
    print(a + b)

@typed(type = int)
def add_three_symbols(a, b, с):
    print(a + b + с)


add_two_symbols("3", 5)

add_three_symbols("3", 5, 0)
