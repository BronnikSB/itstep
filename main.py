# print('"Any one who\n\t stops'   #print - функция вывода.
#       '\n\t\tlearning is old,'
#       '\n\t\t whether at twenty or eighty". '
#       '\n\t\t\t\t\t\t\t Henry Ford')
#
# #---------------------------------------------------
# name = "Sergey"
# last_name = "Bronnikov"
# age = 24
# print("Я", name, last_name,"Мне", age,"года")
# print(name + last_name)
#
# #---------------------------------------------------
# x = 3
# y = 5
#
# print("Произведение:",(x*y)/y,"\n""Сумма:",x+y,"\n""Разность:",x-5,"\n""Деление:", x/y)
# #---------------------------------------------------
# name = input("Введите вашее имя:")
# last_name = input("Введите вашу фамилию:")
# full_name = name + " " + last_name
# print(full_name)
# #---------------------------------------------------
# num = float(input("Введите число:"))
# num2 = float(input("Введите процент:"))/100
# per = num*num2
# print(per)
# #---------------------------------------------------
# width = float(input("Введите ширину:"))
# lengths = float(input("Введите длину:"))
# S = width*lengths
# print(S)
# #---------------------------------------------------
# a = float(input("Введите градус(цельсия):"))* 9/5 + 32
#
# print(a, "Фарингейта")
#
#
#
#
#
# num1 = float(input("Введите первое число:"))
# num2 = float(input("Введите второе число:"))
# num3 = float(input("Введите третье число:"))
#
# num_sum = num1 + num2 + num3
# print("Сумма введенных чисел равна:", num_sum)
# #----------------------------------------------
# num1 = float(input("Введите первое число:"))
# num2 = float(input("Введите второе число:"))
# num3 = float(input("Введите третье число:"))
#
# num_mult = num1 * num2 * num3
# print("Произведение введенных чисел равно:", num_mult)
# #------------------------------------------------
#
# num1 = float(input("Введите Вашу месячную зарплату:"))
# num2 = float(input("Введите сумму месячного платежа по кредиту в банке:"))
# num3 = float(input("Введите задолженность за коммунальные услуги:"))
#
# num_sum = num1 - (num2 + num3)
# print("Остаток зарплаты:", num_sum)
# #----------------------------------------------
# print("Вычисление площади ромба через диагональ")
# d1 = float(input("Введите первую диагональ ромба:"))
# d2 = float(input("Введите вторую площадь ромба:"))
# s_romb = (d1*d2)/2
# print("Площадь ромба равна:", s_romb)
# ##------------------------------------------------
# print('"Life is what happens'
#       '\n\t when'   #print - функция вывода.
#       '\n\t\tyou’re busy making other plans'
#       '\n\t\t\t\t\t\t\t John Lennon.')
# #-------------------------------------------------
# a = int(input("Введите число:"))
# b = a%100
# d = (a-b)/100
# c = b%10
# e = (b-c)/10
#
# print("Первое число: ",d, "\nВторое число: ",e, "\nТретье число: ",c )
# #-----------------------------------------------------------
# print("AAAAAAAA","BBBBBBB","CCCCCCC", sep = "%", end = "!")
# #-----------------------------------------------------------
# a = "BNB"
# print(len(a))
# #len() возвращает длину символа.
# #-----------------------------------------------------------
# num = int(input("Введите число:"))
# a = num%10
# b = a+num
# c = b
# print(a,c)
# #-----------------------------------------------------------
# a = input('Висит груша, нельзя скушать:')
# if a == 'Лампочка':
#     print('Верно!');
# elif a == 'Лампа':
#     print('Верно!')
# elif a != 'Лампочка':
#     print('Неверно!')
# #-----------------------------------------------------------
# a = int(input("Введите число:"))
# if a%2 == 0 :
#     print("Число",a, "четное")
# else:
#     print("Число",a, "нечетное")
# #-----------------------------------------------------------
# a = int(input("Введите число кратное 7:"))
# if a%7 > 0:
#     print("Это число не кратно 7")
# elif a == 0:
#     print("Это число равно 0")
# else:
#     print("Это число кратно 7")
# #-----------------------------------------------------------
# a = int(input("Введите первое число:"))
# b = int(input("Введите второе число:"))
# if a > b:
#     print(a)
# elif a < b:
#     print("Наибольшее число", b)
# else:
#     print("Числа равны")
# #-----------------------------------------------------------
# a = int(input("Введите первое число:"))
# b = int(input("Введите второе число:"))
# if a > b:
#     print(b)
# elif a < b:
#     print("Наименьшее число",a)
# else:
#     print("Числа равны")
# #-----------------------------------------------------------
# a = input("Что нужно сделать?(Сумма - 1, Произведение - 2, Разность - 3, Среднее арифметическое - 4):")
# b = float(input('Введите первое число:'))
# f = float(input('Введите второе число:'))
# if a == "1":
#     d = b + f
#     print(d)
# elif a == "2":
#     d = b * f
#     print(d)
# elif a == "4":
#     d = (b + f)/2
#     print(d)
# elif a == "3":
#     d = b - f
#     print(d)
# else:
#     print('NULL')
# #-----------------------------------------------------------
# action = input("Что нужно сделать(+\*)?:")
# num_one = float(input("Введите первое число:"))
# num_two = float(input("Введите первое число:"))
# num_three = float(input("Введите первое число:"))
# if action == "+":
#     finish = num_one + num_two + num_three
#     print("Сумма введенных чисел равна:",finish)
# elif action == "*":
#     finish = num_one * num_two * num_three
#     print("Произведение введенных чисел равно:",finish)
# else:
#     print("Введите верное действие.")
# #-----------------------------------------------------------
# action = input("Выберите действие:"
#                "\n 1. Максимальное значение"
#                "\n 2. Минимальное значение"
#                "\n 3. Среднее арифметическое"
#                "\n Ввод:")
# num_one = float(input("Введите первое число:"))
# num_two = float(input("Введите второе число:"))
# num_three = float(input("Введите третье число:"))
# if action == "1" and num_one < num_two < num_three:
#     print("Наиболшее значение:",num_three)
# elif action == "1" and num_one > num_two > num_three:
#     print("Наиболшее значение:", num_one)
# elif action == "1" and num_two > num_one > num_three:
#     print("Наиболшее значение:", num_two)
# elif action == "1" and num_one == num_two == num_three:
#     print("Числа равны.")
# elif action == "2" and num_one < num_two < num_three:
#         print("Наименьшее значение:", num_one)
# elif action == "2" and num_one > num_two > num_three:
#         print("Наименьшее значение:", num_three)
# elif action == "2" and num_two < num_one < num_three:
#         print("Наименьшее значение:", num_two)
# elif action == "2" and num_one == num_two == num_three:
#         print("Числа равны.")
# elif action == "3":
#     mid = (num_one + num_two + num_three)/3
#     print("Среднее арифметическое равно:",mid)
# #-----------------------------------------------------------
# action = input("Во что вы хотите конвертировать 'Метры?':\n"
#                "1. Перевести в 'Милли'\n"
#                "2. Перевести в 'Дюймы'\n"
#                "3. Перевести в 'ярды'\n"
#                "Ввод:")
# m = float(input("Введите число:"))
# if action == "1":
#     mi = m/1609
#     print(mi, "m")
# elif action == "2":
#     inch = m * 39.37
#     print(inch, "inch")
# elif action == "3":
#     yd = m * 1.094
#     print(yd, "yd")
# else:
#     print("NULL")
# #-------------------------------------------------------------
# time_action = input("Во что хотите сконвертировать секунды?\n"
#                   "1. Часы\n"
#                   "2. Минуты\n"
#                   "3. Секунды\n"
#                   "Ввод:")
# time_us = float(input("Сколько секунд прошло с начала дня?:"))
# if time_action == "1":
#     time_conv = time_us/3600
#     time_rem = 24-time_conv
#     print("До полуночи осталось", time_rem,"ч.")
# elif time_action == "2":
#     time_conv = time_us/60
#     time_rem = 1440-time_conv
#     print("До полуночи осталось", time_rem,"мин.")
# elif time_action == "3":
#     time_rem = 86400 - time_us
#     print("До полуночи осталось", time_rem,"сек.")
# else:
#     print("NULL")
# #-------------------------------------------------------------
# d = float(input("Введите диаметр окружности:"))
# action = input("Что нужно сделать?\n"
#                "1. Посчитать периметр.\n"
#                "2. Посчитать площадь.\n"
#                "Ввод: ")
# pi = 3.14
# if action == "1":
#     p = d/2 * pi * 2
#     print("Периметр круга равен:",p)
# elif action == "2":
#     s = pi * d * d/4
#     print("Площадь круга равна:",s)
# #-------------------------------------------------------------
# price = float(input("Сколько стоит приставка?:"))
# num = int(input("Количество приставок:"))
# sale = float(input("Размер скидки:"))/100
# action = input("Выберите что нужно сделать?\n"
#                "1. Посчитать общую стоимость товаров\n"
#                "2. Посчитать стоимость одной приставки с учетом скидки.")
# if action == "1":
#     gen = num * price
#     print("Общая стоимость товаров:", gen)
# elif action == "2":
#     gen = price/num * sale
#     print("Cтоимость одной приставки с учетом скидки:", gen)
# #-------------------------------------------------------------
# time = float(input("Введите количество часов:"))
# if time < 6 and time > 0:
#     print("Good Night")
# elif time >= 6 and time < 13:
#     print("Good Morning")
# elif time >= 13 and time < 13:
#     print("Good Day")
# elif time >= 17 and time < 0:
#     print("Good Evening")
# #-------------------------------------------------------------
# gb = float(input("Введите количество гигабайт:"))
# bt = float(input("Введите скорость интернета в байтах:"))
# time = input("Выберите нужную единицу для расчета времени:\n"
#              "1. Секунды\n"
#              "2. Минуты\n"
#              "3. Часы\n"
#              "Ввод:")
# if time == "1":
#     gb_bt = gb * 10 ** 9
#     sec = gb_bt/bt
#     print("Ваш файл будет скачиваться",sec,"сек.")
# elif time == "2":
#     gb_bt = gb * 10 ** 9
#     sec = gb_bt / bt
#     min = sec/60
#     print("Ваш файл будет скачиваться",min,"мин.")
# elif time == "3":
#     gb_bt = gb * 10 ** 9
#     sec = gb_bt / bt
#     hour = sec / 3600
#     print("Ваш файл будет скачиваться",hour,"ч.")
# #-------------------------------------------------------
#
# #-------------------------------------------------------
# num_use = input("Введите число:")
# a = int(num_use[0])
# b = int(num_use[1])
# c = int(num_use[2])
# d = int(num_use[3])
# e = int(num_use[4])
# f = int(num_use[5])
# if len(num_use) == 6:
#     a = int(num_use[5])
#     b = int(num_use[4])
#     e = int(num_use[1])
#     f = int(num_use[0])
#     print(a, b, c, d, e, f, sep= "")
# else:
#     print("Ошибка!")
# #---------------------------------------------
# num_use = input('Введите шестизначное число:')
# a = int(num_use[0])
# b = int(num_use[1])
# c = int(num_use[2])
# d = int(num_use[3])
# e = int(num_use[4])
# f = int(num_use[5])
# if a + b + c == d + e + f:
#     print('Число является счастливым!')
# else:
#     print('Число не является счастливым.')
# #---------------------------------------------
#
# largest_num = 1000
#
# num = int(input("введите число или число 500, чтобы остановить программу"))
#
# while num != 500:
#     if num > largest_num:
#         largest_num = num
#     num = int(input("введите число или число 500, чтобы остановить программу"))
#
# print(largest_num)
# #---------------------------------------------
# num_use = float(input('Введите число:'))
# num_even = 0
# num_odd = 0
# while num_use != 0:
#     if num_use % 2 == 0:
#         num_even += 1
#         num_use = float(input('Введите число:'))
#     elif num_use % 2 != 0:
#         num_odd +=1
#         num_use = float(input('Введите число:'))
#
# print("Четных чисел:", num_even,"\n"
#       "Нечетных чисел:", num_odd)
# #-----------------------------------------------
# num_use = float(input('Введите число:'))
# i = 1
# while i ** 2 <= num_use:
#     print(i ** 2)
#     i += 1
# #-----------------------------------------------
# num_user = int(input("Введите первое число:"))
# num_user_two = int(input("Введите второе число:"))
#
# while num_user != num_user_two:
#     print(num_user)
#     num_user += 1
# num_user = int(input("Введите первое число:"))
# num_user_two = int(input("Введите второе число:"))
# while num_user != num_user_two:
#     print(num_user_two)
#     num_user_two -= 1
# num_user = int(input("Введите первое число:"))
# num_user_two = int(input("Введите второе число:"))
# while num_user != num_user_two:
#     if num_user % 7 == 0:
#         print(num_user)
#     num_user = num_user + 1
# num_user = int(input("Введите первое число:"))
# num_user_two = int(input("Введите второе число:"))
# count = 0
# while num_user != num_user_two:
#     if num_user % 5 == 0:
#         count += 1
#         print(count)
#     num_user += 1
# # -----------------------------------------------
# # Пользователь вводит с клавиатуры два числа. Нужно посчитать сумму чисел в указанном диапазоне,
# # а также среднеарифметическое.
# num_user = int(input("Введите первое число:"))
# num_user_two = int(input("Введите второе число:"))
# sum_range = 0
# mid_num = num_user_two - num_user + 1
# while num_user <= num_user_two:
#     sum_range += num_user
#     num_user += 1
# print("Сумма диапазаона:", sum_range, "\n Среднее арифметическое: " ,sum_range, mid_num)
# #-----------------------------------------------
# a=int(input("введите первое число: "))
# b=int(input("введите второе число: "))
# summ = 0
# sum_chis=b-a+1
# while a<=b:
#     summ+=a
#     a+=1
# print("сумма",summ)
# print("ср.ариф", summ/sum_chis)
# #--------------------------------------
# num_user = int(input("Введите первое число:"))
# factorial = 1
# while num_user > 1:
#     factorial = factorial * num_user
#     num_user -= 1
# print(factorial)
# #-----------------------------------------
# a = 1
# for exp in range(16):
#     print('2 в степени', exp, 'равно', a)
#     a = a * 2
# #-----------------------------------------
# print('Инструкция break')
# for i in range(1, 6):
#     if i == 3:
#         break#останавливает цикл.
#     print('Внутри цикла', i)
# print('Вне цикла', i)
# #-----------------------------------------
# print('Инструкция break')
# for i in range(1, 6):
#     if i == 3:
#         continue#исключает цикл.
#     print('Внутри цикла', i)
# print('Вне цикла', i)
# #-----------------------------------------
# text = 'Всем привет, погода в Москве испортилась'
# for letter in text:
#     if letter == 'п':
#         break
#     print(letter)
# #-----------------------------------------
# print('Нахожлдение фактороиала')
# num_user = int(input('Введите число:'))
# factorial = 1
# for i in range(1, num_user + 1):
#     factorial = i * factorial
# print("Факториал", num_user, "равен",factorial)
# #-----------------------------------------
# n = int(input('Add num'))
# for i in range(0, n + 1):#Количество строк
#     for j in range(0, n - i):#Форма и смещение
#         print(end='')
#     for d in range(0, i):#Количество символов в строке.
#         print('*', end=' ')
#     print()
# #-----------------------------------------
# HomeWork(Figure)
# # # A
# print('Рисунок "А"')
# num_user = int(input('Enter the number:'))
# for string in range(num_user, 0 , -1):
#     for i in range(num_user - string):
#         print('  ', end='')
#     for a in range(string):
#         print('*', end=' ')
#     print()
# # Б
# print('Рисунок "Б"')
# num_user = int(input('Enter the number:'))
# for string in range(num_user + 1):
#     for i in range(num_user - string):
#         print(end='')
#     for a in range(string):
#         print('*', end=' ')
#     print()
# # В
# print('Рисунок "В"')
# num_user = int(input('Enter the number:'))
# for string in range(num_user, 0 , -1):
#     for i in range(num_user - string):
#         print(' ', end='')
#     for a in range(string):
#         print('*', end=' ')
#     print()
# # Г
# print('Рисунок "Г"')
# num_user = int(input('Enter the number:'))
# for b2 in range(0, num_user + 1):
#     for i2 in range(0, num_user - b2):
#         print(end=' ')
#     for a2 in range(b2):
#         print('*', end=' ')
#     print()
# #Д
# print('Рисунок "Д"')
# num_user = int(input('Enter the number:'))
# for string in range(num_user, 0 , -1):
#     for i in range(num_user - string):
#         print('', end=' ')
#     for a in range(string):
#         print('*', end=' ')
#     print()
# for b2 in range(0, num_user + 1):
#     for i2 in range(0, num_user - b2):
#         print(end=' ')
#     for a2 in range(b2):
#         print('*', end=' ')
#     print()
#
# #Е
# print('Рисунок "Ж"')
# num_user = int(input('Enter the number:'))
# print('\n')
# for b in range(num_user, 0 , -1):
#     for i in range(num_user - b):
#         print('*', end=' ')
#     for a in range(b):
#         print(' ', end=' ')
#     print()
# for b2 in range(0, num_user + 1):
#     for i2 in range(0, num_user - b2):
#         print('*', end=' ')
#     for a2 in range(b2):
#         print('', end=' ')
#     print()
# #Ж
# print('Рисунок "З"')
# num_user = int(input('Enter the number:'))
# for string in range(0, num_user):
#     for i in range(0, num_user - string):
#         print('', end='  ')
#     for a in range(string):
#         print('*', end=' ')
#     print()
# for string in range(num_user, 0 , -1):
#     for i in range(num_user - string):
#         print('  ', end='')
#     for a in range(string):
#         print('*', end=' ')
#     print()
# #З
# print('Рисунок "И"')
# num_user = int(input('Enter the number:'))
# for string in range(0, num_user + 1):
#     for i in range(0, num_user - string):
#         print('*', end=' ')
#     for a in range(string):
#         print(' ', end=' ')
#     print()
# #К
# print('Рисунок "К"')
# num_user = int(input('Enter the number:'))
# for string in range(0, num_user + 1):
#     for i in range(0, num_user - string):
#         print('', end='  ')
#     for a in range(string):
#         print('*', end=' ')
#     print()
#
#
#
#
#
# # -----------------------------------------
# # Пользователь вводит с клавиатуры два числа (нача- ло и конец диапазона).
# # Требуется проанализировать все числа в этом диапазоне. Нужно вывести на экран:
#
# # 1. Все числа диапазона;
# # 2. Все числа диапазона в убывающем порядке;
# # 3. Все числа, кратные 7;
# # 4. Количество чисел, кратных 5.
# # ---------------------------------------------
# # Пользователь вводит с клавиатуры два числа (начало и конец диапазона).
# # Требуется проанализировать все числа в этом диапазоне. Вывод на экран должен проходить по правилам, указанным ниже.
# # Если число кратно 3 (делится на 3 без остатка) нужно вывести слово Fizz. Если число кратно 5 нужно вывести слово Buzz.
# # Если число кратно 3 и 5 нужно вывести Fizz Buzz.
# # Если число не кратно не 3 и 5 нужно вывести само число.
#
# num_use = int(input('Введите первое число:'))
# num_use_two = int(input('Введите второе число:'))
#
# print('\nЧисла в порядке возрастания:')
# for up in range(num_use, num_use_two + 1):
#         print(up, end=' ')
#
# print('\nЧисла в порядке убывания:')
# for down in range(num_use_two, num_use - 1, -1):
#         print(down, end=' ')
#
# print('\nЧисла кратные 7:')
# for i_7 in range(num_use,num_use_two):
#     if i_7 % 7 == 0:
#         print(i_7)
#
# print('Количество числел кратных 5:')
# number = 0
# for i_5 in range(num_use,num_use_two):
#     if i_5 % 5 == 0:
#         number += 1
# print(number)
#
# print('\nС условием: если кратно трём:')
# a = ''
# for fizz in range(num_use, num_use_two + 1):
#     if fizz % 3 == 0 and fizz % 5 == 0:
#         a = 'FizzBuzz'
#         print(a, end=' ')
#     elif fizz % 3 == 0 or fizz % 5 != 0:
#         a = 'Fizz'
#         print(a, end=' ')
#     elif fizz % 5 == 0 or fizz % 3 != 0:
#         a = 'Buzz'
#         print(a, end=' ')
# #------------------------------------------
# # Пользователь вводит с клавиатуры длину линии.
# # Нужно отобразить на экране горизонтальную линию из *, указанной длины.
# # Например, если было введено 7, тогда вывод на экран будет такой: *******.
# num_use = int(input('Введите длину линии:'))
# lenght = num_use * '* '
# print(lenght)
#
# num_use = int(input('Введите длину линии:'))
# for i in range(num_use):
#     print('*', end=' ')
# #Пользователь вводит с клавиатуры длину линии и символ для заполнения линии.
# #Нужно отобразить на экране горизонтальную линию из введенного символа, указанной длины.
# #Например, если было введено 5 и &, тогда вывод на экран будет такой: &&&&&.
# num_use = int(input('\nВведите длину линии:'))
# num_use2 = (input('Введите тип линии:'))
# for i in range(num_use):
#     print(num_use2, end=' ')
# #---------------------------------------------List
# lst = ['hello', 1, 2, 145]
# print(lst)
#
# numbers = [0, 45, 33, 89, 201,[1, 2, 3]]
# print('Первоначальное значение списка:', numbers)
# numbers[0] = 222
# print('Обновленное значение:', numbers)
# numbers[1] = numbers[3]
# print('Обновленное значение списка:', numbers)
# print(len(numbers))
#
# del numbers[0]#--delete function
# print('Удаление первого элемента в списке:', numbers)
# #---------------------------------------------method
# lst = [0, 43, 99, 12]
# lst.append(99)
# print(lst)
# lst.insert(1, 444)
# print(lst)
# #---------------------------------------------
# lst = []
# # for i in range(5):
# #     lst.append(i + 1)
# # print(lst)
# for i in range(5):
#     lst.insert(4, i + 1)
# print(lst)
# #--------------------------------------------
# lst = [1, 5, 6, 122, 5443]
# summ = 0
# for i in range(len(lst)):
#     summ += lst[i]
# print(summ)
#
#
# lst = [1, 5, 6, 122, 5443]
# summ = 0
# for i in lst[-1:-3]:
#     summ += i
# print(summ)
# #---------------------------------------------
# lst = [1, 5, 6, 122, 5443]
# lst[0], lst[3] = lst[3], lst[0]
# print(lst)
# lst = []
# for i in range(5):
#     lst.insert(0,input('Add:'))
# print(lst)
#
# lst = input('Add:')
# lst_new = lst.split()
# lst_rev = []
# for i in lst_new:
#     lst_rev.insert(0, i)
# print(lst_rev)
#
# myList = []
# for i in range(5):
#     myList.append(i+1)
# print(myList)
# #------------------------------------------------
# #isdigit() возвращает True, если все символы в строке являются цифрами. Если нет, возвращается False
# enter_use = input('Введите число:')
# print(enter_use.upper())
# print(enter_use.lower())
#
# num = [
#     int(i)
#     for i in enter_use
#     if i.isdigit()
# ]# проверка наличия цифр в строке
# print(len(num))
#
# sum = 0
# for s in num:
#     sum += s
# print(sum)
# #-------------------------------------------------
# a = 'HelloWorld!'
# print(a.find('W'))
# print(a.count('l'))
# #-------------------------------------------------
# import random#library
#
# list = []
# for i in range(10):
#     list.append(random.randint(0, 1))#Добавляет рандомные числа в список list
# print(list)
# #------------------------------------------------
# random_num_list = []
# for i in range(15):
#     random_num_list.append(random.randint(-30, 30))
# text = 'Рандомный список:'
# print(text)
# print(*random_num_list, sep=', ')
#
# sum_negative = 0
# sum_even = 0
# sum_even_not = 0
# multiple_three = 1
# sum_range = 0
# max_num = 0
# min_num = 0
# for i in random_num_list:
#     if i < 0:
#         sum_negative += i#сумма отрицательных чисел
# for i in random_num_list:
#     if i % 2 == 0:
#         sum_even += i#сумма четных чисел
# for i in random_num_list:
#     if i % 2 != 0:
#         sum_even_not += i#сумма нечетных чисел
# for i in random_num_list:
#     if i % 3 == 0:
#         multiple_three = multiple_three * i#произведение чисел кратных 3
# for i in random_num_list:
#     if i > 0:
#         sum_range += i#сумма положительных чисел
# for i in random_num_list:
#     if i > max_num:
#         max_num = i
#     elif i < min_num:
#         min_num = i
# multiple_max_min = max_num * min_num
# print('Сумма отрицательных чисел:', sum_negative,
#       '\nCумма четных чисел:', sum_even,
#       '\nСумма нечетных чисел:', sum_even_not,
#       '\nПроизведение чисел кратных трем:', multiple_three,
#       '\nСумма положительных чисел', sum_range,
#       '\nПроизведение максимального и минимального числа чисел:', multiple_max_min)
# #----------------------------------
# lst = ['asd','nhd', 'num']
# lst_str = ', '.join(lst)
# print(lst_str)
# lst = [1, 4, 6, 12, 99, 'table','armchair']
# lst = [str(i) for i in lst]
# lst_str = ', '.join(lst)
# print(lst_str)
# #----------------------------------calculator
# import sys, os
# operator = input('Что нужно сделать?\n''+\n''-\n''*\n''/\n''Ввод:')
# num_1 = 0
# num_2 = 0
# while True:
#     try:
#         num_1 = float(input('Введите первое число:'))
#     except ValueError:
#         print('Необходимо ввести число!')
#     try:
#         num_2 = float(input('Введите второе число:'))
#     except ValueError:
#         print('Необходимо ввести число!')
#     else:
#         break
#
# result = 0
#
# if operator == '+':
#     result = num_1 + num_2
# elif operator == '-':
#     result = num_1 - num_2
# elif operator == '*':
#     result = num_1 * num_2
# elif operator == '/':
#     result = num_1 / num_2
# else:
#     print('Вы ввели неверный оператор!')
# print(result)
# #-----------------------------------Проверка наличия элементов в списке
# print('Если в списке есть элемент, то...')
# lst = [1, 3, 54, 3, 21, 44]
# lst[0] = lst[3] + 21
# if 3 in lst:# ищем число 3 в списке lst
#     print(lst[0])
# else:
#     print(lst[5])
# def line_function():
#     line = []
#     for i in range(20):
#         line.append(i)
#         print('--', end='')
# line_function()
# #-------------------------------------------
# print('\nЕсли в списке нет элемента, то...')
# lst_two = ['Hi', 'How', 'are', 'you', '?']
# if 'i am fine' not in lst_two:# проверяем действительно в списке нет элемента 'i am fine'
#     print('Poorly')
# else:
#     print('And I')
# print('Количество элементов в строке = ', len(lst_two))
# line_function()
# #-------------------------------------------
# print('\nДобавляем в список новый элемент в указанное место')
# lst_two.insert(1, 'Bran!')#Добавляем новый эелемент в указанное место
# print(*lst_two)
# print('Номер элемента "Bran!" в списке =', lst_two.index('Bran!'))
# line_function()
# #-------------------------------------------
# print('\nПереносим каждый элемент списка на новую строку, добавляя запятую')
# for new_str in lst_two:
#     new_str += ','
#     print(new_str)
# #-----------------------------------Самостоятельная работа 30.09.21
#Каждое предложение с заглавной буквы
input_use = list(input('Введите текст:'))

input_use[0] = input_use[0].upper()
separator = ['.', '!', '?']
len_input_use = len(input_use)
for i in range(len_input_use):
    if input_use[i] in separator:
        input_use[i+1] = input_use[i + 1].upper()
print(*input_use, end='', sep='')
#----------Количество цифр в строке
num = [
    int(i)
    for i in input_use
    if i.isdigit()
]
print('\nКоличество цифр в строке:', len(num))
#----------------Количество знаков препинания
punctuation = ['.', ',', '?', '!', '-', ':', ';', '(', ')', '"', "'"]
punctuation_number = 0
for i in range(len_input_use):
    if input_use[i] in punctuation:
        punctuation_number += 1
print('Количество знаков препинания:', punctuation_number)
#-------------------Ищем количество символов в строке
num = list(input('Введите символ:'))
num_sought = input('Введите искомое число:')
number_sought = 0
for i in num:
    if i == num_sought:
        number_sought += 1
print('Количество символов', num_sought, 'равно', number_sought)