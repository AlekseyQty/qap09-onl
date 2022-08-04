"""
В классическом варианте игра рассчитана на двух игроков. Каждый из игроков задумывает
и записывает тайное 4-значное число с неповторяющимися цифрами. Игрок, который
начинает игру по жребию, делает первую попытку отгадать число. Попытка — это 4-
значное число с неповторяющимися цифрами, сообщаемое противнику. Противник
сообщает в ответ, сколько цифр угадано без совпадения с их позициями в тайном числе
(то есть количество коров) и сколько угадано вплоть до позиции в тайном числе (то есть
количество быков).
При игре против компьютера игрок вводит комбинации одну за другой, пока не отгадает
всю последовательность.
Ваша задача реализовать программу, против которой можно сыграть в "Быки и коровы"
Загадано число 3219
 2310
Две коровы, один бык
3219
Вы выиграли!
"""
import random


def get_all_answers():
    """ список ответов"""
    answer = []
    for i in range(10000):
        tmp = str(i).zfill(4)
        number_list = ['x' for number in tmp if tmp.count(number) == 1]
        if len(number_list) == 4:
            answer.append(list(map(int, tmp)))
    # print(answer)
    return answer


def get_one_answer(answer):
    """ выбор одного ответа из списка"""
    number = random.choice(answer)
    return number


def input_number():
    """ запрашивает у пользователя неповторяющие цифры"""
    while True:
        nums = input("Введите четыре неповторяющихся числа: ")
        if len(nums) != 4 or not nums.isdigit():
            continue
        nums = list(map(int, nums))
        if len(set(nums)) == 4:
            break
    return nums


def check(nums, true_numbers):
    """сравнивает два числа и сообщает колличество быков и коров"""
    bulls, cows = 0, 0
    for i, num in enumerate(nums):
        if num in true_numbers:
            if nums[i] == true_numbers[i]:
                bulls += 1
            else:
                cows += 1
    return bulls, cows


def del_bad_answer(ans, enemy_try, bull, cow):
    """удаляет неподходящие варианты из списка возможных"""
    for num in ans[:]:
        temp_bull, temp_cow = check(num, enemy_try)
        if temp_bull != bull or temp_cow != cow:
            ans.remove(num)
    return ans


# сама игра
print("Игра быки и коровы")
answers = get_all_answers()
computer = get_one_answer(answers)
player = input_number()

while True:
    print('=' * 15, "Ход игрока", "=" * 15)
    print("Угадайте число компьютера")
    number = input_number()
    bulls, cows = check(number, computer)
    print("Быки: ", bulls, "Коровы: ", cows)
    if bulls == 4:
        print("Победил игрок")
        print("Компьютер загадал число ", computer)
        break
# угадывает компьютер
    print('=' * 15, "Ход компьютера", "=" * 15)
    enemy_try = get_one_answer(answers)
    print("Компьютер считает, что вы загаадил число ", enemy_try)
    bulls, cows = check(enemy_try, player)
    print("Быки: ", bulls, "Коовы: ", cows)
    if bulls == 4:
        print("Победил компьютер")
        print("Компьютер загадал число ", computer)
        break
    else:
        answers = del_bad_answer(answers, enemy_try, bulls, cows)
