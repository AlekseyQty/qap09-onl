import time

# 1. Напишите декоратор, который проверял бы тип параметров функции, конвертировал их если надо и складывал:


def typed(typo):
    def decorator(funk):
        def wrapper(*args):
            list_args = []
            for arg in args:
                if isinstance(arg, float):
                    list_args.append(arg)
                else:
                    arg = typo(arg)
                    list_args.append(arg)
            funk(*list_args)
        return wrapper
    return decorator


@typed(typo=str)
def some_funk_1(a, b):
    print(a + b)


some_funk_1("3", 5)
some_funk_1(5, 5)
some_funk_1("a", "b")


@typed(typo=int)
def some_funk_2(a, b, c):
    print(a + b + c)



some_funk_2(5, 6, 7)
some_funk_2("3", 5, 0)
some_funk_2(0.1, 0.2, 0.4)


# 2. Расчет времени работы функции


def decorator_timeit(funk):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        funk(*args, **kwargs)
        end_time = time.time() - start_time
        print(f"Время работы {funk}: {end_time} сек.")
    return wrapper


@decorator_timeit
def some_funk_3(num_1, num_2):
    time.sleep(2)
    return num_1 ** num_2


some_funk_3(356, 5)


# 3. Лексикографическое возрастание*

number_names = {0: 'zero', 1: 'one', 2: 'two',
                3: 'three', 4: 'four', 5: 'five',
                6: 'six', 7: 'seven', 8: 'eight',
                9: 'nine', 10: 'ten', 11: 'eleven',
                12: 'twelve', 13: 'thirteen',
                14: 'fourteen', 15: 'fifteen',
                16: 'sixteen', 17: 'seventeen',
                18: 'eighteen', 19: 'nineteen'}

numb_in = [int(i) for i in input('Введите список чисел через пробел: ').split()]
list_str = []
for i in numb_in:
    for k in number_names.keys():
        if i == k:
            list_str.append(number_names[k])

list_str.sort()

list_dict = [[k, v] for k, v in number_names.items()]
list_dict_rev = []
for i in list_dict:
    list_dict_rev.append(i[::-1])
new_number_names = {}
for i in list_dict_rev:
    new_number_names[i[0]] = i[1]

sort_list_numb = []
for i in list_str:
    for k in new_number_names.keys():
        if i == k:
            sort_list_numb.append(new_number_names[k])

sort_numb = [str(i) for i in sort_list_numb]
print("В порядке лексикографического возрастания: " + " ".join(sort_numb))
