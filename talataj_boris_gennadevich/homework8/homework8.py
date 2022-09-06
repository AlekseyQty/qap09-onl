#Напишите декоратор, который проверял бы тип параметров функции, конвертировал их если надо и складывал:


def typed(type):
    def decorator(function):
        def wrapper(*args):
            first_arg = []
            for arg in args:
                if isinstance(arg, float):
                    first_arg.append(arg)
                else:
                    arg = type(arg)
                    first_arg.append(arg)
            function(*first_arg)
        return wrapper
    return decorator

@typed(type = str)
def add_two_symbols(a, b):
    print(a + b)

add_two_symbols("3", 5)    # -> "35"
add_two_symbols(5, 5)      # -> "55"
add_two_symbols('a', 'b')  # -> 'ab'

@typed(type = int)
def add_three_symbols(a, b, c):
    print(a + b + c)

add_three_symbols(5, 6, 7)   # -> 18
add_three_symbols("3", 5, 0) # -> 8
add_three_symbols(0.1, 0.2, 0.4) # -> 0.7000000000001

#Расчет времени работы функции

import time

def timeit(func):
    def wrapper(*args):
        start = time.time()
        func(*args)
        end = time.time()

        print(f'Function worked for {end - start} seconds')

    return wrapper

@timeit
def sleepy_func(sleep_amount):
    for i in range(100):
        print(i)
    time.sleep(sleep_amount)

@timeit
def func_1():
    num = []
    for i in range(100000):
        num.append(i)


@timeit
def func_2():
    num = []
    my_range = list(range(100000))
    for i in my_range:
        num.append(i)

func_1()
func_2()













