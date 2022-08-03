# 1.Факториал
from random import randrange

a = randrange(2, 20)

factorial = 1

for i in range(2, a+1):
    factorial *= i
    print(f'Factorial: {a}', factorial)

#2.BuzzFuzz

for i in range(1,101):
    if i % 3 == 0:
        print('Fuzz')
    elif i % 5 == 0:
        print('Buzz')
    elif i % 3 == 0 and i % 5 == 0:
        print('FuzzBuzz')
    else:
        i % 3 != 0 and i % 5 != 0
        print(i)

#3.Быки и коровы

print('Игрок № 1, ввдите число из 4х разных цифр')

while True:
    player_1 = input('=> :')

    if len(player_1) != 4:
        print('Игрок № 1, число должно состаять из 4х цифр!')
        player_1

    else:
        if len(str(player_1)) == 4:

                for i in range(len(player_1) - 1):
                    for j in range(i + 1, len(player_1)):
                        if player_1[j] == player_1[i]:
                            print('Игрок № 1, число должно содержать 4 разных цифры!')
                            player_1 = input('=> :')
                        else:
                            if player_1[j] != player_1[i]:
                                continue
    break

print('Игрок № 2, ввдите число из 4х разных цифр')

while True:
    player_2 = input('=> :')

    if len(player_2) != 4:
        print('Игрок № 2, число должно состаять из 4х цифр!')
        player_2

    else:
        if len(str(player_2)) == 4:

                for i in range(len(player_2) - 1):
                    for j in range(i + 1, len(player_2)):
                        if player_2[j] == player_2[i]:
                            print('Игрок № 2, число должно содержать 4 разных цифры!')
                            player_2 = input('=> :')
                        else:
                            if player_2[j] != player_2[i]:
                                continue
    break

player_1 = list(player_1)
player_2 = list(player_2)

bull = 0
cow = 0

while True:

    for i in range(4):
        if player_2[i] == player_1[i]:
            bull += 1
            player_1[i] = '-'
            player_2[i] = '+'

    if bull == 4:
        print('Игрок № 2, Вы победили!!!')
        break

    for i in range(4):
        n = player_2[i]
        for j in range(4):
            if n == player_1[j]:
                cow += 1
                player_1[j] = '+'
    break




