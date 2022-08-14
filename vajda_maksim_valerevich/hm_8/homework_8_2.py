# My own task decorator

def print_task(task_no):
    def decorator_task(func_task):
        def wrapper_task(*args):
            print(f'{"̅" * 20} {task_no} TASK {"̅" * 20}')
            func_task(*args)
            print(f'{"̅" * 50}')

        return wrapper_task

    return decorator_task


# Расчет времени работы функции
# Напишите декоратор, который считает сколько времени работала декорируемая функция.
# Для получения текущего времени можно использовать функцию time.time().
# Для того чтобы искусственно замедлить работу функции можно использовать time.sleep()


import time


def timeit(func):
    def wrapper():
        start = time.time()
        sleep = 1
        time.sleep(sleep)
        func()
        end = time.time()

        print(f'Function worked for <{end - start - sleep}> seconds')

    return wrapper


@print_task('SECOND')
@timeit
def my_func():
    array_start = [1, 5, 2, 9, 2, 9, 1]
    # Homework 4 Task *1
    for i in range(len(array_start)):
        amount = array_start.count(array_start[i])
        if amount == 1:
            return array_start[i]


my_func()
