#Напишите программу, которая перебирает последовательность от 1 до 100 Для чисел
#кратных 3 она должна написать: "Fuzz" вместо печати числа, а для чисел кратных 5
#печатать "Buzz". Для чисел которые кратны 3 и 5 надо печатать "FuzzBuzz". Иначе
#печатать число.
#Вывод должен быть следующим:
#1
#2
#fuzz
#4
#buzz
#fuzz
#7
#8


for fuzzbuzz in range(100):
    if fuzzbuzz % 3 == 0 and fuzzbuzz % 5 == 0:
        print("FuzzBuzz")
        continue
    elif fuzzbuzz % 3 == 0:
        print("Fuzz")
        continue
    elif fuzzbuzz % 5 == 0:
        print("Buzz")
        continue
    print(fuzzbuzz)