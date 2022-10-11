import func

while True:
   fun_num = input('////////////// \n1. Сложение \n2. Вычитание \n3. Умножение \n4. Деление \nВведите номер пункта меню: ')

   if fun_num == '':
       fun_num

   elif int(fun_num) > 4:
       fun_num

   arg1 = input('Введите первое число: ')
   arg2 = input('Введите второе число: ')

   if int(fun_num) == 1:
       sum_num = func.Sum_num().math_func(arg1, arg2)
       print(f'////////////// \nОтвет: {sum_num}')

   elif int(fun_num) == 2:
       calc_num = func.Calc_num().math_func(arg1, arg2)
       print(f'////////////// \nОтвет: {calc_num}')

   elif int(fun_num) == 3:
       multip_num = func.Multip_num().math_func(arg1, arg2)
       print(f'////////////// \nОтвет: {multip_num}')

   elif int(fun_num) == 4:
       if float(arg2) == 0:
           print(f'////////////// \nДеление на 0 невозможно!')

       elif float(arg1) == float(arg2):
           print('////////////// \nОтвет: 0')

       else:
           if float(arg2) != 0:
               divi_num = func.Divi_num().math_func(arg1, arg2)
               print(f'////////////// \nОтвет: {divi_num}')