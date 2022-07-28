#  tasks 1: Заменить символ “#” на символ “/” в строке 'www.my_site.com#about'.
print("--------task1_start--------")

my_string = input("Enter any URL/string/sentence: ")  # for example: www.my_site.com#about
print(my_string.replace("#", "/", my_string.count("#")))

print("--------task1_end----------")

# tasks 2: Напишите программу, которая добавляет ‘ing’ к словам.
print("--------task2_start--------")
# for example:
# Yesterday ... mom washed a lot of things: 5 windows, 1 car - suddenly it started to rain. It was terrible??!!!
my_list = input("Enter any sentence or text: ").split()
new_list = []
for i in range(len(my_list)):
    word = my_list[i]
    for j in range(1, len(word) + 1):
        if word[-j].isalpha():
            if word[-1].isalpha():
                new_word = word + "ing"
                new_list.append(new_word)
                break
            else:
                new_word = word[:-j + 1] + "ing" + word[-j + 1:]
                new_list.append(new_word)
                break
    else:
        new_list.append(word)
print(' '.join(new_list))

print("--------task2_end-----------")

# tasks 3: В строке “Ivanov Ivan” поменяйте местами слова => "Ivan Ivanov".
print("--------task3_start--------")

try:
    my_text = input("Enter space-separated last name and first name: ")
    position = my_text.index(' ')
    print(my_text[position + 1:].title() + " " + my_text[:position].title())
except ValueError:
    print("No space")

print("--------task3_end-----------")

# tasks 4: Напишите программу, которая удаляет пробел в начале, в конце строки.
print("--------task4_start--------")
print(input("Enter any sentence: ").strip())

print("--------task4_end-----------")
