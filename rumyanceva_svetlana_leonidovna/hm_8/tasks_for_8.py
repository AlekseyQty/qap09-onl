import time
# Task1. Напишите декоратор, который проверял бы тип параметров функции, конвертировал их если надо и складывал:
# @typed(type=’str’)
# def add_two_symbols(a, b):
# return a + b

# add_two_symbols("3", 5) -> "35"
# add_two_symbols(5, 5) -> "55"
# add_two_symbols('a', 'b') -> 'ab’


def typed(var_type):
    def decorator(func_to_decor):
        def wrapper(enter_list):
            if var_type == "str":  # all elements of the list have to convert to type str
                new_list = []
                for elem in enter_list:
                    if not isinstance(elem, str):
                        new_list.append(str(elem))  # convert elem to type str
                    else:
                        new_list.append(elem)
                print(func_to_decor(new_list, ""))
            elif var_type == "int":  # all elements of the list have to convert to type int
                new_list = []
                for elem in enter_list:
                    if isinstance(elem, float) or isinstance(elem, int):
                        new_list.append(elem)  # just add elem=number, which has type float or int
                    elif elem.count(".") == 1:  # if elem is type str and contain 1 dot, you can convert to float
                        new_list.append(float(elem))
                    elif elem.isalpha():
                        print("Letter can't be converted to a number")
                        return
                    else:
                        new_list.append(int(elem))  # convert elem to type int

                print(func_to_decor(new_list, 0))

        return wrapper
    return decorator


@typed(var_type="int")
def add_symbols(result_list, summary):
    for elem in result_list:
        summary += elem
    return summary


add_symbols(["0.1", "v", 1])
# add_symbols(["0.1", "v", 1])
# add_symbols([0.1, 5, 1])
# add_symbols(["a", "b", "i"])


print("------------task2--task3*------start---------")
# Task2: Расчет времени работы функции. Напишите декоратор, который считает сколько времени работала декорируемая
# функция. Для получения текущего времени можно использовать функцию time.time(). Для того чтобы искусственно
# замедлить работу функции можно использовать time.sleep()

# Task3*: Лексикографическое возрастание*. На вход подаётся некоторое количество (не больше сотни) разделённых пробелом
# целых чисел (каждое не меньше 0 и не больше 19). Выведите их через пробел в порядке лексикографического возрастания
# названий этих чисел в английском языке.
# Т.е., скажем числа 1, 2, 3 должны быть выведены в порядке 1, 3, 2, поскольку слово two в словаре встречается позже
# слова three, а слово three -- позже слова one
# (иначе говоря, поскольку выражение 'one' < 'three' < 'two' является истинным)


def timeit(func_to_decor):
    def wrapper():
        start_time = time.time()
        print(func_to_decor())
        print(f"Function worked for {time.time() - start_time} seconds")
    return wrapper


@timeit
def my_func():
    # time.sleep(0.5)
    try:
        my_list = []
        for i in range(1, 11):
            num = int(input("Enter any integer numbers from 0 to 19: "))
            if 0 <= num <= 19:
                my_list.append(num)
            else:
                print("You have entered an integer number out range from 0 to 19.")
                exit()
    except ValueError:
        print("You have entered no integer number.")
        exit()
    else:
        sorted_keys_list = sorted(number_names, key=number_names.get)
        # [8, 18, 11, 15, 5, 4, 14, 9, 19, 1, 7, 17, 6, 16, 10, 13, 3, 12, 2, 0]
        sorted_my_list = []
        for elem in sorted_keys_list:
            if elem in my_list:
                if my_list.count(elem) == 1:  # if elem from sorted_keys_list is met one time in entered my_list,
                    # add this elem to sorted my list.
                    sorted_my_list.append(elem)
                else:  # if element from sorted_keys_list is met more one time in entered my_list,
                    # add this elem the necessary number of times to the sorted_my_list
                    for _ in range(my_list.count(elem)):
                        sorted_my_list.append(elem)
        return sorted_my_list


number_names = {
    0: 'zero', 1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six', 7: 'seven', 8: 'eight', 9: 'nine',
    10: 'ten', 11: 'eleven', 12: 'twelve', 13: 'thirteen', 14: 'fourteen', 15: 'fifteen', 16: 'sixteen',
    17: 'seventeen',  18: 'eighteen', 19: 'nineteen'}

my_func()
print("------------task2--task3*------end---------")
