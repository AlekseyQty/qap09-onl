# Exercise_1. Переменной var_int присвойте значение 10, var_float - значение 8.4, var_str - "No".

var_int = 10
var_float = 8.4
var_str = "No"
print("var_int:", type(var_int), var_int)
print("var_float:", type(var_float), var_float)
print("var_str:", type(var_str), var_str)


# Exercise_2. Измените значение, хранимое в переменной var_int, увеличив его в 3.5 раза,
# результат свяжите с переменной big_int.

big_int = var_int * 3.5
print("big_int:", type(big_int), big_int)


# Exercise_3. Измените значение, хранимое в переменной var_float, уменьшив его на единицу,
# результат свяжите с той же переменной.

var_float = var_float - 1
print("var_float:", type(var_float), var_float)


# Exercise_4. Разделите var_int на var_float, а затем big_int на var_float. Результат данных выражений
# не привязывайте ни к каким переменным.

print("var_int / var_float:", var_int / var_float)
print("big_int / var_float:", big_int / var_float)


# Exercise_5. Измените значение переменной var_str на "NoNoYesYesYes". При формировании нового значения
# используйте операции конкатенации (+) и повторения строки (*).

var_str_1 = "Yes"
var_str = var_str * 2 + var_str_1 * 3
print("var_str:", type (var_str), var_str)


# Exercise_6. Выведите значения всех переменных.

print("result_var_int:", type(var_int), var_int)
print("result_big_int:", type(big_int), big_int)
print("result_var_float:", type(var_float), var_float)
print("result_var_str:", type(var_str), var_str)


# Exercise_7. Свяжите переменную с любой строкой, состоящей не менее чем из 8 символов. Извлеките из
# строки первый символ, затем последний, третий с начала и третий с конца. Измерьте длину вашей строки.

my_str = "exponentiation"
print("my_str:", len(my_str))
print("start_first_sign:", my_str[0])
print("end_first_sign:", my_str[-1])
print("start_third_sign:", my_str[2])
print("end_third_sign:", my_str[-3])


# Exercise_8. Присвойте произвольную строку длиной 10-15 символов переменной и извлеките из нее
# следующие срезы: первые восемь символов, четыре символа из центра строки, символы с индексами
# кратными трем, переверните строку.

s = "baseinterpreter"
print("start_eight_signs:", s[:8])
print("four_signs_from_centre:", s[6:-5])
print("multiple_of_three:", s[::3])
print("change_order:", s[::-1])


# Exercise_9. Есть строка: “my name is name”. Напечатайте ее, но вместо 2ого “name” вставьте ваше имя.

my_name = "Maria"
print("My name is {name}".format(name=my_name))


# Exercise_10. Есть строка: test_tring = "Hello world!", необходимо: напечатать на каком месте находится
# буква w, кол-во букв l, проверить начинается ли строка с подстроки: “Hello”, проверить заканчивается ли
# строка подстрокой: “qwe”.

test_string = "Hello world!"
print("find_w:", test_string.find("w"))
print("count_l:", test_string.count("l"))
print("starts_with_Hello:", test_string.startswith("Hello"))
print("ends_with_qwe:", test_string.endswith("qwe"))