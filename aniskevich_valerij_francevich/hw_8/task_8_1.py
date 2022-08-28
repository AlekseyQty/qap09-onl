# Напишите декоратор, который проверял бы тип параметров функции, конвертировал их
# если надо и складывал:
# @typed(type=’str’)
# def add_two_symbols(a, b):
# return a + b
# add_two_symbols("3", 5) -> "35"
# add_two_symbols(5, 5) -> "55"
# add_two_symbols('a', 'b') -> 'ab’
# @typed(type=’int’)
# def add_three_symbols(a, b, с):
# return a + b + с
# add_three_symbols(5, 6, 7) -> 18
# add_three_symbols("3", 5, 0) -> 8
# add_three_symbols(0.1, 0.2, 0.4) -> 0.7000000000000001

def typed(type=str):
    def my_decorator(func):
        def wrapper(*args):
            args_list = []
            for i in args:
                my_args = type(i)
                args_list.append(my_args)
            result = func(*args_list)
            return result

        return wrapper

    return my_decorator


@typed(type=float)
def add_three_symbols(a, b, c):
    return a + b + c


@typed(type=str)
def add_two_symbols(a, b):
    return a + b


print(add_three_symbols(5, 3, 4))
print(add_two_symbols(5, 5))
print(add_three_symbols(0.1, 0.2, 0.4))
