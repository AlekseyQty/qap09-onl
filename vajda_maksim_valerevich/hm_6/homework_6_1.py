print(f'{"̅"*26}{"̅"*26}')
print(f'{" "*20}FIRST TASK{" "*20}')
print(f'{" "*16}CREDIT CARD VALIDATE{" "*16}')
print(f'{"̅"*26}{"̅"*26}')
"""
1.Validate
Ваша задача написать программу, принимающее число - номер кредитной карты(число
может быть четным или не четным). И проверяющей может ли такая карта существовать.
Предусмотреть защиту от ввода букв, пустой строки и т.д.
"""

def luna_alg(user_card_num_luna):                           # Luhn algorithm
    for i in range(len(user_card_num_luna)):
        if i % 2 == 0:
            user_card_num_luna[i] = user_card_num_luna[i] * 2
            if user_card_num_luna[i] > 9:
                user_card_num_luna[i] = user_card_num_luna[i] - 9
                if sum(user_card_num_luna) % 10 == 0:
                    result = "The result: CARD is EXIST"
                else:
                    result = "The result: CARD isn't EXIST"
    return result


user_card_num = input('Enter your card number: ')          # validate(4561261212345464) #=> False
                                                           # validate(4561261212345467) #=> True
if len(user_card_num) != 0 and user_card_num.isdigit():    # credit card can only contain 15-16 digits, not empty string
    if len(user_card_num) == 16:
        user_card_num_valid = user_card_num
    elif len(user_card_num) == 15:
        user_card_num_valid = user_card_num + '7'
    else:
        print("The result: CARD isn't EXIST")
        quit()
else:
    print("The result: CARD isn't EXIST")
    quit()
user_card_num_luna = list(map(int, user_card_num_valid))

print(luna_alg(user_card_num_luna))
print(f'{"̅"*26}{"̅"*26}')

