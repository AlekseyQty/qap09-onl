#1. Декоратор типов
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
def typ(typ_e):
    def decorator(funk):
        def wrapper(*args):
            all_arg = []
            for arg in args:
                if isinstance(arg, float):
                    all_arg.append(arg)
                else:
                    arg = typ_e(arg)
                    all_arg.append(arg)
            funk(*all_arg)
        return wrapper
    return decorator


@typ(typ_e=str)
def add_two_symbols(a, b):
    print(a + b)

add_two_symbols("3", 5)
add_two_symbols(5, 5)
add_two_symbols('a', 'b')

@typ(typ_e = int)
def add_three_symbols(a, b, с):
    print(a + b + с)

add_three_symbols(5, 6, 7)
add_three_symbols("3", 5, 0)
add_three_symbols(0.1, 0.2, 0.4)


#2. Расчет времени работы функции
import time

def my_fun_time(fun):

    def fun_time():

        start = time.perf_counter()
        fun()
        stop = time.perf_counter()

        return print(f'Function worked for <{stop - start:0.6f}> seconds')

    return fun_time

@my_fun_time
def generator():

    my_list = [1, 2, 3, 4, 5, 6]
    new_my_list = []

    for i in my_list:
        if i % 2:
            new_my_list.append(i)

    return new_my_list

generator()
