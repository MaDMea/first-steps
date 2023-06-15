# -*- encoding: utf-8 -*-
# При выполнении дз использовать Git (делать коммиты, работать в develop ветке,
# для каждой задачи отдельная feature/<название_ветки> ветка из develop ветки,
# после завершения работы над задачей - делать merge feature ветки в dev ветку,
# после выполнения всех заданий сделать merge develop в master)
# #
# #
# # 1. Пользователь вводит с клавиатуры три числа. В зависимости от выбора пользователя программа
# # выводит на экран максимум из трёх, минимум из трёх или среднеарифметическое трёх чисел.
# #
# num1 = int(input("Введите первое число: "))
# num2 = int(input("Введите второе число: "))
# num3 = int(input("Введите третье число: "))
#
# big = num1
# if big < num2:
#     big = num2
# if big < num3:
#     big = num3
#
# print("Большее из введеных: ", big)
#
# small = num1
# if small > num2:
#     small = num2
# if small > num3:
#     small = num3
#
# print("Меньшее из введеных: ", small)
#
# sum = num1 + num2 +num3
# midar = sum/3
#
# print("Среднее арифметическое чисел: ", midar)
# #
# # 2. Пользователь вводит с клавиатуры количество метров. В зависимости от выбора пользователя программа
# # переводит метры в мили, дюймы или ярды.
###############
#
#
# 1. Пользователь вводит с клавиатуры номер дня недели (1-7). Необходимо вывести на экран названия дня недели.
# Например, если 1, то на экране надпись понедельник, 2 — вторник и т.д.

# day = int (input("Введите номер дня: "))
# if day == 1:
#     print("Понедельник")
# elif day == 2:
#     print("Вторник")
# elif day == 3:
#     print("Среда")
# elif day == 4:
#     print("Четверг")
# elif day == 5:
#     print("Пятница")
# elif day == 6:
#     print("Суббота")
# elif day == 7:
#     print("Воскресенье")
# else:
#     print("Введите корректное число 1-7!")

# 2. Пользователь вводит два числа. Определить, равны ли эти числа, и, если нет,
# вывести их на экран в порядке возрастания
#
# a = int(input("Введите первое число: "))
# b = int(input("Введите второе число: "))
#
# if a == b:
#     print("Числа равны!")
# elif a != b:
#     print(*sorted([a, b]))
#     print("Числа не равны!")

#
#
# 3. Пользователь вводит два числа и матем действие: + - * или /
#
# В зависимости от введенного матем действия вывести результат
#
# print("Что бы выйти из программы введите 0 в метематическом действе")
# while True:
#
#     s = input("Введите математическое действие: ")
#     if s == "0":
#         break
#     if s not in ('+', '-', '*', '/'):
#         continue
#     a = int(input("Введите первое число: "))
#     b = int(input("Введите второе число: "))
#
#     if s == '+':
#         print("Сложение", a + b)
#     elif s == '-':
#         print("Вычитание", a - b)
#     elif s == '*':
#         print("Умножение", a * b)
#     elif s == '/':
#         if b != 0:
#             print("Деление", a / b)
#         else:
#             print("Деление на ноль!")

# Home work 5.06
# 1. Пользователь вводит с клавиатуры строку. Посчитайте количество букв, цифр в строке.
# Выведите оба количества на экран. (использовать цикл)

# line = input("Введите числа и буквы: ")
# digit_counter = 0
# alpha = 0
# for i in line:
#     if i.isdigit():
#         digit_counter += 1
#     if i.isalpha():
#         alpha += 1
# else:
#     print("Цифры: ", digit_counter, "Буквы: ", alpha)
#
#
# 2. Пользователь вводит с клавиатуры строку и символ для поиска.
# Посчитайте сколько раз в строке встречается искомый символ.
# Полученное число выведите на экран.
#
# line = input("Введите строку: ")
#
# search_char = input("Введите символ для поиска: ")
#
# count = 0
#
# for char in line:
#    if char == search_char:
#        count += 1
#
# print(f"Символ '{search_char}' встречается {count} раз(а) в строке.")
#
# 3. Пользователь вводит с клавиатуры строку, слово для поиска, слово для замены.
# Произведите в строке замену одного слова на другое. Полученную строку
# отобразите на экране.
#
# string = input("Введите строку: ")
# word_to_find = input("Введите слово для поиска: ")
# word_to_replace = input("Введите слово для замены: ")
# new_string = ""
# word = ""
# found = False
# for char in string:
#    if char == " ":
#        if word == word_to_find:
#            new_string += word_to_replace + " "
#            found = True
#        else:
#            new_string += word + " "
#        word = ""
#    else:
#        word += char
# if word == word_to_find:
#    new_string += word_to_replace
#    found = True
# else:
#    new_string += word
# if found:
#    print("Измененная строка:", new_string)
# else:
#    print("Слово не найдено в строке.")
#
#
# 4. Дана строка. (сделать срезы)
# - Сначала выведите третий символ этой строки.
#
# - Во второй строке выведите предпоследний символ этой строки.
#
# - В третьей строке выведите первые пять символов этой строки.
#
# - В четвертой строке выведите всю строку, кроме последних двух символов.
#
# - В пятой строке выведите все символы с четными индексами (считая, что индексация начинается с 0,
# поэтому символы выводятся начиная с первого).
#
# - В шестой строке выведите все символы с нечетными индексами, то есть начиная со второго символа строки.
#
# - В седьмой строке выведите все символы в обратном порядке.
#
# - В восьмой строке выведите все символы строки через один в обратном порядке, начиная с последнего.
#
# - В девятой строке выведите длину данной строки.
#
# sentence = input("Введите строку: ")
# print(sentence[3])
# print(sentence[-2])
# print(sentence[:5])
# print(sentence[:-2])
# print(sentence[::2])
# print(sentence[1::2])
# print(sentence[::-1])
# print(sentence[::-2])
# print(len(sentence))

# Задание 1
#
# В списке целых, заполненном случайными числами вычислить:
#
# ■ Сумму отрицательных чисел;
#
# ■ Сумму четных чисел;
#
# ■ Сумму нечетных чисел;
#
# ■ Произведение элементов с индексами кратными 3;
#
# ■ Произведение элементов между минимальным и максимальным элементом;
#
# ■ Сумму элементов, находящихся между первым и последним положительными элементами.
#


import random

# numbers = [random.randint(-10, 10) for i in range(10)]
# sum_neg = 0
# sum_odd = 0
# sum_even = 0
# product_3 = 1
# min_num = 0
# max_num = 0
# product_min_max = 1
# print(numbers)
# for i in numbers:
#     if i < 0:
#         sum_neg += i
# print("Summa otricat", sum_neg)
#
# for i in numbers:
#     if i % 2 == 0:
#         sum_odd += i
#
# print("Summa chetnyh", sum_odd)
#
# for i in numbers:
#     if i % 2 != 0:
#         sum_even += i
#
# print("Summa nechetnyh", sum_even)
#
# for i in range(len(numbers)):
#     if i % 3 == 0:
#         product_3 *= numbers[i]
#
# print("Proizved index 3 ", product_3)
#
#
#
# min_value = min(numbers)
# max_value = max(numbers)
# min_value_index = numbers.index(min_value)
# max_value_index = numbers.index(max_value)
#
# if max_value_index - min_value_index != 0:
#     if min_value_index > max_value_index:
#         min_value_index, max_value_index = max_value_index, min_value_index
#
#     mult = 1
#
#     for i in range(min_value_index + 1, max_value_index):
#         mult *= numbers[i]
#
#     print(mult)
#
# first_index = 0
# last_index = 0
# for i in range(len(numbers)):
#     if numbers[i] > 0:
#         first_index = i
#         break
#
# for i in range(len(numbers) - 1, -1, -1):
#     if numbers[i] > 0:
#         last_index = i
#         break
#
# print(first_index)
# print(last_index)
#
#
# if first_index != last_index:
#     my_sum = 0
#     for i in range(first_index + 1, last_index):
#         my_sum += numbers[i]
#
#     print(my_sum)
#
#
#  Задание 2
#
# Есть список целых, заполненный случайными числами. На основании данных этого массива нужно:
#
# ■ Создать список целых, содержащий только четные числа из первого списка;
#
# ■ Создать список целых, содержащий только нечетные числа из первого списка;
#
# ■ Создать список целых, содержащий только отрицательные числа из первого списка;
#
# ■ Создать список целых, содержащий только положительные числа из первого списка.


# OK
# numbers = [random.randint(-10, 10) for i in range (10)]
# print(numbers)
#
# odd_list = [(i) for i in numbers if i % 2 == 0]
# print("List even", odd_list)
#
# even_list = [(i) for i in numbers if i % 2 != 0]
# print("List odd", even_list)
#
# negative_list = [(i) for i in numbers if i < 0]
# print("List negative", negative_list)
#
# positive_list = [(i) for i in numbers if i >= 0]
# print("List positive", positive_list)
#
#
#
#

