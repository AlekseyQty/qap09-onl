# 3.Быки и коровы
import random
digits = random.sample("1234567890", 4)  # 4 элемента без повторов из заданной коллекции
number = int("".join(digits))  # соединяем в одно и конвертируем в число
if number < 1000:  # если первая цифра была 0...
    number = number * 10  # ...то добавляем его в конец

while True:
    user_number = int(input("Введите ваше число: "))
    counter = 0  # Переменная counter создана для подсчета быков(т.е. для количества цифр, угаданных на своей позиции.

    if number//1000 == user_number//1000:  # Проверка первой цифры
        counter += 1
    if number//100 - number//1000*10 == user_number//100 - user_number//1000*10:  # Проверка второй цифры
        counter += 1
    if number//10 - number//100*10 == user_number//10 - user_number//100*10:  # Проверка третьей цифры
        counter += 1
    if number % 10 == user_number % 10:  # Проверка четвертой цифры
        counter += 1

    # Записываем загаданное число и вводимое число в 2 списка
    system_number_list = [number//1000, number//100 - number//1000*10, number//10 - number//100*10, number % 10]
    user_number_list = [user_number//1000, user_number//100 - user_number//1000*10,
                        user_number//10 - user_number//100*10, user_number % 10]

    if user_number == number:
        print("Вы выйграли! :)")
        break
    else:
        # Для подсчёта "коров" используем операцию пересечения для двух верхних множеств (A&B) и подсчитываем количество
        # угаданных цифр
        print(f"{len(set(system_number_list) & set(user_number_list)) - counter} Коровы и {counter} бык")
        print("Не верно, попробуйте еще раз.")

