import time
from functools import wraps
import help_decorator

# Напишите декоратор, который считает сколько времени работала декорируемая функция.
# Для получения текущего времени можно использовать функцию time.time().
# Для того чтобы искусственно замедлить работу функции можно использовать time.sleep()

print(("-")*25 + "Расчет времени работы функции" + ("-")*25)


def timeit(func_to_decorate):
    @wraps(func_to_decorate)
    def wrapper():
        start_time = time.time()
        result = func_to_decorate()
        time.sleep(1)
        end_time = time.time()
        print(f"Function worked for {end_time - start_time} seconds")
        return result
    return wrapper


@timeit
def my_func_loop():
    even_loop = []
    for i in range(20):
        if i % 2 == 0:
            even_loop.append(i)
    return even_loop


@timeit
def my_func_gen():
    even_gen = [i for i in range(20) if i % 2 == 0]
    return even_gen


print("My_func_loop:", my_func_loop())
print("Name:", my_func_loop.__name__)

print("My_func_gen:", my_func_gen())
print("Name:", my_func_gen.__name__)


# Напишите декоратор, который проверял бы тип параметров функции, конвертировал их если надо и складывал:
# @typed(type=’str’)
# def add_two_symbols(a, b):
#     return a + b
#
# add_two_symbols("3", 5) -> "35"
# add_two_symbols(5, 5) -> "55"
# add_two_symbols('a', 'b') -> 'ab’
#
# @typed(type=’int’)
# def add_three_symbols(a, b, с):
#     return a + b + с
#
# add_three_symbols(5, 6, 7) -> 18
# add_three_symbols("3", 5, 0) -> 8
# add_three_symbols(0.1, 0.2, 0.4) -> 0.7000000000000001


def typed(style):
    def my_decorator(func_to_decorate):
        @wraps(func_to_decorate)
        def wrapper(*args):
            my_args = []
            for el in args:
                if isinstance(el, float):
                    my_args.append(el)
                else:
                    el = style(el)
                    my_args.append(el)
            func_to_decorate(*my_args)
        return wrapper
    return my_decorator


@help_decorator.print_task_no("Type decorator")
@typed(style=str)
def add_two_symbols(a, b):
    print(a + b)


add_two_symbols("a", "b")
add_two_symbols("3", 5)
add_two_symbols(5, 5)


@help_decorator.print_task_no("Type decorator")
@typed(style=int)
def add_three_symbols(a, b, c):
    print(a + b + c)


add_three_symbols(5, 6, 7)
add_three_symbols("3", 5, 0)
add_three_symbols(0.1, 0.2, 0.4)
