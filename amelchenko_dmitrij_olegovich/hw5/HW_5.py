# 1.Факториал
from random import randrange

a = randrange(2, 20)

factorial = 1

for i in range(2, a+1):
    factorial *= i
    print(f'Factorial: {a}', factorial)

#2.BuzzFuzz

for i in range(1,101):
    if i % 3 == 0 and i % 5 != 0:
        i = 'Fuzz'

    elif i % 3 != 0 and i % 5 == 0:
        i = 'Buzz'

    elif i % 3 == 0 and i % 5 == 0:
        i = 'FuzzBuzz'

    print(i)

# 3.Быки и коровы

print('Игрок № 1, ввдите число из 4х разных цифр')

while True:
    player_1 = input('=> :')
    a = True

    if len(player_1) != 4:
        print('Игрок № 1, число должно состаять из 4х цифр!')
        continue

    for i in range(len(player_1) - 1):
        for j in range(i + 1, len(player_1)):
            if player_1[j] == player_1[i]:
                print('Игрок № 1, число должно содержать 4 разных цифры!')
                a = False
                break

    if a == True:
        player_1 = list(player_1)
        break


def play_2():
    bull = 0
    cow = 0

    print('Игрок № 2, ввдите число из 4х разных цифр')

    while True:

        player_2 = input('=> :')
        a = True

        if len(player_2) != 4:
            print('Игрок № 2, число должно состаять из 4х цифр!')
            continue

        for i in range(len(player_2) - 1):
            for j in range(i + 1, len(player_2)):
                if player_2[j] == player_2[i]:
                    print('Игрок № 2, число должно содержать 4 разных цифры!')
                    a = False
                    break

        if a == True:
            player_2 = list(player_2)
            break

    while True:
        for i in range(4):
            if player_2[i] == player_1[i]:
                bull += 1
                player_1[i] = '-'
                player_2[i] = '+'
                continue

        for i in range(4):
            n = player_2[i]
            for j in range(4):
                if n == player_1[j]:
                    cow += 1
                    player_1[j] = '+'
                    continue

        if bull != 4:
            print(f'Быков: {str(bull)}, Коров: {str(cow)}')
            play_2()

        else:
            if bull == 4:
                print(f'Вы выиграли!!! \n'
                      f'Быки: {str(bull)} из 4')
                break


play_2()
