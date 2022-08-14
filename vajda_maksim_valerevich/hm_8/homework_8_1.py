# My own task decorator

def print_task(task_no):
    def decorator_task(func_task):
        def wrapper_task(*args):
            print(f'{"̅" * 20} {task_no} TASK {"̅" * 20}')
            func_task(*args)
            print(f'{"̅" * 50}')

        return wrapper_task

    return decorator_task


# Декоратор типов
# Напишите декоратор, который проверял бы тип параметров функции, конвертировал их если надо и складывал:


def typed(type):
    def decorator(func):
        def wrapper(arg1, arg2):
            if type == 'str':
                arg1 = str(arg1)
                arg2 = str(arg2)
                func(arg1, arg2)
            elif type == 'int':
                arg1 = int(arg1)
                arg2 = int(arg2)
                func(arg1, arg2)
            else:
                print('I dont know')

        return wrapper

    return decorator


@print_task('FIRST')
@typed(type='str')
def add_two_symbols(a, b):
    print(a + b)


add_two_symbols("3", 5)  # -> "35"
add_two_symbols(5, 5)  # -> "55"
add_two_symbols('a', 'b')  # -> 'ab’

""" 
Не смог сделать универсальный декоратор, для разного кол-ва аргументов.
Нужен совет.
"""


# @print_task('ONE')
# @typed(type='int')
# def add_three_symbols(a, b, c):
#     print(a + b + c)
#
#
# add_three_symbols(5, 6, 7)  # -> 18
# add_three_symbols("3", 5, 0)  # -> 8
# add_three_symbols(0.1, 0.2, 0.4)  # -> 0.7000000000000001
