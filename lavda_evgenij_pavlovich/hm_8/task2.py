"""Напишите декоратор, который считает сколько времени работала декорируемая
функция. Для получения текущего времени можно использовать функцию time.time().
Для того чтобы искусственно замедлить работу функции можно использовать
time.sleep()"""
import time


def timeit(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        return_value = func(*args, **kwargs)
        end = time.time()
        print(f"Время выполнения функции: {end - start} секунд ")
        return return_value
    return wrapper


@timeit
def my_funck():
    a = []
    for i in range(100):
        a.append(i)
    return sum(a)


print(my_funck())
