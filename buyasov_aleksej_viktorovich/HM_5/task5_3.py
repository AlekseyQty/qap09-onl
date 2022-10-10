import random

numbers = list(range(1, 10))
pc_number = ''.join(map(str, random.sample(numbers, k=4)))
pc_number

def get_user_input():
    while True:
        value = input('> ')
        if value.isdigit() and len(set(value)) == 4:
            return value
        print('Wrong number. Try again...')


user_input = get_user_input()
while pc_number != user_input:
    cow = len(set(pc_number).intersection(set(user_input)))
    bull = sum([pc_number[i] == user_input[i] for i in range(4)])
    print(f'{cow} Cows, {bull} Bulls')
    user_input = get_user_input()
print('You won!')