import time
from functools import wraps

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