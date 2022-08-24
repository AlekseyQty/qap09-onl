'''
Напишите декоратор, который проверял бы тип параметров функции, конвертировал их
если надо и складывал:
'''


def typed(type):
    def decorator(func):
        def wrapper(*args):
            result = []
            for arg in args:
                arg = type(arg)
                result.append(arg)
            func(*result)
        return wrapper
    return decorator

@typed(type = str)
def add_two_symbols(a, b):
    print(a + b)

@typed(type = int)
def add_three_symbols(a, b, с):
    print(a + b + с)

@typed(type = float)
def add_three_symbols(a, b, с):
    print(a + b + с)

add_two_symbols("3", 5)

add_three_symbols("3", 5, 0)
add_three_symbols(0.1, 0.2, 0.4)