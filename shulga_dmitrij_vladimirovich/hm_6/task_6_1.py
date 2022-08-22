# Ваша задача написать программу, принимающее число - номер кредитной карты(число может быть четным или не четным).
# И проверяющей может ли такая карта существовать. Предусмотреть защиту от ввода букв, пустой строки и т.д.

def luna(number_card):
    even_numbers = []
    odd_numbers = []
    for number in range(len(number_card)):
        if number % 2 == 0:
            odd_numbers.append(int(number_card[number]))
        else:
            even_numbers.append(int(number_card[number]))
    list_multiplied_two = []
    for odd_number in odd_numbers:
        number_multiplied_two = odd_number * 2
        if number_multiplied_two >= 10:
            number_more_ten = number_multiplied_two - 9
            list_multiplied_two.append(number_more_ten)
        else:
            list_multiplied_two.append(number_multiplied_two)

    summa = even_numbers + list_multiplied_two
    total = 0
    for sum in summa:
        total += sum
    if total % 10 == 0:
        return ("This is a valid card")
    else:
        return ("This is not a valid card")

number_card = ""
while number_card != "quit":
    number_card = input("Please enter your number card: ")
    def check(number_card):
        for check_number in number_card:
            if check_number.isalpha():
                result_when_letter = 'You entered letters, please enter numbers'
                return result_when_letter
            if check_number == " ":
                result_when_space = 'You entered a space, please enter numbers'
                return result_when_space
            else:
                result_number = ''
                return result_number

    print(check(number_card))

    if check(number_card) == '':
        print(luna(number_card))
    else:
        check(number_card)
