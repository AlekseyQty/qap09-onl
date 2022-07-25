# 1. Заменить символ “#” на символ “/” в строке 'www.my_site.com#about'

add_str = 'www.my_site.com#about'

print('task_1/1: ' + add_str.replace('#', '/'))
print(f'task_1/2: { add_str.replace("#", "/") }')

# 2. Напишите программу, которая добавляет ‘ing’ к словам

word = input('Word please:')
word_1 = 'play'
word_2 = 'drink'
word_3 = 'jump'

add_ing = 'ing'

print('task_2/1: ' + word_1 + add_ing, word_2 + add_ing, word_3 + add_ing)
print(f'task_2/2: {word}ing')


# 3. В строке “Ivanou Ivan” поменяйте местами слова => "Ivan Ivanou"

name = 'Ivanou Ivan'

first_name = name[name.find(' ')+1:]
last_name = name[:name.find(' ')+1]

print('task_3/1: ' + first_name + ' ' + last_name)
print('task_3/2: ' + ' '.join(name.split()[::-1]))


# 4. Напишите программу которая удаляет пробел в начале, в конце строки

origin_str = '_The_world_under_spam_attack_'

#  "Space" mark as "_" for visibility

first_space = origin_str.find('_')
last_space = origin_str.rfind('_')

print('task_4/1: ' + origin_str[first_space+1:last_space])
print('task_4/2: ' + origin_str.strip('_'))

origin_str2 = input('Str please:')
print('task_4/3: ' + origin_str2.strip())
