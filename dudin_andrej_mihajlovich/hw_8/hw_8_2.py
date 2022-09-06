'''
Напишите декоратор, который считает сколько времени работала декорируемая
функция. Для получения текущего времени можно использовать функцию time.time().
Для того чтобы искусственно замедлить работу функции можно использовать
time.sleep()
Пример работы:
@timeit
def my_func():
some code
> Function worked for <time> seconds
'''
import time

def timeit(func):
    def wrapper(*args):
        start_time = time.time()
        func(*args)
        print(f"\nFunction worked for {time.time() - start_time} seconds")
    return wrapper


@timeit
def test_func(num_1, num_2):
    time.sleep(2)
    return num_1 * num_2


test_func(100,200)