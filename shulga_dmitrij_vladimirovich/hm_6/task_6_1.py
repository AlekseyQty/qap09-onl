# Ваша задача написать программу, принимающее число - номер кредитной карты(число может быть четным или не четным).
# И проверяющей может ли такая карта существовать. Предусмотреть защиту от ввода букв, пустой строки и т.д.

def luna(number_card):
    unique = []
    unique_1 = []
    for i in range(len(number_card)):
        if i % 2 == 0:
            unique.append(number_card[i])
        else:
            unique_1.append(int(number_card[i]))
    #print(unique)
    #print(unique_1)
    unique_2 = []
    for j in unique:
        j = int(j)
        f = j * 2
        if f >= 10:
            f = f - 9
            unique_2.append(f)
        else:
            unique_2.append(f)
    #print(unique_2)
    summa = unique_1 + unique_2
    #print(summa)
    total = 0
    for sum in summa:
        total += sum
    #print(total)
    if total % 10 == 0:
        return ("This is a valid card")
    else:
        return ("This is not a valid card")

number_card = ""
while number_card != "quit":
    number_card = input("Please enter your number card: ")
    def check(number_card):
        for s in number_card:
            if s.isalpha():
                result_1 = 'You entered letters, please enter numbers'
                return result_1
            if s == " ":
                result_2 = 'You entered a space, please enter numbers'
                return result_2
            else:
                result_3 = ''
                return result_3

    print(check(number_card))

    if check(number_card) == '':
        print(luna(number_card))
    else:
        check(number_card)