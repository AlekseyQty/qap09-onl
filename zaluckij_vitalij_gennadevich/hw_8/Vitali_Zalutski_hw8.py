# 1.Напишите декоратор, который проверял бы тип параметров функции, конвертировал их
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

print("Hello")

def typed(type):
    def my_decorator(func):
        def wrapper(*args):
            my_args = []
            for i in args:
                i = type(i)
                my_args.append(i)
            func(*my_args)

        return wrapper

    return my_decorator


@typed(type=str)
def add_two_symbols(a, b):
    print(a + b)


@typed(type=int)
def add_three_symbols(a, b, c):
    print(a + b + c)


@typed(type=float)
def add_three_symbols(a, b, c):
    print(a + b + c)


add_two_symbols("3", 5)
add_two_symbols(5, 5)

add_three_symbols(5, 6, 7)
add_three_symbols("3", 5, 0)
add_three_symbols(0.1, 0.2, 0.4)

# 2
# 2.Расчет времени работы функции
# Напишите декоратор, который считает сколько времени работала декорируемая
# функция. Для получения текущего времени можно использовать функцию time.time().
# Для того чтобы искусственно замедлить работу функции можно использовать
# time.sleep()
# Пример работы:
# @timeit
# def my_func():
# some code
# > Function worked for <time> seconds


import time


def timeit(my_func):
    def wrapper(*args):
        start = time.time()
        my_func(*args)
        print(f"Function worked{time.time() - start} seconds")

    return wrapper


@timeit
def func(one, two):
    time.sleep(5)
    return one * two


func(10, 30)