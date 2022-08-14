# My own task decorator

def print_task(task_no):
    def decorator_task(func_task):
        def wrapper_task(*args):
            print(f'{"̅" * 20} {task_no} TASK {"̅" * 20}')
            func_task(*args)
            print(f'{"̅" * 50}')

        return wrapper_task

    return decorator_task


# Лексикографическое возрастание*
# На вход подаётся некоторое количество (не больше сотни) разделённых пробелом целых чисел
# (каждое не меньше 0 и не больше 19).
# Выведите их через пробел в порядке лексикографического возрастания названий этих чисел в английском языке.
# Т.е., скажем числа 1, 2, 3 должны быть выведены в порядке 1, 3, 2,
# поскольку слово two в словаре встречается позже слова three, а слово three -- позже слова one
# (иначе говоря, поскольку выражение 'one' < 'three' < 'two' является истинным)
#


@print_task('THIRD')
def func():
    number_names = \
        {
            0: 'zero', 1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six', 7: 'seven', 8: 'eight',
            9: 'nine',
            10: 'ten', 11: 'eleven', 12: 'twelve',
            13: 'thirteen', 14: 'fourteen', 15: 'fifteen', 16: 'sixteen', 17: 'seventeen', 18: 'eighteen',
            19: 'nineteen'
        }
    input_num = list(map(str, input('Enter numbers by space: ').split()))

    sorted_dict = {}
    sorted_keys = sorted(number_names, key=number_names.get)

    for v in sorted_keys:
        sorted_dict[v] = number_names[v]

    new_one = {}
    for k, v in sorted_dict.items():
        if str(k) in input_num:
            new_one[k] = v
    print("Sorted result:")
    for key in new_one.keys():
        print(key, end=' ')
    print()


func()
