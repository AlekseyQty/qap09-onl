# Напишите декоратор, который считает сколько времени работала декорируемая функция. Для получения текущего времени
# можно использовать функцию time.time(). Для того чтобы искусственно замедлить работу функции можно использовать
# time.sleep()

import time


def timeit(func):
    def wrapper(time_delay):
        start_1 = time.time()
        func(0)
        end_1 = time.time()

        print(f" Time work: {round(end_1 - start_1, 4)}")

        start_2 = time.time()
        func(time_delay)
        end_2 = time.time()

        print(f" Time work after sleep: {round(end_2 - start_2, 4)}")

    return wrapper

@timeit
def my_func(time_delay):
    number = 10000
    factorial = 1
    for i in range(1, number + 1):
        if i > 1:
            factorial *= i
        else:
            factorial = 1
    time.sleep(time_delay)


delay = ""
while delay != "quit":
    delay = input("Please enter your time sleep: ")

    if delay == "quit":
        print("Goodbye")
    else:
        delay = int(delay)

        my_func(delay)
