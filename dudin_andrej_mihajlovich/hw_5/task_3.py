input_number = int(input("Введите четырехзначное число из уникальных цифр "))
reference_number = 1234

while len(set(list(str(input_number)))) != 4:
    print(f"Введенное число {input_number} не состоит уникальных чисел. Попробуйте еще раз ")
    input_number = int(input("Введите четырехзначное число из уникальных цифр "))

reference_number = list(str(reference_number))
input_number = list(str(input_number))

while reference_number != input_number:
    i, byki, korovy = 0, 0, 0
    while i < len(reference_number):
        if input_number[i] == reference_number[i]:
            byki += 1
        elif input_number[i] in reference_number:
            korovy += 1
        else:
            pass
        i += 1
    print(f"Коровы {korovy}, Быки {byki}")

    input_number = list(str(input("Попробуйте ввести новое число ")))
    while len(set(input_number)) != 4:
        print(f"Введенное число не состоит из уникальных чисел. Попробуйте еще раз ")
        input_number = list(str(input("Введите четырехзначное число из уникальных цифр ")))
else:
    print("Вы выиграли!")