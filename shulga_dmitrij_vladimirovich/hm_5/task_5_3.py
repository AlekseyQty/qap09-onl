# 3.Быки и коровы
# В классическом варианте игра рассчитана на двух игроков.
# Каждый из игроков задумывает и записывает тайное 4-значное число с неповторяющимися цифрами.
# Игрок, который начинает игру по жребию, делает первую попытку отгадать число.
# Попытка — это 4-значное число с неповторяющимися цифрами, сообщаемое противнику.
# Противник сообщает в ответ, сколько цифр угадано без совпадения с их позициями в тайном числе
# (то есть количество коров) и сколько угадано вплоть до позиции в тайном числе (то есть количество быков).
# При игре против компьютера игрок вводит комбинации одну за другой, пока не отгадает всю последовательность.
# Ваша задача реализовать программу, против которой можно сыграть в "Быки и коровы"

my_number = ""
while my_number != "quit":
    number = input("Please enter hidden four-digit number: ")
    my_number = input("Please enter your four-digit number: ")
    #number = "1324"
    if my_number == number:
        print("Вы выиграли!")
        break
    else:
        count = 0
        for j in number:
            if j in my_number:
                count += 1
            if count == 1:
                count_1 = str(count)
                count_1 = "Одна корова"
                continue
            if count == 2:
                count_1 = str(count)
                count_1 = "Две коровы"
                continue
            if count == 3:
                count_1 = str(count)
                count_1 = "Три коровы"
                continue
            if count == 4:
                count_1 = str(count)
                count_1 = "Четыри коровы"
                continue
        count_2 = 0
        for i in range(1, len(number)):
            if number[i] == my_number[i]:
                count_2 += 1
            if count_2 == 1:
                count_3 = str(count_2)
                count_3 = "Один бык"
                continue
            if count_2 == 2:
                count_3 = str(count_2)
                count_3 = "Два быка"
                continue
            if count_2 == 2:
                count_3 = str(count_2)
                count_3 = "Три быка"
            if count_2 == 2:
                count_3 = str(count_2)
                count_3 = "Четыри быка"

        print(f"{count_1}, {count_3} ")



