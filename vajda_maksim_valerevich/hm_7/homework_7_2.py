print(f'{"̅" * 26}{"̅" * 26}')
print(f'{" " * 20} SECOND TASK {" " * 20}')
print(f'{" " * 20}  GENERATOR  {" " * 20}')
print(f'{"̅" * 26}{"̅" * 26}')

"""
Генераторы:
1.	Напишите генератор который принимает список 
numbers = [34.6, -203.4, 44.9, 68.3, -12.2, 44.6, 12.7] 
и возвращает новый список только с положительными числами
"""


def generator_positive(numbers):
    new_arr = []
    for element in range(len(numbers)):
        if numbers[element] > 0:
            new_arr.append(numbers[element])
    yield new_arr


numbers = [34.6, -203.4, 44.9, 68.3, -12.2, 44.6, 12.7]
for i in generator_positive(numbers):
    print(f'Generator 1: {i}')


"""
2.	Необходимо составить список чисел которые указывают на длину слов в строке: 
sentence = " the quick brown fox jumps over the lazy dog", но только если слово не "the".
"""


def len_generator(sentence):
    sentence_list = sentence.split()
    new_list = []
    for word in sentence_list:
        if word == 'the':
            continue
        else:
            new_list.append(len(word))
    return f'Generator 2: {new_list}'


print(len_generator(sentence=" the quick brown fox jumps over the lazy dog"))
