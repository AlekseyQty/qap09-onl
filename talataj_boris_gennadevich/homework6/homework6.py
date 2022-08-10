#Ваша задача написать программу, принимающее число - номер кредитной карты
# (числоможет быть четным или не четным). И проверяющей может ли такая карта существовать.
# Предусмотреть защиту от ввода букв, пустой строки и т.д.

def digitSum(myString):

    lenght = len(myString)
    oddSum = 0
    evenSum = 0

    if (lenght == 0):
        return 0
    else:
        if (lenght % 2 == 0):
            last = int(myString[:-1])
            evenSum += last

            return evenSum + digitSum(myString[:-1])

        else:
            last = int(myString[-1])
            last = 2 * last
            part_sum = last // 10 + last % 10
            oddSum += part_sum

            return oddSum + digitSum(myString[:-1])

def luhns():
    mySrting = input('Введите 16-ти значный номер карты: ')
    total = digitSum(mySrting)

    if (total % 10 == 0):
        print('Valid card')
    else:
        print('Invalid card')


luhns()

#На вход подается строка, например, "cccbba" результат работы программы - строка “c3b2a"
#Примеры для проверки работоспособности:
#"cccbba" == "c3b2a"
#"abeehhhhhccced" == "abe2h5c3ed"
#"aaabbceedd" == "a3b2ce2d2"
#"abcde" == "abcde"
#"aaabbdefffff" == "a3b2def5"

def countingletters(string):
    result =''
    i = 0
    while i<len(string):
        symbol = string[i]
        symbolCount = string.count(symbol)
        result = result + symbol + str(symbolCount)
        string = string.replace(symbol, '')
        i = i+1

    print(result)

countingletters("aaabbrruuii")


#Реализуйте программу, которая спрашивала у пользователя, какую операцию он хочет
#произвести над числами, а затем запрашивает два числа и выводит результат
#Проверка деления на 0 Реализовать программу нужно с использованием функций.

s = input("Выберите операцию (+, -, *, /): ")
if s not in ('+', '-', '*', '/'):
    quit()
a = float(input('a = '))
b = float(input('b = '))

if s == '+':
    print(a + b)
elif s == '-':
    print(a - b)
elif s == '*':
    print(a * b)
elif s == '/':
    if b != 0:
     print(a / b)
    else:
        print('Деление на ноль')

