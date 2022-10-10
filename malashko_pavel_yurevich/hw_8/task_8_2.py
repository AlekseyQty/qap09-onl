import time


def timeit(func):
    def wrapper():
        start_time = time.time()
        func()
        print(f"\nFunction worked for {time.time() - start_time} seconds")
    return wrapper


@timeit
def some_function():
    number = 9000
    factorial = 1
    if number > 0:
        while number:
            factorial = factorial * number
            number -= 1
        print(factorial)
    else:
        print("Error, please, input positive number.")


some_function()
