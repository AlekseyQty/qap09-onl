# На вход подаётся некоторое количество (не больше сотни) разделённых пробелом целых чисел (каждое не меньше 0 и не
# больше 19).Выведите их через пробел в порядке лексикографического возрастания названий этих чисел в английском
# языке. Т.е., скажем числа 1, 2, 3 должны быть выведены в порядке 1, 3, 2, поскольку слово two в словаре встречается
# позже слова three, а слово three -- позже слова one (иначе говоря, поскольку выражение 'one' < 'three' < 'two'
# является истинным)

import random

amount = ""
while amount != "quit":
    amount = input("Please enter amount <=100: ")

    if amount == "quit":
        print("Goodbye")
    else:
        amount = int(amount)
        number_names = {
        0: 'zero', 1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six', 7: 'seven', 8: 'eight', 9: 'nine',
        10: 'ten', 11: 'eleven', 12: 'twelve', 13: 'thirteen', 14: 'fourteen', 15: 'fifteen', 16: 'sixteen',
        17: 'seventeen',  18: 'eighteen', 19: 'nineteen'}


        def decorater(func):

            def wrapper():
                unique_list = []
                for i in func():
                    if i in number_names.keys():
                        for k in number_names:
                            if i == k:
                                unique_list.append(number_names[k])
                sorted_list = sorted(unique_list)
                final_result = []
                for j in sorted_list:
                    if j in number_names.values():
                        for key, value in number_names.items():
                            if j == value:
                                final_result.append(key)

                print(f" Sorted list: {final_result}")
            return wrapper


        @decorater
        def my_func():
            beg = 0
            end = 19
            list_numbers = []
            for i in range(amount):
                list_numbers.append(random.randint(beg, end))
            print(f" Start list: {list_numbers}")
            return list_numbers

        my_func()



