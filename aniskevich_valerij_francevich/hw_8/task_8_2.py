import time


# Расчет времени работы функции
# Напишите декоратор, который считает сколько времени работала декорируемая
# функция. Для получения текущего времени можно использовать функцию time.time().
# Для того чтобы искусственно замедлить работу функции можно использовать
# time.sleep()
# Пример работы:
# @timeit
# def my_func():
# some code
# > Function worked for <time> seconds

def timeit(func):
    def wrapper():
        start_time = time.time()
        func()
        finish_time = time.time()
        lasting = finish_time - start_time
        print(f"Function worked for {lasting} seconds")

    return wrapper


@timeit
def my_function():
    my_list = []
    for i in range(12345678):
        my_list.append(i)
    return my_list


my_function()
