#2 Расчет времени работы функции
import time

def my_fun_time(fun):

    def fun_time():

        start = time.perf_counter()
        fun()
        stop = time.perf_counter()

        return print(f'Function worked for <{stop - start:0.6f}> seconds')

    return fun_time

@my_fun_time
def generator():

    my_list = [1, 2, 3, 4, 5, 6]
    new_my_list = []

    for i in my_list:
        if i % 2:
            new_my_list.append(i)

    return new_my_list

generator()
