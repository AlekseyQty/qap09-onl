print("--------task1***_start--------")
#  *1) Вам передан массив чисел. Известно, что каждое число в этом массиве имеет пару, кроме одного:
#  [1, 5, 2, 9, 2, 9, 1] => 5. Напишите программу, которая будет выводить уникальное число.

while True:

    try:
        my_list = input("Enter any space-separated integer numbers in any quantity (for example:5 16 0 -5): ").split()
        numbers_list = [int(element) for element in my_list]
        print(numbers_list)
    except ValueError:
        print("Oops! No all elements of this array are integer numbers. Try again")
        my_list = input("Enter any space-separated integer numbers in any quantity (for example:5 16 0 -5): ").split()
    else:
        counter = 0
        for element in my_list:
            if my_list.count(element) == 1:
                print(f"The unique number is {element}.")
                counter += 1
        if counter == 0:
            print("The unique number does not exist in this sequence.")
        break

print("--------task1***_end----------")
print("--------task2***_start--------")

# *2) Дан текст, который содержит различные английские буквы и знаки препинания. Вам необходимо найти самую
# частую букву в тексте. Результатом должна быть буква в нижнем регистре. При поиске самой частой буквы, регистр
# не имеет значения, так что при подсчете считайте, что "A" == "a". Убедитесь, что вы не считайте знаки препинания,
# цифры и пробелы, а только буквы. Если в тексте две и больше буквы с одинаковой частотой, тогда результатом будет
# буква, которая идет первой в алфавите. Для примера, "one" содержит "o", "n", "e" по одному разу,
# так что мы выбираем "e".
# "a-z" == "a"  "Hello World!" == "l"  "How do you do?" == "o"  "One" == "e"  "Oops!" == "o" "AAaooo!!!!" == "a"
# "a" * 9000 + "b" * 1000 == "a"
my_text = input("Enter any english text: ").lower()
english_alphabet = "abcdefghijklmnopqrstuvwxyz"
my_dictionary = {}
for char in english_alphabet:
    if char in my_text:
        counter = my_text.count(char)
        my_dictionary[char] = counter
if not my_dictionary:
    print('No english letters')
else:
    print(f"The maximum number of letter '{max(my_dictionary, key=my_dictionary.get)}' is "
          f"{my_dictionary[(max(my_dictionary, key=my_dictionary.get))]}")

print("--------task2***_end----------")
