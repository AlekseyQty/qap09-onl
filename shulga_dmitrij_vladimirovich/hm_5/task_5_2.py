# 2.BuzzFuzz
# Напишите программу, которая перебирает последовательность от 1 до 100.
# Для чисел кратных 3 она должна написать: "Fuzz" вместо печати числа, а для чисел кратных 5  печатать "Buzz".
# Для чисел которые кратны 3 и 5 надо печатать "FuzzBuzz". Иначе печатать число.

current_number = 0
while current_number < 100:
    current_number += 1
    if current_number %5 == 0 and current_number % 3 == 0:
        print("BuzzFuzz")
        continue
    if current_number %3 == 0:
        print("Fuzz")
        continue
    if current_number %5 == 0:
        print("Buzz")
        continue
    print(current_number)
