def validate(string):
    """Функция для проверки валидности карты по алгоритму Луна"""
    if len(string) == 16 and string.isdigit():  # Проверка на то, что строка содержит 16 символов и является числом
        string = str(string)
        odds = []  # Список для нечетных цифр номера
        even = []  # Список для четных цифр номера

        # Проходим по всему номеру карты и заносим нечетные цифры номера умноженные на 2 в массив
        for i in range(0, len(string), 2):
            odds.append(int(string[i])*2)
        # Если какое-то число в списке является двузначным, то пишем сумму его цифр (14-> 1+4 -> 5)
        for i in range(len(odds)):
            sum_num = 0
            while odds[i] != 0:
                last_digit = odds[i] % 10
                sum_num += last_digit
                odds[i] //= 10
            odds[i] = sum_num

        # Записывае четные цифры номера во второй список
        for i in range(1, len(string), 2):
            even.append(int(string[i]))

        # Карта ялвяется валидной при условии, что сумма элементов из двух списков делится нацело на 10
        if (sum(odds) + sum(even)) % 10 == 0:
            print(True)
        else:
            print(False)
    else:
        print(False)


validate(input())


