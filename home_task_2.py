# -*- encoding: utf-8 -*-
#При выполнении дз использовать Git (делать коммиты, работать в develop ветке,
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
# #
try:
    day = int (input("Enter number of a day: "))
if day == 1:
    print("Понедельник")
elif day == 2:
    print("Вторник")
elif day == 3:
    print("Среда")
elif day == 4:
    print("Четверг")
elif day == 5:
    print("Пятница")
elif day == 6:
    print("Суббота")
elif day == 7:
    print("Воскресенье")
elif:
    except Exception("Please enter a valid date 1-7!")

#     if 1 < len(name) <= 20:
#         print(f"Hello, {name}")
#     else:
#         raise Exception("Please enter a valid name!")  # raise -> сгенерировать исключение (бросить исключение)
#
#     num = 0
#     if num == 0:
#         raise ZeroDivisionError("Не дели на ноль!")
# except ZeroDivisionError as err:
#     print("ashdfvbsdfvblsdvfbldsfv")
# except Exception as e:
#     print(f"Error: {e}")

# 2. Пользователь вводит два числа. Определить, равны ли эти числа, и, если нет,
# вывести их на экран в порядке возрастания
#
#
#
# 3. Пользователь вводит два числа и матем действие: + - * или /
#
# В зависимости от введенного матем действия вывести результат


# try:
#     name = input("Enter you name: ")
#
#     if name == "vasya":
#         raise Exception("Вася, пока!")
#
#     if 1 < len(name) <= 20:
#         print(f"Hello, {name}")
#     else:
#         raise Exception("Please enter a valid name!")  # raise -> сгенерировать исключение (бросить исключение)
#
#     num = 0
#     if num == 0:
#         raise ZeroDivisionError("Не дели на ноль!")
# except ZeroDivisionError as err:
#     print("ashdfvbsdfvblsdvfbldsfv")
# except Exception as e:
#     print(f"Error: {e}")