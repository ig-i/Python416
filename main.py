# name = "admin"
# print("Hello,", name)
# age = 20
# print(age)
# print(type(name))  # тип данных строка
# print(type(age))  # тип данных целое число
import os
from itertools import count
from multiprocessing.context import set_spawning_popen
from sys import base_prefix
from tkinter.font import names
from tokenize import endpats

# a = 4
# b = 5
# print(id(a))
# print(id(b))
# a = b
# print(a)

# a = b = c = 1
# print(a)
# print(b)
# print(c)

# print("строка\
#     символов")
# print("строка \nсимволов")
# print("Документ \"file.txt\"находится по пути: D\\folder\\file.txt")   ## экранирование
# s1 = "Hello"
# s2 = "Python"
# s3 = s1 + " " + s2 + '___'
# print(s3 * 3)

# print(6+2)
# print(6-2)
# print(6*2)
# print(6/2)
# print(6//2)
# print(7**2)
# print(7%2)

# a = 5
# b = 7
# c = 3
# print("Суммa:", + b + c)
# print("Произведение:",a * b * c)
# print("Средне арифметическое:",(a+b+c)/3)


# num = 10
# num += 5  # num = num + 5 = 15
# print(num)
# num -= 3  #  num = num - 3 = 12
# print(num)
# num *= 4  # 48print(num)

# num = 4321
# print(num)
# a = num % 10
# print("a:", a)
# num = num // 10
# print(num)
# b = num % 10
# print("b:", b)
# num = num // 10
# print(num)
# c = num % 10
# print("c:", c)
# num = num // 10
# print(num)
# d = num % 10
# print("d:", d)
# print("Обратное число:", a * 1000 + b * 100 + c * 10 + d)

# num = 4321  #4321
# print("Исходное число:", num)
# res = num % 10 * 1000  #1000
# num //= 10
# res += num % 10 * 100  #200
# num //= 10
# res += num % 10 * 10
# num //= 10
# res += num % 10
# print("Обратное число:", res)

# num1 = "2"
# num2 = 3
# res = int(num1) + num2
# res = num1 + str(num2)
# print(res)

# print(int(3.8))
# print(round(3.8))
# print(type(round(3.8)))
# print(round(3.895, 2))
# print(type(round(3.899, 2)))

# a = '5.2'
# b = 10
# c = float(a) + b
# print(c)

# name = "Виктор"
# age = 28
# print("Меня зовут ", name, ". Мне ", age, " лет.", sep="", end="\n")
# print("Новая строка")

# name = input("введите имя:")
# print("Ваше имя:", name)

# num = input("Введите число: ")
# power = input("Введите степень: ")
# num = int(num)
# power = int(power)
# res = num ** power
# print("Число", num, "в степени", power, "равно:", res)

# num = int(input("Введите число: "))
# power = int(input("Введите степень: "))
# res = num ** power
# print("Число", num, "в степени", power, "равно:", res)

# num1 = int(input("Введите число 1: "))
# num2 = int(input("Введите число 2: "))
# num3 = int(input("Введите число 3: "))
# num4 = int(input("Введите число 4: "))
# sum1 = num1 + num2
# sum2 = num3 + num4
# res = sum1 / sum2
# print(round(res, 2))

# b1 = True
# b2 = False
# print(type(b1))
# print(b1 + 5)
# print(b2 + 5)

# print(bool("python"))
# print(bool(""))
# print(bool(" "))
# print(bool(5))
# print(bool(0))
# print(bool(0.1))
# print(bool(0.0))
# print(bool(False))
# print(bool(None))
# a = None
# print(a)
# print(type(a))

# print(7 == 7)
# print(2 + 5 == 7 / 3)
# print(2 + 5 != 7 / 3)
# print(8 > 5)
# print(8 > 8)
# print(8 >= 8)
# print(9 > 9)
# print(9 >= 9)
# print("python" > "Python")  # 112 > 80

# print(2 < 4 < 9)  # True && True => True
# print(2 * 5 > 7 >= 4 + 3)  # 10 > 7 >= 7  True && True => True
# print(3 * 3 <= 7 >= 2)  # 9 <= 7 >= 2  False && True =>
#
# a = "10"
# b = 10
# c = a == b
# print(a, b, c)


##    урок 3 от 21.01.25

# print(5 - 3 == 2 and 1 + 3 == 4)  ##True and True (логическое - и)
# print(5 - 3 == 2 or 1 + 3 == 4)  ## логическое или
# print(not 9 - 5)

# cnt = 5
# if cnt < 10:
#     cnt = cnt + 1  ## оператора инкремента не существует
# print(cnt)

# age = int(input("Введите свой возраст:"))
# if age >= 18:
#     print("Доступ на сайт разрешен")
# else:
#     print("Доступ запрещен")

# a = 15
# b = 5
# if a > b:
#     print("a > b")
# elif a == b:
#     print("a == b")
# else:
#     print("b > a")

# a = input("Введите первую строку: ")
# b = input("Введите вторую строку: ")
# c = input("Введите третью строку: ")
#
# if a == b == c:
#     print("Треугольник равносторонний")
# elif a == b or b == c or a == c:
#     print("Треугольник равнобедренный")
# else:
#     print("Треугольник разносторонний")


# day = int(input("Введите день недели (цифрой): "))
# if 1 <= day <= 5:   # day >= 1 and day <=5:
#     print("Рабочий день - ", end="")
#     if day == 1:
#         print("понедельник")
#     if day == 2:
#         print("вторник")
#     if day == 3:
#         print("среда")
#     if day == 4:
#         print("четверг")
#     if day == 5:
#         print("пятница")
#
# elif day == 6 or day == 7:
#     print("Выходной день")
#     if day == 6:
#         print("суббота")
#     if day == 7:
#         print("воскресенье")
# else:
#     print("Такого дня недели не существует")


# mons = int(input("Введите номер месяца (цифрой): "))
# if 1 <= mons <= 12:
#     print("Время года - зима")
# elif 3 <= mons <= 5:
#     print("Время года - весна")
# elif 6 <= mons <= 8:
#     print("Время года - лето")
#
# )
# season = int(input("Введите номер месяца: "))
# if 1 <= season <= 12:
#     print("Время года: ", end="")
# if 1 <= season <= 2 or season == 12:
#     print("Зима")
# if 3 <= season <= 5:
#     print("Весна")
# if 6 <= season <= 8:
#     print("Лето")
# if 9 <= season <= 11:
#     print("Осень")
# else:
#     print("Такого месяца нет")


# n = int(input("Введите количество ворон: "))
# if 0 <= n <= 9:
#     print("На ветке ", end="")
# if n == 1:
#     print(n, "ворона")
# if 2 <= n <= 4:
#     print(n, "вороны")
# if 5 <= n <= 9 or n == 0:
#     print(n, "ворон")
# else:
#     print("Ошибка ввода")
# #
# n = int(input("Введите количество ворон: "))
# if 0 <= n <= 9:
#     print("На ветке ворон", end="")
# if n == 1:
#     print("а", n)
# if 2 <= n <= 4:
#     print("ы", n)
# if 5 <= n <= 9 or n == 0:
#     print("", n)
# else:
#     print("Ошибка ввода")

# password = "ad"
# match password:
#     case "admin":
#         print("Администратор")
#     case "user":
#         print("Пользователь")
#     case _:
#         print("Пароль не верен")

# day = 'понедельник'
# time = 12

# match day:
#     case 'понедельник' | 'вторник' | 'среда' | 'четверг' | 'пятница' if 9 <= time <= 12 or 14 <= time <= 17:
#         print("Рабочий день")
#     case 'суббота' | 'воскресенье':
#         print("Выходной день")
#     case _:
#         print("Такого дня недели не существует или нерабочее время")
#
#         # тернарное выражение
#
# a, b = 21, 20
# print(a if a > b else b)

# a, b = 21, 10
# print("На ноль делить нельзя" if b >= 1 else a / b)

# a, b = 30, 20
# print("На ноль делить нельзя" if b == 0 else a / b)

##  урок  23.01  Исключения

# try:
#     n = int(input("Введите делимое: "))
#     m = int(input("Введите делитель: "))
#     print(n / m)
# except ValueError:
#     print("Нельзя вводить строки")
# except ZeroDivisionError:
#     print("Нельзя делить на 0")

# try:
#     n = int(input("Введите делимое: "))
#     m = int(input("Введите делитель: "))
#     print(n / m)
# except (ValueError, ZeroDivisionError):
#     print("Нельзя вводить строки или нельзя делить на 0")
# else: # когда в блоке try не возникло исключение
#     print("Все нормально. Вы ввели", n, "и", m)
# finally: # выполнится в любом случае
#     print("Конец программы")

# n = input("Введите первое число: ")
# m = input("Введите второе число: ")
# try:
#     print(int(n) + int(m))
# except ValueError:
#     print(str(n) + str(m))


# n = input("Введите первое число: ")
# m = input("Введите второе число: ")
# try:
#     n = int(n)
#     m = int(m)
# except ValueError:
#     n = str(n)
# finally:
#     print(n + m)

## Циклы    (итерация  - 1 шаг цикла т.е. 1 раз выполняется while)

# i = 0
# while i < 5:
#     print("i=", i)
#     i += 1


# i = 1
# while i <= 20:
#     if i % 2 == 0:
#         print(i, end=" ")
#         i += 1


# j = 2
# while j <= 20:
#     print(j, end=" ")
#     j += 2

# n = int(input("Укажите количество символов: "))
# i = 1
# while i <= n:
#     print("*", end="\t")
#     i += 1
#
# n = int(input("Укажите количество символов: "))
# print("*" * n)

# a = int(input("Введите начало диапазона: "))
# b = int(input("Введите конец диапазона: "))
#
# res = 0
# while a <= b:
#     if a % 2:   # 1 3 5
#         print(a)
#         res += a
#     a += 1
# print("Сумма нечетных чисел:", res)

# n = input("Введите целое число: ")
# while type(n) is not int:      try:        n = int(n)      except ValueError: print("Число не целое!")
# n = input("Введите целое число: ")
# if n % 2 == 0:
#     print("Четное")
# else:
#     print("Нечетное")

# i = 0
# while i < 10:
#     if i == 3: i += 1
#     continue
#
# print(i, end=" ")
# if i == 5:
#     break
# i += 1
# print("\nЦикл завершен")
#
# i = 0
# while True:
#     print(i)
#     if i == 5:
#         break
# i += 1


# res = 1
# while True:
#     n = int(input("введите  число: "))
#     if n == 0:
#         break
# res *= n
# print(res)

# i = 1
# while i < 5:
#     print("Внешний цикл: i =", i)
#     j = 1
#     while j < 4:
#         print("\tВнутренний цикл: j=", j)
#         j += 1
#     i += 1


# урок 28.01
# for i in "Hello", "World":
#     print(i)

# range(start = по умолчанию 0 можно не писать, stop, step  = значение по умолчанию = 1 можно не писать )

# print(range(1, 10, 2))
# print(range(10))
#
# for i in (range(1, 15, 1)):
#     print(i, end=" ")

# a = int(input("Введите целое число: "))
# for i in range(1, a):
#     if a % i == 0:
#         print(i, end=" ")

# for i in range(10, 100):
#     if i % 10 == i // 10:
#         print(i, end=" ")

# for i in range(3):
#     if i == 1:
#         break
#     print(i)
# else:
#     print("Конец цикла")

# for i in range(2):  # for(let i = 0; i < 3; i++) и далее i = 1, 2
#     print("+++")
#     for j in range(2):
#         print("---")

# w = int(input("Введите ширину прямоугольника: "))
# h = int(input("Введите высоту прямоугольника: "))
# for i in range(h):
#     for j in range(w):
#         if i == 0 or i == h - 1 or j == 0 or j == w -1:
#             print("* ", end="")
#         else:
#             print("  ", end="")
#     print()

# string = [letter * 2 for letter in "Python"]
# print(string)
# print([letter * 2 for letter in "Python"])
#
# for letter in "Python":
#     print(letter * 2, end="\t")

# num = [i for i in range(30) if i % 2 == 0]
# print(num)
#
# print()
#
# for i in range(30):
#     if i % 2 == 0:
#         print(i, end="\t")

# спиcок (list)

# nums = [8, 3, 9, 4, 1, "one", True]
# print(nums)
# print(type(nums))
# print(nums[0])
# print(nums[4])
# print(nums[-1])
# print(nums[-2])
# print(nums[-7])

# nums = [8, 3, 9, 4, 1]
# print(nums)
# nums[1] = 256
# print(nums)
# nums[3] += 100
# print(nums)
# print("Длина списка:", len(nums))

# nums = [8, 3, 9, 4, 1]
# nums2 = [11, 12, 13]
# n = nums + nums2
# print(n)
# print(n * 2)

# print(list("Hello"))
# print(range(10))
# print(list(range(10)))
# print(list(range(2, 10)))
# print(list(range(10, 2, -3)))

# a = ["*" for _ in range(5)]
# print(a)

# n = 5
# a = [i ** 2 for i in range(1, n + 1)]
# print(a)

# a = [0] * int(input("Введите количество элементов списка: "))
# print(a)
# for i in range(len(a)):
#     a[i] = int(input("->: "))
# print(a)


# b = [int(input("-> ")) for i in range(int(input(" n = ")))]

# урок 30.01

# a = list(range(10, 100, 10))
# print(a)
#
# for i in range(len(a)):
#     print(a[i], end=" ")
# print()
#
# for i in a:
#     print(i + 2, end=" ")


# a = [int(input("-> ")) for i in range(int(input(" n = ")))]
#
# for i in range(len(a)):
#     if i % 2 == 0:
#         print(a[i], end=" ")
#
# for i in range(0, len(a), 2):
#     print(a[i], end=" ")

# a = [int(input("-> ")) for i in range(int(input(" n = ")))]
# print(a)
# for i in range(1, len(a)):
#     if a[i] > a[i - 1]:
#         print(a[i], end=" ")

# n = list(range(21, 41))
# print(n)
# k = s = 0
#
# for i in range(len(n)):    #  range(0, len(a), 1) - аналог записи range
#     if n[i] % 2 == 0:
#         k = k + 1
#     else:
#         s += n[i]
# print("Количество четных элементов: ", k)
# print("Сумма нечетных элементов:", s)

#  2 вариант без использования индексов. Обращение к коллекции элементов
# for i in n:
#     if i % 2 == 0:
#         k = k + 1
#     else:
#         s += i
# print("Количество четных элементов: ", k)
# print("Сумма нечетных элементов:", s)

# a = [int(input("-> ")) for i in range(int(input(" n = ")))]
# sum1 = kol = 0
#
# for i in a:
#     if i != 0:
#         kol += 1
#     sum1 += i
#
#
# print(sum1/kol)


# a = [int(input("-> ")) for i in range(int(input(" n = ")))]
# sum1 = kol = 0
# for i in range(len(a)):
#     if a[i] != 0:
#         kol += 1
#         sum1 += a[i]
# print(sum1 / kol)


# lst = [7, 9, 2, 1, 17]
# print(lst)
# lst[0], lst[1] = lst[1], lst[0]
# print(lst)

# срез
# список[start: stop: step]

# s = [9, 7, 2, 1, 17, 8]
# print(s)
# print(s[1:4])
# print(s[:])
# print(s[2:])
# print(s[:2])
# print(s[::2])
# print(s[0:-1])  # развернет элементы наоборот
# print(s[-1:0:-1])
# print(s[10:20])

# Создать срезы из списка

# lst = list(range(1, 8))
# print(lst)
# print(lst[::-1])
# print(lst[::2])
# print(lst[1::2])
# print(lst[:1])
# print(lst[::-7])
# print(lst[-1:])
# print(lst[3:4])
# print(lst[4:7])
# print(lst[4:])
# print(lst[4:1:-1])
# print(lst[2:5])

# str = "Hello Python"
# print(str[0:3])
# print(str[::-1])
#
# st = "123456"
# print(st[1:3])
# num = st[::-1]
# print(num)
# print(type(num))  # строка
# num = int(num)    # преобразуем строку в число
# print(num)
# print(type(num))

# lst = list(range(1, 8))
# print(lst)
# lst[1:3] = [0, 0, 0, 0]
# print(lst)
# lst[1:2] = [20]
# lst[3] = [40, 50]  # вставляем вложенный список по номеру индекса
# print(lst)
# lst[15:16] = [100]  # вставляет в конец списка
# print(lst)

# методы списка
#
# print(dir(list))
# lst = list(range(1, 8))
# print(lst)
# lst.append(99)    # добавляет 1 элемент в конец списка
# print(lst)
# lst.extend([1, 2, 3])   # добавляет список элементов в конец списка
# print(lst)
# lst.insert(1, 100)  # добавляет элемент (второй параметр) по заданному индексу (первый параметр)
# print(lst)                         # в конец списка не добавляет

# s = [0, 0, 0]
# n = int(input("Количество элементов списка: "))
# for num in range(n):
#     x = int(input("Введите число: "))
#     s.append(x)
#     # s.insert(0, x)  # 5, 6, 7, 8, 9
# print(s)

# a = [5, 9, 2, 1, 4, 3, 4, 2]
# b = [4, 2, 1, 3, 7, 2]
# c = []

# for i in a:
#     for j in b:
#         if i in c:
#             continue
#         if i == j:                     # проверка 5 == 4, 5 == 2, 5 == 1 и т.д. проверяется вложенный цикл
#
#             if i == j:
#                 c.append(i)
#             break
# print(c)


# for element in a:
#     if element in b and element not in c:  # 2, 1, 4, 3, 4, 2
#         c.append(element)
# print(c)

# a = [1, 2, 3]
# b = [11, 22, 33, 4, 2]
# c = []
#
# for i in range(len(a)):
#     c.append(a[i])
#     c.append(b[i])
# for i in range(len(a), len(b)):
#     c.append(b[i])
#
# print(c)
#
# a = [1, 2, 3, 55, 66]
# b = [11, 22, 33]
# c = []
# if len(a) > len(b):    a, b = b, a for
# i in range(
#     len(a)):  # 0 1 2

# c.append(a[i])    c.append(b[i])for i in range(len(a), len(b)):  # range(3, 5):    c.append(b[i])# if len(b) > len(a):#     for i in range(len(a)):  # 0 1 2#         c.append(a[i])#         c.append(b[i])#     for i in range(len(a), len(b)):  # range(3, 5):#         c.append(b[i])# else:#     for i in range(len(b)):  # 0 1 2#         c.append(a[i])#         c.append(b[i])#     for i in range(len(b), len(a)):  # range(3, 5):#         c.append(a[i])print(c)  # [1, 11, 2, 22, 3, 33, 4, 2]

# lst = [11, 1, 22, 2, 33, 3, 55, 66]

# lst[5:] = []
# print(lst)
# del lst[2]
# print(lst)

# lst.remove(22)   # удаляет элемент из списка по значению (первое вхождение)
# print(lst)
#
# last = lst.pop()  # удаляет последний элемент из списка и возвращает его
# print(last)
# print(lst)
#
# second = lst.pop(0)  # удаляет элемент по индексу и возвращает его, если индекса нет то получаем исключение
# print(second)
# print(lst)
#
# lst.clear()   # удалил все значения из списка
# print(lst)

# print("Введите элементы списка: ")
# a = [int(input("-> ")) for i in range(int(input("n = ")))]
# print("Введите индекс: ")
# k = int(input("k = "))
# a.pop(k)
# print(a)

# lst = [11, 1, 22, 2, 33, 3, 55, 66, 33]
# name = 3
# ind = lst.index(name, 5)   # возвращает индекс первого вхождения искомого элемента, можно указать диапазон от какого до какого индекса мы производим поиск, может выбрасываться исключение
#
# if name in lst:
#     ind = lst.index(name)
#     print(ind)
# print(lst)

# lst = [11, 1, 22, 2, 33, 3, 55, 66, 33]
# a = lst.copy()  # создает копию списка по другому адресу
# print(lst)
# print(a)

# lst = [11, 1, 22, 2, 33, 3, 55, 66, 33]
# # lst.reverse()  # развернул элементы списка в противоположную сторону
# # print(lst)
# lst.sort(reverse=True)
# print(lst)


# s = ["Виталий", "Сергей", "Александр", "Анна"]
# s.sort(key=len, reverse=False)
#
# new_lst = sorted(lst, reverse=True)
# print(new_lst)
# print(lst)
# s.sort(key=len, reverse=False)
# print(s)

# Генерация случайных данных


#
# print(random.random())
# print(random.randint(5, 10))
# print(random.randrange(5, 10, 2))

# city_list = ['Москва', 'Новосибирск', 'Воронеж', 'Сочи', 'Екатеринбург']
# s = [55, 66, 77, 88, 99, 5, 7, 9, 1, 2, 4, 3, 8]
#
# # print(random.choice(city_list))
# # print(random.choice(s))
# # print(random.choices(city_list, k=3))
# # print(random.choices(s, k=3))
# random.shuffle(city_list)
# random.shuffle(s)
# print(city_list)
# print(s)


# import random
# mas = [random.randint(0, 100) for i in range(10)]
# print(mas)
# print(len(mas))   # длина списка
# print(min(mas))  # минимальный элемент из списка
# print(max(mas))  # максимальный элемент списка
# print(sum(mas))  # сумма элементов списка

# mas = [random.randint(0, 100) for i in range(10)]
# print(mas)
# maximum = max(mas)
# print("Max =", maximum)
# mas.insert(0, maximum)
#
# print(mas)

# mas = [random.randint(0, 10) for i in range(10)]
# print(mas)
# print(2 not in mas)

# lst = [5]
# # if len(lst) == 0:
# #     print("Список пустой")
#
# # print(bool(lst))
#
# if not lst:
#     print("Список пустой")
# else:
#     print("В списке есть элементы")

# m = [
#     [1, 2, 3, 4],   # 0 индекс
#     [5, 6, 7, 8],   # 1 индекс
#     [9, 10, 11, 12]  # 2 индекс
# ]
# print(m)
# print(len(m))
# print(m[1])
# print(m[1][2])
# print(m[2][1])
# print(m[1][3])
# print("Вариант 1")
# for row in range(len(m)):  # 0 1 2 приходят индексы
#     for col in range(len(m[row])): # col = [0], [1], [2], [3]
#         print(m[row][col], end="\t")
#     print()
#
# print("Вариант 2")
# for row in m:
#     for x in row:
#         print(x, end="\t")
#     print()


import math  # либо from math import *  либо  from math import sqrt, ceil, floor (этот более производительный)

# print(math.sqrt(4))
# print(math.ceil(3.2))
# print(math.floor(3.2))

# from math import pi
# # print(pi)
# #
# radius = int(input("Введите радиус окружности: "))
# print("Длина окружности:", round(2 * pi * radius, 2))
#
# import time
# # Модули
# import locale
#
# print(time.time())
# print(time.ctime(778863234))
# res = time.localtime()
# print(time.localtime().tm_year, "-0", res.tm_mon, "-", res.tm_mday, sep="")
#
# # print(res.tm_year, "-0", res.tm_mon, "-0", res.tm_mday, sep="")
# print(time.strftime("Today is %B %d, %Y"))
# print(time.strftime("%m/%d/%Y, %H:%M:%S"))
# #
# locale.setlocale(locale.LC_ALL, "ru")  # указываем язык страны для которой делается сайт
# print(time.strftime("Сегодня: %B %d, %Y, %A"))

# start = time.monotonic()
# pause = 5
# print("Программа запущена")
# #
# time.sleep(pause)
# result = time.monotonic() - start
# print("Программа выполнена за", result, "секунд")

# Функции  (урок  - 11.02)


# def hello(name, age):
#     print("Меня зовут " + str(name) + ". Мне " + str(age) + " лет.")
#
#
# hello("Irina Сидорова", 28)
# hello("Ivan Пупкин", 15)


# def get_sum(a, b):
#     print(a + b)
#
#
# x = 2
# y = 5
# get_sum(x, y)
# get_sum("abc", "def")
# get_sum(55, 55)
# def print_line(lens, a, b):
#     for i in range(lens):
#         if i % 2 == 0:
#             print(a, end="")
#         else:
#             print(b, end="")
#     print()
#
#
# print_line(9, "+", "-")
# print_line(7, "X", "O")

# def get_sum(a, b):
#     return a + b
#
#
# lens = 2
# bens = 5
# res = get_sum(lens, bens)
# print(res)


# def max_value(one, two):
#     if one > two:
#         return  one
#     else:
#         return two
#
#
# print(max_value(9, 6))
# print(max_value(9, 16))


# def get(x, y):
#     if x > y:
#         return x - y
#     else:
#         return x + y
#
#
# a = int(input("Введите число a =  "))
# b = int(input("Введите число b =  "))
# print(get(a, b))

# def add(x, y):
#     if x > y:
#         return x - y
#     else:
#         return x + y
#
#
# a = int(input("a = "))
# b = int(input("b = "))
# print(add(a, b))

# def change(lst):
#     lst[0], lst[-1] = lst[-1], lst[0]
#     return lst


# def change(lst):
#     end = lst.pop()
#     start = lst.pop(0)
#     lst.append(start)
#     lst.insert(0, end)
#     return lst
#
# print(change([1, 2, 3]))
# print(change([9, 12, 33, 54, 105]))
# print(change(["c", "л", "о", "н"]))


# def is_first_big(x, y):
#     if x > y:
#         return True
#     else:
#         return False


# print(is_first_big(10, 5))
# print(is_first_big(5, 10))

# a = int(input("Введите первое число: "))
# b = int(input("Введите второе число: "))
# if is_first_big(a, b):
#     print("Первое число больше второго")
# else:
#     print("Второе число больше первого")

# def check_password(password):
# has_upper = False
# has_lower = False
# has_num = False
# for ch in password:
#     if"A" <= ch <= "Z": has_upper = True
# if "a" <= ch <= "z":
#     has_lower = True
# if "0" <= ch <= "9":
#      has_num = True
# if len(password) >= 8 and has_upper and has_lower and has_num:
#     return True
# return False
# p = input("Введите пароль: ")
# if check_password(p):
#     print("Это надежный пароль")
# else:
#     print("Это ненадежный пароль")

# def get_sum(a, b, c=0, d=1):
#     return a + b + c + d
# # print(get_sum(7, 9, d=3, c=5))
#
#
# print(get_sum(1, 5, 2, 7))
# print(get_sum(1, 5, 2))
# print(get_sum(1, 5))
# print(get_sum(1, 5, d=2))


# def res(a=20, b='-'):
#     return a * b
#
#
# print(res(10, "+"))
# print(res(5, "*"))
# print(res(15, "#"))
# print(res(7))
# print(res())


# def display_info(name, age):
#     print("Name:", name, "\nAge:", age)
#
#
# display_info("Ira", 23)
# display_info(23, "Ira")
# display_info(age=23, name="Ira")
# display_info("Igor", age=23, name="Ira")

#  урок 13.02

# lst1 = [1, 2, 3]
# lst2 = [1, 2, 3]
# print(lst1, id(lst1))
# print(lst2, id(lst2))
# print(lst1 == lst2)
# print(lst1 is lst2)
# a = "Hello"
# b = "Hello"
# print(a, id(a))
# print(b, id(b))
# print(a == b)
# print(a is b)

# lst1 = [1, 2, 3]
# print(lst1, id(lst1))
# lst1.append(4)
# print(lst1, id(lst1))
# lst1.pop(1)
# print(lst1, id(lst1))

# a = "Hello"
# print(a, id(a))
# a = a + "!"
# print(a, id(a))

# a = 5
# print(a, id(a))
# a = a + 3
# print(a, id(a))


# тип данных кортэж - tuple


# lst = [10, 20, 20]     ## - это список
# tpl = (10, 20, 30)     ## - это кортеж
#
# print(lst.__sizeof__())   # показывает размер элемента в байтах
# print(tpl.__sizeof__())   # показывает размер элемента в байтах


# a = 1, 2, 3, 4, 5, 6
# a = tuple("hello")
# b = list("hello")
# print(a, type(a))  # класс кортеж
# print(b, type(b))   # класс список

# a = (1, 2, 3, 4, 5, 6)
# print(a[2])
# print(a[1:3])
#
# from random import randint                    # заполнение кортежа случайными числами
#
# # print(tuple(i for i in range(10)))
# #
# # print(tuple(input("-> ") for i in range(5)))  # пользователь с клавиатуры вводит 5 элементов
#
# print(tuple(randint(50, 100) for i in range(10)))   # заполнение кортежа случайными числами от 50 до 100
# (генератор кортежа)


# t1 = tuple("hello")
# t2 = tuple("world")
# t3 = t1 + t2
# print(t3 * 2)
# print(t3)
# # print(len(t3))
# # print(t3.count('l'))
# print(t3.index('l', 0))
# if 'a' in t3:
#     print(t3.index('a'))
# elif 'h' in t3:
#     print(t3.index('h'))
# else:
#     print('Такого элемента нет')
#
# for i in t3:
#     print(i, end=" ")

# def slicer(tpl, el):
#     if el in tpl:                          # проверяем есть ли 8 ка в первом кортеже
#         if tpl.count(el) == 1:             # проверяем если кол-во элементов (8 ка) == 1
#             first = tpl.index(el)          # находим индекс 8 -ки
#             return tpl[first:]             # tpl [2:] возвращаем срез от индекса 8-ки и до конца
#         else:
#             first = tpl.index(el)                   # находим индекс первой 8-ки во втором списке
#             second = tpl.index(el, first + 1)       # находим индекс второй 8-ки во втором списке
#             print("first", first)
#             print("second", second)
#             return tpl[first:second + 1]   # cрез tpl[1:5]
#
#     else:
#         return ()
#
#
# print(slicer((1, 2, 3), 8))
# print(slicer((1, 8, 3, 4, 8, 8, 9, 2), 8))
# print(slicer((1, 2, 8, 5, 1, 2, 9), 8))

# t = (True, 11, "Phyton", [4, 5, 6], ["hello", "world"])
# print(t, id(t))
# t[4][0] = 'new'
# print(t, id(t))
# t[4].append("hi")
# print(t, id(t))

# Распаковка кортежа

# t = (1, 2, 3)
# # x = t[0]
# # y = t[1]
# # z = t[2]
# x, y, z = t
# print(x, y, z)
#
# def get_user():
#     name = "Tom"
#     age = 22
#     is_married = False
#     return name, age, is_married
#
#
# user = get_user()
# # print(user, type(user))
# # first_name, year, married = user
# # print(first_name)
# # print(year)
# # print(married)
# first_name, year, married = get_user()
# print(first_name + " " "Kruz")
# print(year * 2)
# # print(married)


# lst = [1, 2, 3, 4, 5]     # список
# print(lst, type(lst))     # класс список
# tpl = tuple(lst)          # c помощью tuple преобразовываем список в кортеж
# print(lst, type(tpl))     # кортеж
# lst2 = list(tpl)          # c помощью list преобразовываем кортеж обратно в список
# print(lst2, type(lst2))   # список


# countries = (
#     ("Германия", 80.2, (("Берлин", 3.326), ("Гамбург", 1.718))),
#     ("Франция", 66, (("Париж", 2.2), ("Марсель", 1.6))),
# )
#
# # print(countries)
# for country in countries:
#     country_name, country_population, cities = country
#     print("\nСтрана: ", country_name, ", население = ", country_population, sep="")
#     for city in cities:
#         city_name, city_population = city
#         print("\tГород: ", city_name, ", население = ", city_population, sep="")


# tpl = tuple(input("Введите строку: "))
# print(tpl)
#
# lst = []
# for i in range(len(tpl)):
#     if tpl[i] not in lst:
#         lst.append(tpl[i])
#
# print(lst)
# for i in range(len(lst)):
#     print("Количество", lst[i], "-", tpl.count(lst[i]))

# Множество  (set) 18.02.25

# s = {"red", "yellow", "green", "yellow", "green"}
# print(s)
# print(type(s))
# print(len(s))

# a = set("hello")
# print(a, type(a))


# s = {i * i for i in range(10)}
# print(s)

# lst = [10, 2, 2, 2, 2, 3, 3, 8, 8, 9, 9, 10]
# print(lst)
# # st = {i for i in lst if i % 2 == 0}
# # print(st)
# st = set(lst)    # преобразовали список в set и отбросили дублирующиеся элементы
# lst2 = list(st)  # преобразовали этот же set обратно в список
# print(lst2)


# t = {"red", "yellow", "green"}
# print("green" in t)
# print("blue" in t)

# lst = ["ab_1", "ac_2", "bc_1", "bc_2"]
# print({i for i in lst if 'a' in i})         # это выводится set (множество)
# print(tuple(i for i in lst if 'a' in i))    # это выводится tuple (кортеж)
# print(tuple("A" + i[1:] if i[0] == "a" else "B" + i[1:] for i in lst))
# print(["A" + i[1:] if i[0] == "a" else "B" + i[1:] for i in lst if i[1] == "c"])   #  это выводится список
# lst2 = []
# for i in lst:
#     if i[1] == "c":
#         if i[0] == "a":
#             lst2.append("A" + i[1:])
#         else:
#             lst2.append("B" + i[1:])
# print(lst2)


# print(dir(set))

# a = {"red", "yellow", "green"}
# print(a)
# a.add("black")  # добавление элемента в множество
# print(a)
#
# a.remove('yellow')  # удаляет элемент по значению
# print(a)
#
# # a.remove('blue')  # Key Error
# # print(a)
#
# a.discard('blue')  # удаляет элемент по значению но не выбрасывает исключение если этого элемента нету
# print(a)

# a.pop()    # удаляет первый элемент из множества
# print(a)
#
# a.clear()   # очищает множество
# print()

# a = {0, 1, 2, 3}
# b = {4, 2, 3, 1}
# c = a.union(b)  # {0, 1, 2, 3, 4}
# # c = a | b
# print(c)
# a |= b
# print(a)
# c = a & b
# print(c)

# s1 = {1, 2}
# s2 = {3}
# s3 = {4, 5}
# s4 = {3, 2, 6}
# s5 = {6}
# s6 = {7, 8}
# s7 = {9, 8}
#
# s = s1 | s2 | s3 | s4 | s5 | s6 | s7
# s = s1.union(s2, s3, s4, s5, s6, s7)
# print(s)
# print("Кол-во уникальных элементов:", len(s))
# print("Min:", min(s))
# print("Max:", max(s))

# s1 = "Hello"
# s2 = "How are you"
#
# a = set(s1) & set(s2)
# print(a)
#
# for i in a:
#     print(i, end="")

# a = {0, 1, 2, 3, 4}
# b = {3, 2, 1}
# c = a <= b
# print(c)

# словарь (dict)

# lst = ["one", "two"]
# d = {"first": "one", "second": "two"}
# print(lst[1])
# print(d["second"])

# d = {}
# print(d)
# print(type(d))

# d = dict(a="Hello", b="World")
# print(d)
# print(type(d))

# d = {0: "text", "one": 45, (1, 2): "Кортеж", 42: [9, 8], True: 1, False: 0, "a": "Кортеж", 1: "один", "a": 56}
# print(d)

# user = [
#     ["a", 1],
#     ["b", 2],
#     ["c", 3],
# ]
#
# print(user)
# new_dict = dict(user)
# print(new_dict)

# урок 20.02   словари (продолжение)

# d = {i: i ** 2 for i in range(1, 8)}
# print(d)

# del d[3]          # удаление элемента по ключу
# print(3 in d)   # проверяет наличие ключа в словаре
# print(25 in d)
# key = 9
# if key in d:     # обработка ключа что бы не получить исключение
#     del d[key]
# print(d)
#
# try:                # обработка с помощью Try что бы не получить исключение
#     del d[key]
# except KeyError:
#     print("Элемента с ключом", key, "нет в словаре")
# print(d)

# d = {'x1': 3, 'x2': 7, 'x3': 5, 'x4': -1}
#
# res = 1
# for key in d:
#     print(key, ':', d[key])
#     res *= d[key]
#
# print(res)

# d = dict()
# d[1] = input("->")
# d[2] = input("->")
# d[3] = input("->")
# d[4] = input("->")
# print(d)

# d = {i: input("->") for i in range(1, 5)}     # генератор словаря
# print(d)
# dislike = int(input("Какой элемент исключить: "))
# del d[dislike]
# print(d)

# goods = {'1': ['Core-i3-4330', 9, 4500],
#          '2': ['Core i5-4670K', 3, 8500],
#          '3': ['AMD FX-6300', 6, 3700],
#          '4': ['Pentium G3220', 8, 2100],
#          '5': ['Core i5-3450', 5, 6400],
#          }
# for i in goods:
#     print(i, ") ", goods[i][0], " - ", goods[i][1], " шт. по ", goods[i][2], "руб", sep="")
#
# while True:
#     n = input("№: ")
#     if n == "0":
#         break
#     else:
#         if n in goods:
#             while True:
#                 try:
#                     count = int(input("Количество: "))
#                     goods[n][1] += count
#                     break
#                 except ValueError:
#                     print("Значение не корректное. Введите число")
#
#         else:
#             print("Такого ключа не существует")
#
# for i in goods:
#     print(i, ") ", goods[i][0], " - ", goods[i][1], " шт. по ", goods[i][2], "руб", sep="")

#  Методы словарей


# d = {"A": 1, "B": 2, "C": 3}
# print(d)
#
# print(d.keys())  # список ключей
# print(d.values())  # список значений
# print(d.items())   # список ключей и значений в виде кортежа
#
# for i, j in d.items():
#     print(i, ":", j)

# d = {"A": 1, "B": 2, "C": 3}
# d2 = d.copy()             # возвращается копия словаря
# print("D =", d)
# print("D2 =", d2)

# d = {"A": 1, "B": 2, "C": 3}
# print(d)
# # d.clear()  # очистка словаря
# # item = d.pop("B")   # удаление элемента по ключу
# item = d.pop("M", "Такого ключа нет")
# items = d.popitem()  # удаляется последний элемент и возвращается кортеж из ключа и значения
# # print(d)
# print(items)
# print(d)


# d = {"A": 1, "B": 2, "C": 3}
# print(d)
# # print(d["B"])
# value = d.get("B", "Такого ключа нет")  # получает значение по заданному ключу
# print(value)
# item = d.setdefault('B', 5)  # по заданному ключу добавляет новый ключ и значение, если ключа не существовало
# print(d)
# print(item)

# d = {"A": 1, "B": 2, "C": 3}
# # d2 = {"R": 7, "Q": 9}
# d2 = [("R", 7), ("Q", 9)]
# print(d)
# print(d2)
# # d3 = d | d2
# d.update(d2)
# print(d)

# d = {"name": "Kelly", "age": 25, "salary": 8000, "city": "New York"}
#
#
# new_d = dict()
# # new_d['name'] = d.pop("name")
# # new_d['salary'] = d.pop("salary")
# new_d['name'], new_d['salary'] = d.pop("name"), d.pop("salary")
# # d.pop('name')
# # d.pop('salary')
# print(d)


# d = {"name": "Kelly", "age": 25, "salary": 8000, "city": "New York"}
#
# d['location'] = d.pop("city")  # перезаписываем ключ со значением
# print(d)
# d['sam'] = d.pop('age')
# print(d)

# d = {"first": {1: "one", 2: "two", 3: "three"}, "second": {4: "four", 5: "five"}}
# print(d)
#
# for x in d:
#     print(x)
#     for y in d[x]:
#         print("\t", y, ":", d[x][y], sep='')
#
# for x, y in d.items():
#     print(x)
#     for i, j in y.items():
#         print("\t", i, ": ", j, sep="")


# d = {"один": 1, "два": 2, "три": 3, "четыре": 4}
# print({v: k for k, v in d.items()})
#
# print({k: v for k, v in d.items() if v <= 2})          # задача вывести только 2 первых ключа и значения

# d = {i: i * 5 for i in [10, 20, 30, 40, 50]}
# print(d)
#
# s = "Hello"
# d1 = {i: i * 3 for i in s}
# print(d1)


# lst = ["one", 1, 2, 3, "two", 10, 20, "three", 15, 36, 60, "four", -20]
#
# d = dict()
# s = None
#
# for i in lst:
#     if type(i) is str:      # type (i) == str
#         d[i] = []
#         s = i               # s = "one", "two"
#     else:
#         d[s].append(i)
#
# print(d)


# zip([],[])
#
# d = dict(zip([1, 2, 3], ['one', 'two', 'three']))
# print(d)
#
#
# d1 = list(zip([1, 2, 3], ['one', 'two', 'three']))    # обьединяет несколько последовательностей в одну
# print(d1)

# a = [1, 2, 3]
# b = ['one', 'two', 'three']
# d = {k: z for k, z in zip(b, a)}
# print(d)

# a = [1, 2, 3]
# c = list(zip(a))
# print(c)


# one = {"name": "Igor", "surname": "Pavlov", "job": "Consultant"}
# two = {"name": "Irina", "surname": "Vetrova", "job": "Manager"}
#
# for (k1, v1), (k2, v2) in zip(one.items(), two.items()):
#     print(k1, '->', v1)
#     print(k2, '->', v2)

# lst = [(1, 'a'), (2, 'b'), (3, 'c'), (4, 'd')]
# a, b = zip(*lst)   # распаковка кортежа на 2 последовательности
# print(a)
# print(b)

# letter = ['b', 'a', 'd', 'c']
# number = [3, 4, 1, 2]
# d = dict(zip(letter, number))
# print(d)
#
# data1 = list(zip(letter, number))
# print(data1)
# data1.sort()
# print(data1)
#
# d2 = dict(data1)
# print(d2)

# letter = ['b', 'a', 'd', 'c']
# number = [3, 4, 1, 2]
# d = dict(zip(letter, number))
# print(d)
# d1 = sorted(zip(letter, number))
# print(d1)
# d2 = sorted(d.items())
# print(d2)
# d3 = dict(d2)
# print(d3)


# a = [1,2,3]
# b = [a, 4, 5, 6]
# b1 = [*a, 4, 5, 6]    # обьединение списка, кортежа сета (убирает скобки)
# print(b)
# print(b1)

# one = {"один": 1, "два": 2}
# two = {"три": 3, "четыре": 4}
# print({**one, **two})      # преобразует в один словарь, убирает лишние скобки


# colors = ["red", "yellow", "green"]
# # i = 1
# # for color in colors:
# #     print(i, ")", color, sep="")
# #     i += 1
# print()
# #
# for j, color in enumerate(colors, 1):             # вывод через функцию счетчика enumerate (счетчик)
#     print(j, ")", color, sep="")

# d = {"один": 1, "два": 2, "три": 3, "четыре": 4}
#
# for i, (k, v) in enumerate(d.items(), 1):          # использование функции счетчика enumerate со словарем
#     print(i, ")", k, ":", v, sep="")


# def summa(*param):
#     res = 0
#     for n in param:
#         res += n
#     return res
#
# print(summa(1,2,3,4,5,6,7,8,9))
# print(summa(7, 8, 9))

# def average(*args):
#     sr = sum(args) / len(args)
#     print(sr)
#
# #     res = []
# #     for num in args:
# #         if num < sr:
# #             res.append(num)
# #
# #     return res
# #
# print(average(1,2,3,4,5,6,7,8,9))
# print(average(3,6,1,9,5))

# def info(**data):
#     for k, v in data.items():
#      print(k, ":", v)
# print()
# info(name="Irina", surname="Vetrova", age=22)
# info(name="Igor", phone="456789", age=22, email="igor@mail.ru")

# 27.02  занятие

# def func1(*args):
#     print(args)
#     print(args[0])
#
#
# def func2(**kwargs):
#     print(kwargs)
#
#
# func1(1,2,3, 4, 5,6)
# func2(one=123, two=456)


# Области видимости (scape)

# name = "Tom"             # глобальная переменная
#
#
# def hi():
#     global name
#     name = "Sam"
#     surname = "Jonson"     # локальная переменная
#     print("Hello", name)
#
#
# def bye():
#     print("Gud buy", name)
#
#
# hi()
# bye()
# print(name)

# import builtins
# #
# name = dir(builtins)
#
# for t in name:
#     print(t)

# x = 4


# def func():
#     x = 2           # 2
#
#     def inner():
#         print("x =", x)    #  4
#         print(x + 3)       #  5
#
#     inner()                #  3
#
#
# func()             # 1

#   Вложенные функции

# def outer(_):
#     def inner():
#         print("Hello", _)
#
#     inner()
#
#
# outer("World")


# def fun1():
#     a = 6    # 2
#
#     def fun2(b):
#         a = 4      # 5
#         print("Сумма: ", a + b)     # 6
#
#     print("a:", a)   # 3
#     fun2(3)        # 4
#
#
# fun1()    # 1

# x = 25
#
#
# def fn():
#     global t
#     a = 30
#     t = a
#
#     def inner():
#         nonlocal a    # перезаписывает значение вышестоящей локальной переменной в пределах функции
#         a = 35
#         print("a =", a)
#
#     inner()
#     t = a
#
#
# fn()
# c = x + t   # 25 + 30 = 55
# print(c)


# def fn1():
#     x = 25
#
#     def fn2():
#         x = 33     # 55
#
#         def fn3():
#             nonlocal x     # переносит значение х = 55 в вышестоящую переменную
#             x = 55
#
#         fn3()
#         print("fn2.x=", x)   # 33 -> 55
#
#     fn2()
#     print("fn1.x=",x)      # 25
#
#
# fn1()


# def outer(a1, b1, a2, b2):
#     a = 0  # 1
#     b = 0   # 7
#
#     def inner():
#         nonlocal a, b
#         a = a1 + a2
#         b = b1 + b2
#         print(a)
#         print(b)
#
#     inner()
#     return [a, b]
#
#
# print(outer(2, 3, -1, 4))


# def outer(a, b, c):
#
#     def inner(i, j):
#         return i * j
#
#     s = 2 * (inner(a, b) + inner(a, c) + inner(b, c))     # вариант задачи когда переменная обьявлена как локальная
#     return s
#
#
# print(outer(2, 4, 6))
# print(outer(5, 8, 2))
# print(outer(1, 6, 8))

# замыкание

# def outer(n):
#     def inner(x):
#         return n + x
#
#     return inner        # замыкание это когда одна функция возвращает вложенную функцию, но ее при этом не вызывает
#
# func1 = outer(5)
# print(func1(10))


# def func1():
#     a = 1
#     b = "line"
#     c = [1, 2, 3]
#
#     def func2():
#         nonlocal a, b
#         c.append(4)
#         a = a + 1
#         b = b + "!"
#         return a, b, c
#
#     return func2
#
#
# func = func1()
# print(func())


#  Анонимные функции (lambda - выражения)  урок 04.03


# print((lambda x, y: x + y)(1,2))
#
# func = lambda x, y: x + y    # не желательно так прописывать функцию т.к. получается мы даем имя для lambda функции
# print(func(1, 2))
# func = (lambda x, y: x + y)(1,2)
# print(func)
#
# func = (lambda x, y: x + y)(1, 2)   # так можно прописывать
# print(func)
# print((lambda a, b, c: a + b + c)(10, 20, 30))
# print((lambda a, b, c=3: a + b + c)(10, 20))
# print((lambda a, b=2, c=3: a + b + c)(10))
# print((lambda a=1, b=2, c=3: a + b + c)())
#
# print((lambda *args: sum(args))(1, 2, 3, 4))

# tpl = (
#     lambda x: x * 2,
#     lambda x: x * 3,
#     lambda x: x * 4,
# )
#
# for i in tpl:
#     print(i("abc___"))


# def outer(n):
#     def inner(x):
#         return n + x
#
#     return inner
#
#
# f = outer(42)
# print(f(3))
#
#
# def outer(n):
#     return lambda x: n + x
#
#
# f = outer(42)
# print(f(3))
#
#
# outer = lambda n: lambda x: n + x      # не рекомендуется lamda выражение обььявлять в переменной
# f = outer(42)
# print(f(3))
#
# print((lambda n: lambda x: n + x)(42)(3))


# print((lambda a: lambda b: lambda c: a + b + c)(2)(4)(6))

# d = {"b": 10, "a": 15, "c": 4}
# print(d)
# lst = list(d.items())
# print(lst)
# lst.sort(key=lambda i: i[1])    # отсортировка элементов словаря через список (list) по значениям с примен. lambda
# print(lst)
# print(dict(lst))

# players = [{'name': 'Антон', 'last name': 'Бирюков', 'rating': 9},
#            {'name': 'Алексей', 'last name': 'Бодня', 'rating': 10},
#            {'name': 'Федор', 'last name': 'Сидоров', 'rating': 4},
#            {'name': 'Михаил', 'last name': 'Семенов', 'rating': 6}]
#
#
# res = sorted(players, key=lambda i: i["last name"])
# print(res)
#
# res = sorted(players, reverse=True, key=lambda i: i["rating"])
# print(res)
#
# res = sorted(players, key=lambda i: i["rating"])
# print(res)


# lst = [lambda x, y: x + y, lambda x, y: x - y, lambda x, y: x * y, lambda x, y: x / y]
# print(lst[1](12, 6))    # высчитывает значение функции lambda по номеру индекса из общего списка

# d = {1: lambda: print("Понедельник"), 2: lambda: print("Вторник"), 3: lambda: print("Среда"),
#      4: lambda: print("Четверг"), 5: lambda: print("Пятница"), 6: lambda: print("Суббота"),
#      7: lambda: print("Воскресенье")}
#
# d[4]()      # вызываем функцию lambda по номеру ключа в словаре

# print((lambda a, b: a if a > b else b)(5, 7))  # условие в lambda может быть написано в виде тернарного выражения

# рассмотрим еще 2 встроенные функции ЦИКЛА

# map(function, iterables), filter(function, iterables)  - принимает 2 параметра
# MAP - ЭТО ФУНКЦИЯ ЦИКЛА


# def mult(t):  # рассмотрим на примере обычной функции
#     return t * 2
#
#
# lst = [2, 8, 12, -5, -10]
#
# print(list(map(mult, lst)))  # map проходится в цикле по итерируемым обьектам списка lst и применяет функцию mult
# print(tuple(map(mult, lst)))  # то же самое только возвращает  в кортеж

# print(list(map(lambda t: t * 2, [2, 8, 12, -5, -10])))   # применение функции map с использованием lambda выражения
#
# st = ["a", "b", "c", "d"]
# num = [1, 2, 3, 4]

# print(dict(map(lambda a, b: (a, b), st, num)))    # словарь
# print(list(map(lambda a, b: (a, b), st, num)))    # список
# print(tuple(map(lambda a, b: (a, b), st, num)))   # кортеж
# print(set(map(lambda a, b: (a, b), st, num)))   # множество
#
# l1 = [1, 2, 3]
# l2 = [4, 5, 6]
# print(dict(map(lambda x, y: (x, y), l1, l2)))
# print(list(map(lambda a, b: a + b, l1, l2)))

# lst = [input("-> ") for i in range(5)]
# print(lst)
# lst = (list(map(int, lst)))
# print(lst)

# t = ('abcd', 'abc', 'cdefg', 'def', 'ghi')
#
# print(tuple(filter(lambda i: len(i) == 3, t)))


# lst = [66, 90, 68, 59, 76, 60, 88, 74, 81, 65]
# print(list(filter(lambda s: s > 75, lst)))

# from random import randint
# lst = [randint(1, 40) for i in range(10)]
# print(lst)
# print(list(filter(lambda a: (a >= 10) and a <= 20, lst)))
# print(list(filter(lambda a: 10 <= a <= 20, lst)))

# nums = [45, 55, 60, 37, 100, 105, 220]
# print(list(filter(lambda s: s % 15 == 0, nums)))
# print(list(filter(lambda s: not s % 15, nums)))

# совмещение map и filter

# print(list(map(lambda x: x ** 2, filter(lambda x: x % 2, range(10)))))  # 1 вариант решения
#
# print([x ** 2 for x in range(10) if x % 2])   # 2 вариант решения


# урок 06.03  - Декораторы

# def hello():
#     return "Hello, I am func 'hello'"
#
#
# def super_func(func):
#     print("Hello, I am func 'super_func'")
#     print(func())
#
#
# super_func(hello)


# def hello():
#     return "Hello, I am func 'hello'"
#
#
# test = hello
# print(test())

# def my_decorator(func):
#     def func_wrapper():
#         print("Код до функции")
#         func()
#         print("Код после функции")
#
#     return func_wrapper
#
#
# def func_test():
#     print("Hello, I am func 'func_test'")
#
#
# test = my_decorator(func_test)
# test()


# def my_decorator(func):                 # декорирующая функция
#
#     def func_wrapper():
#         print("Код до функции")
#         func()
#         print("Код после функции")
#
#     return func_wrapper
#
# @my_decorator                            # декоратор
# def func_test():                         # декорируемая функция
#
#     print("Hello, I am func 'func_test'")
#
#
# func_test()

# def bold(fn):
#     def wrap():
#         return "<b>" + fn() + "</b>"
#
#     return wrap
#
#
# def italic(func):
#     def wrap():
#         return "<i>" + func() + "</i>"
#
#     return wrap
#
#
# @italic
# @bold
# def hello():
#     return "text"


# print(hello())

# def cnt(fn):
#     count = 0
#
#     def wrap():
#         nonlocal count
#         count += 1
#         fn()
#         print("Вызов функции:", count)
#
#     return wrap
#
#
# @cnt
# def hello():
#     print("Hello")
#
#
# hello()
# hello()
# hello()

# def outer(fn):
#     def inner(args1, args2):
#         print("Данные:", args1, args2)
#         fn(args1, args2)
#
#     return inner
#
#
# @outer
# def print_full_name(first, last):
#     print("Меня зовут", first, last)
#
#
# print_full_name("Ирина", "Ветрова")


# def outer(fn):
#     def inner(*args, **kwargs):
#         print("args:", args)
#         print("kwargs:", kwargs)
#         fn(*args, **kwargs)
#
#     return inner
#
#
# @outer
# def print_data(a, b, c, study="Python"):
#     print(a, b, c, "изучают", study, end="\n\n")
#
#
# print_data("Борис", "Елизавета", "Светлана", study="JavaScript")
# print_data("Владимир", "Екатерина", "Виктор")

# def decor(args1, args2):
#     def args_dec(fn):
#         def wrap(x, y):
#             print(args1, x, args2, y, "=", end=" ")
#             fn(x, y)
#
#         return wrap
#     return args_dec
#
#
# @decor("Сумма:", "+")
# def summa(a, b):
#     print(a + b)
# #
#
# @decor("Разность:", "-")
# def sub(a, b):
#     print(a - b)
#
#
# summa(5, 2)
# sub(15, 12)


# def multiply(arg):
#     def my_decorator(func):
#         def wrap(*args, **kwargs):
#             return arg * func(*args, **kwargs)
#
#         return wrap
#     return my_decorator
#
#
# @multiply(3)
# def return_num(num):
#     return num
#
#
# print("Результат:", return_num(5))


# Строки

# print(bin(18))  # 0b10010 - двоичная система счисления
# print(oct(18))  # 0o22 - восьмеричная система счисления
# print(hex(18))  # 0x12 - шестнадцатеричная система счисления
#
# print(0b10010)
# print(0o22)
# print(0x12 + 0b10010 + 4)

# Unicode

# q = 'Pyt'
# w = "hon"
# e = q + w
# print(e)
# print(e * 3)
# print("y" in e)
# print("a" in e)
# print(e[-1])
# print(e[1:3])

# def chang_char_to_str(s, old, new):
#     s2 = ""
#
#     i = 0
#     while i < len(s):
#         if s[i] == old:
#             s2 += new
#         else:
#             s2 += s[i]
#         i += 1
#
#     return s2
#
#
# str1 = "Я изучаю Nython. Мне нравится Nython. Nython очень интересный язык программирования"
# str2 = chang_char_to_str(str1, "N", "P")
# print(str1)
# print(str2)

# print(u"Привет")
# print("Привет")

# print("C:\\file.txt\\")
# print(r"C:\file.txt\\"[:-1])
# print(r"C:\file.txt" + "\\")

#  урок 11.03

# print(b"a1b2c2")


# name = "Дмитрий"
# age = 25
# print("Меня зовут ", name, ". Мне ", age, " лет.", sep="")
# print("Меня зовут " + name + ". Мне " + str(age) + " лет.")
# print(f"Меня зовут {name}. Мне {age} лет.")


# x = 10
# y = 5
# print(f"{x=}, {y=}")
# print("x=", x, ", y=", y, sep="")
#
# print(f"{x} x {y} / 7 = {round(x + y / 7, 4)}")
# print(f"{x} x {y} / 7 = {x * y / 7:.2f}")

# num = 74
# print(f"{{{{{num}}}}}")

# dir_name = "folder"
# file_name = "file.txt"
# print(fr"home\{dir_name}\{file_name}")
# print("home\\" + dir_name + "\\" + file_name)


# st = ("Однострочный "
#       "текст")
# print(st)
#
# s = """Многострочный
# текст
# """
# print(s)
#
# s1 = '''Многострочный
# текст
# '''
# print(s1)
#
#
# """Многострочный комментарий
# текст
# """
#
# "Однострочный комментарий"


# def square(n):
#     """Принимает число n, возвращает квадрат числа n"""
#     res = n ** 2
#
#     return res
#
#
# print(square(5))
# print(square.__doc__)
# print(len.__doc__)
# # print(min.__doc__)
# # print(max.__doc__)
# # print(sum.__doc__)


# from math import pi
#
#
# def cylinder(r, h):
#     """
#     Вычисляет площадь цилиндра.
#
#     Вычисляет площадь цилиндра на основании заданной высоты и радиуса основания
#     :param r: положительное число, радиус основания цилиндра
#     :param h: положительное число, высота цилиндра
#     :return: положительное число, площадь цилиндра
#     """
#     return 2 * pi * r * (r + h)
#
#
# print(cylinder(2, 4))
# print(cylinder.__doc__)


# print(ord('a'))
# print(ord('#'))
# print(ord('п'))

# while True:
#     n = input("-> ")
#     if n != "-1":
#         print(ord(n))
#     else:
#         break

# st = "Test string for me "
# arr = [ord(x) for x in st]
# print("ASCII коды:", arr)
# arr = [int(sum(arr) / len(arr))] + arr
# print("Среднее арифметическое:", arr)
# arr += [ord(x) for x in input("-> ")[:3] if ord(x) not in arr]
# print(arr)
# print(arr.count(arr[-1]) - 1)
# arr.sort(reverse=True)
# print(arr)

# print(chr(97))
# print(chr(35))
# print(chr(8364))
# print(chr(1057))

# a = 97
# b = 122
#
# if a > b:
#     for i in range(b, a + 1):
#         print(chr(i), end=" ")
# else:
#     for i in range(a, b + 1):
#         print(chr(i), end=" ")


# from random import randint
#
# SHORTEST = 6
# LONGEST = 16
# MIN_ASCII = 33
# MAX_ASCII = 126
#
#
# def random_password():
#     rand_len = randint(SHORTEST, LONGEST)
#     result = ""
#     for i in range(rand_len):
#         result += chr(randint(MIN_ASCII, MAX_ASCII))
#     return result
#
#
# print("Случайный пароль:", random_password())

# print(dir(str))

# s = "hello, WORLD! I am learning Python."
# print(s.capitalize())  # Hello, world! i am learning python.
# print(s.lower())  # hello, world! i am learning python.
# print(s.upper())  # HELLO, WORLD! I AM LEARNING PYTHON.

# print(s.count("h", 1, -1))
# print(s.lower().count("i"))

# print(s.find("Python"))
# print(s.find("h", 1, -4))  # при ненахождении элемента выбрасывает значение -1
# print(s.find("h"))           # поиск элемента с левой стороны
# print(s.rfind("h"))          # поиск элемента с правой стороны

# print(s.index("h", 1, -4))     # при ненахождении элемента выбрасывает исключение
# print(s.rindex("h"))             # поиск элемента с правой стороны при ненахождении элемента выбрасывает исключение

# st = "один два"
# st = input("-> ")
# one = st[:st.find(" ")]  # st[:4] т.е. срез от начала до пробельного символа
# two = st[st.find(" ")+1:]  # st[4:] срез от 4 символа до конца
# res = two + " " + one
# print(res)

# st = "один два"
# print(st[st.find(" ") + 1:] + " " + st[:st.find(" ")])

# s = "hello, WORLD! I am learning Python."
# print(s.startswith("hello"))
# print(s.startswith("I am", 14))
# print(s.find("I am"))
#
# print(s.endswith("Python."))


# print("abc123".isalnum())  # состоит ли строка из букв и цифр
# print("abc!123".isalnum())
# print("abc".isalnum())
# print("123№".isalnum())

# print("ABCabcП".isalpha())  # состоит ли строка из букв
# print("ABC%abc".isalpha())

# print("123".isdigit())  # # состоит ли строка из цифр
# print("123@".isdigit())


# print('aab'.islower())  # находятся ли в строке буквы в нижнем регистре, допускается наличие других символов
# print('123aab!№;'.islower())
#
# print("ABC".isupper())  # находятся ли в строке буквы в верхнем регистре, допускается наличие других символов
# print("123AвBC!!".isupper())

# print("py".center(10))
# print("py".center(10, "-"))
# print("py".center(1))


# print("    py".lstrip())
# print("py    ".rstrip())
# print("    py    ".strip())
#
# print("https://www.python.org".lstrip("/:htps"))
# print("https://www.python.org.www".lstrip("/:htps").rstrip(".w"))
# print("https://www.python.org.www".strip("/:htps.w"))

#
# str1 = "Я изучаю Nython. Мне нравится Nython. Nython очень интересный язык программирования"
# print(str1.replace("N", "P", 1))


# s = "-"
# seq = ("a", "b", "c")
# print(s.join(seq))
#
# print("..".join(['1', '99']))
#
# print(":".join("Hello"))


# s = "Hello"
# print(s[::-1])

# урок 13.03


# # s = "I am learning Python. hello, WORLD!"
# s = input("Введите строку: ")
# # print(s.rfind('h') + 1)
# a = s[:s.find('h')]  # s[:17]
# b = s[s.find('h'):s.rfind('h') + 1]  # s[17:23]  # получается срез - hon. h
# c = s[s.rfind('h') + 1:]  # s[23:]
# print(a + b[::-1] + c)    # реверс строки в противоположную сторону


# print("Строка разделенная пробелами".split())
# print("www.python.org.ru".split(".", 1))


# s = input("Введите ФИО: ").split()
# print(s)
# print(f"{s[0]} {s[1][0]}.{s[2][0]}.")


# s = input("Введите числа через пробел: ").split()
# print(s)
# num = list(map(int, s))
# print(num)
# print(sum(num))


# Регулярные выражения

# import re

# s = "Я ищу совпадения в 2025 году. И я их найду в 2 счёта. 6789. [Hel_lo] Wor-ld"
# print(dir(re))
# reg = "\\."
# reg = r"\."                             # row - строка для регулярных выражений
# print(re.findall(reg, s))               # возвращает список совпадений с шаблоном
# print(re.search(reg, s))                # возвращает только первое совпадение с шаблоном
# print(re.search(reg, s).span())         # показывает на каких индексах нашлось совпадение
# print(re.search(reg, s).start())        # показывает начальный индекс совпадения
# print(re.search(reg, s).end())          # конечный индекс совпадения
# print(re.search(reg, s).group())        # выводит само совпадение
# print(re.split(reg, s))                 # возвращает список, который разбит по заданному шаблону
# print(re.sub(reg, "!", s))              # поиск и замена

# reg = r"[205]"
# reg = r"[0-9]"
# reg = r"[12][0-9][0-9][0-9]"            # находит по первым цифрам, это либо 1 либо 2 (1998 или 2021)
# reg = r"[а-яА-Я]"                       # находит все буквы русского алфавита в диапазоне
# reg = r"[А-яЁё.\]\[-]"
# reg = r"[A-Za-z]"
# reg = r"[^0-9]"                         # находит цифры которые противоположны от 0 до 9
# print(re.findall(reg, s))

# st = "Час в 24-часовом формате от 00 до 23. 2021-06-15T10:59. Минуты, в диапазоне от 00 до 59. 2021-06-15T01:09."
# reg = "[0-2][0-9]:[0-5][0-9]"
# print(re.findall(reg, st))
# reg = r"\d"               # [0-9]
# reg = r"\D"               # [^0-9] ищет все что не цифры
# reg = r"\s"               # [ ] находит только пробелы
# reg = r"\S"               # [^ ] находит все что не пробел
# reg = r"\w"               # [А-яA-Za-z0-9_] ищет буквы, цифры и символ подчеркивания
# reg = r"\W"               # [^А-яA-Za-z0-9_] ищет все что не казано в скобках
# reg = r"\AЯ ищу"          # ищет элементы с начала строки
# reg = r"Wor-ld\Z"         # ищет элементы с конца строки
# reg = r"\Bния"
# reg = r"\w?"              # выводит все слово или цифру, пока не встретит пробел
# reg = r"20*"                # обязательная цифра 2, а 0 может быть, может не быть
# print(re.findall(reg, s))

# Кол-во повторений
# + - от 1 до бесконечности
# * - от 0 до бесконечности
# ? - от 0 до 1 повторения

# d = "Цифры: 7, +17, --42, 0013, 0.3"
# reg = r"[+-]?[\d.]+"
# print(re.findall(reg, d))

# st = "05-03-1987 # Дата рождения"
#
# print("Дата рождения:", re.sub(r"\s#.+", "", st))
# print(re.sub("-", ".", st))
#
# print("Дата рождения:", re.sub(r"\s#.+", "", re.sub("-", ".", st)))           # два метода вложены друг в друга

# st = "author=Пушкин А.С.; title  = Евгений Онегин; price =200; year= 1831"
# reg = r"\w+\s*=\s*\w+\s*\w*\.?\w*\.?"
# reg = r"\w+\s*=\s*\w+[\s\w.]*"
# reg = r"\w+\s*=[^;]+"
# print(re.findall(reg, st))
# print(re.split(r";\s", st))


# st = "12 сентября 2025 год 456 789456123"
# reg = r"\d{4}"                                      # указываем в скобках что ищем 4 цифры
# reg = r"\d{2,4}"                                    # указываем что ищем вариации цифр от 2 до 4
# reg = r"\d{,4}"                                     # указывает от 0 до 4 повторений
# reg = r"\d{2,}"                                     # указывает от 4 и более повторений
# print(re.findall(reg, st))


# st = "+7 499 456-45-78, +74994564578, +7 (499) 456 45 78, 74994564578"
# reg = r"\+?7\d{10}"
# print(re.findall(reg, st))

# reg = r"^\w+\s\w+"
# reg = r"\w+\s\w+$"
# print(re.findall(reg, s))

# def validate_login(login):
#     return re.findall(r"^[a-zA-Z0-9_-]{3,16}$", login)
#
#
# print(validate_login("Python_master"))
# print(validate_login("Pyt"))

# урок 18.03 - флаги

import re


# from tkinter.font import names

# print(re.findall(r"\w+", "12 + й"))
# print(re.findall(r"\w+", "12 + й", flags=re.ASCII))
#
# text = "hello world"
# print(re.findall(r"\w\+", text))
# print(re.findall(r"\w\+", text, re.DEBUG))

# text = "helLo worLd"
# print(re.findall(r"l", text, re.IGNORECASE))


# text = """
# one
# two
# """

# print(re.findall(r"one.\w+", text))
# print(re.findall(r"one.\w+", text, re.DOTALL))

# print(re.findall(r"one$", text))
# print(re.findall(r"one$", text, re.MULTILINE))

# print(re.findall("""
# [a-z.-]+  # part 1
# @         # @
# [a-z.]+   # part 2
# """, "test@mail.ru", re.VERBOSE))

# text = """Python,
# python,
# PYTHON
# """
# reg = "(?mi)^python"
# print(re.findall(reg, text))


# text = "<body>Пример жадного соответствия регулярных выражений</body>"
# print(re.findall('<.*?>', text))        # здесь знак ? -  ленивое совпадение, т.е. без внутреннего содержимого
#
#
# st = "12 сентября 2025 год 456 789456123"
# # reg = r"\d{4}"
# # reg = r"\d{2,4}?"
# # reg = r"\d{,4}?"
# reg = r"\d{4,}?"
# print(re.findall(reg, st))

# *?, +?, ??                           # может так выводить ленивое совпадение
# {m,n}?, {,n}?, {m,}?

# s = "Петр, Ольга и Виталий отлично учатся!"
# reg = "Петр|Ольга|Виталий|Василий|Виталий"
# print(re.findall(reg, s))

# s = "int = 4, float = 4.0f, double = 8.0, int"
# # reg = r"int\s*=\s*\d[\w.]*|float\s*=\s*\d[\w.]*"  # 1 вариант
# reg = r"(?:int|float)\s*=\s*\d[\w.]*"               # 2 вариант с круглыми сохраняющими скобками
# print(re.findall(reg, s))

# s = "Word2016, PS6, AI5"
# reg = r"([a-z]+)(\d+)"                                 # вариант использования с круглыми скобками
# print(re.findall(reg, s, re.IGNORECASE))
# print(re.search(reg, s, re.IGNORECASE))

# s = "5 + 7*2 - 4"
# reg = r"\s*[+*-]\s*"
# print(re.split(reg, s))                          # split  разбивает по символу разделителю строку на список
# #
# s = "5 + 7*2 - 4"
# reg = r"\s*([+*-])\s*"                          # здесь со скобками split работает по другому
# print(re.split(reg, s))


# s = "28-01-1979"  # 1900-2099
# reg = r"(0[1-9]|[12][0-9]|3[01])-(0[1-9]|1[0-2])-(19[0-9][0-9]|20[0-9][0-9])"
# print(re.findall(reg, s))
# # print(re.search(reg, s))
# # print(re.search(reg, s).group())


# s = "Word2016, PS6, AI5"
# reg = r"([a-z]+)(\d+)"
# print(re.findall(reg, s, re.IGNORECASE))
# print(re.search(reg, s, re.IGNORECASE).group())
# m = re.search(reg, s, re.IGNORECASE)
# print(m[1])                            # вывел только совпадение с 1 круглой скобкой
# print(m[2])                            # вывел только совпадение с 2 круглой скобкой
# print(m[0])                            # все совпадение шаблона (полное совпадение)

# s = "Самолет прилетает 10/23/2025. Будем рады вас видеть после 10/24/2025."
# reg = r"(\d{2})/(\d{2})/(\d{4})"
# print(re.sub(reg, r"\2.\1.\3", s))      # через метод sub меняем местами данные  по номеру скобки

# s = "yandex.com and yandex.ru"
# reg = r"(([a-z0-9-]{2,}\.)+[a-z]{2,4})"
# print(re.sub(reg, r"http://\1", s))


# Рекурсия

# def elevator(n):  # 0
#     if n == 0:  # базовый случай
#         print("Вы в подвале")
#         return
#     # print("=>", n)
#     elevator(n - 1)  # стек 5 4 3 2 1
#     print(n, end=" ")
#
#
# n1 = int(input("На каком вы этаже: "))
# elevator(n1)


# def sum_list(lst):
#     res = 0
#     for i in lst:
#         res += i
#     return res

# def sum_list(lst):  # [9]
#     if len(lst) == 1:
#         print(lst, "=> lst[0]:", lst[0])
#         return lst[0]  # 9
#     else:
#         print(lst, "=> lst[0]:", lst[0])
#         return lst[0] + sum_list(lst[1:])  # 1 + 3 + 5 + 7
#
#
# print(sum_list([1, 3, 5, 7, 9]))  # 25


# def to_str(n, base):  # n = 15, base = 16
#     convert = "0123456789ABCDEF"
#     if n < base:
#         return convert[n]  # 'F'
#     else:
#         return to_str(n // base, base) + convert[n % base]  # 'F' + 'E'
#
#
# print(to_str(254, 16))

# names = ['Adam', ["Bob", ["Chet", "Cat"], "Bard", "Bert"], 'Alex', ["Bea", "Bill"], "Ann"]
# print(names)
# print(len(names))
# print(names[0])
# print(isinstance(names[0], list))
# print(names[1])
# print(isinstance(names[1], list))
# print(names[1][1])
# print(isinstance(names[1][1], list))
# print(names[1][1][0])
# print(isinstance(names[1][1][0], list))


# names = ['Adam', ["Bob", ["Chet", "Cat"], "Bard", "Bert"], 'Alex', ["Bea", "Bill"], "Ann"]
#
#
# def count_items(item_list):  # ['Adam', ["Bob", ["Chet", "Cat"], "Bard", "Bert"], 'Alex', ["Bea", "Bill"], "Ann"]
#     count = 0  # 10
#     for item in item_list:  #
#         if isinstance(item, list):
#             count += count_items(item)
#         else:
#             count += 1
#     return count
#
#
# print(count_items(names))

# print("Текст в локальном и глобальном репозитории")
# print("Новый репозиторий")

# print("Код на новом устройстве")


# Файлы

# f = open(r"text.txt")
# f = open(r"C:\Users\user\Desktop\Pithon\text.txt")            # r - подавляет экранирование элементов
# print(*f)
# print(f)
# print(f.mode)                                                 # режим доступа к файлу (чтение)
# print(f.name)                                                 # просмотреть имя файла
# print(f.encoding)                                             # название кодировки
#
# f.close()                                                     # закрывает файл
# print(f.closed)                                               # показывает True если файл закрыт, False если открыт


# f = open(r"text.txt")
# print(f.read(3))
# print(f.read())
# f.close()

# f = open("xyz.txt", "w")                                        # запись и чтение нового файла
# f.write("This is line1.\nThis is line2.\nThis is line3.\n")     # функция для записи данных в файл
# f.close()

# f = open("xyz.txt")
# print(f.read())            # метод позволяет считать файл полностью все символы
# print(f.readline())          # метод позволяет считать 1 строку
# print(f.readline(8))       # метод позволяет считать 8 символов
# print(f.readline())
# f.close()

# print(f.readlines(15))         # метод позволяет считать данные в виде списка строк

# f = open("xyz.txt")              # вывод этих же строк в цикле
# for line in f:
#     print(line)
# f.close()

# lines = ["This is line1.\n", "This is line2.\n", "This is line3.\n"]
# f = open("lines.txt", "w")
# f.writelines(lines)                 # метод для записи списка строк в файл
# f.close()

# lines = [str(i) for i in range(10, 1000, 15)]      # в чистом виде файлы работают только строкой
# print(lines)
#
# f = open("lines.txt", "w")
# for index in lines:
#     f.write(index + "\t")
# f.close()

# file = "text2.txt"
# f = open(file, "w", encoding="utf-8")
# f.write("Замена строки в тестовом файле;\nизменить строку в списке\nзаписать список в файл\n")
# f.close()
#
# f = open(file, "r", encoding="utf-8")
# read_line = f.readlines()    # считывает все строки из текст. файла и возвр. каждую строку как строковый элем. в списке.
# print(read_line)
# read_line[1] = "Hello world!\n"
# print(read_line)
# f.close()
#
# f = open(file, "w", encoding="utf-8")
# f.writelines(read_line)                  # метод для записи списка строк в файл
# f.close()

# f = open("text.txt", "r")
# print(f.read(3))                      # указываем что необходимо считать 3 символа
# print(f.tell())                       # возвращает текущую позицию условного курсора в файле
#
# print(f.seek(1))                     # перемещает условный курсор в заданную позицию
# print(f.read())                      # считываем данные с 1 позиции
# print(f.tell())
# f.close()


# f = open("text.txt", "a")            # запись (если файл существует, то данные добавляются в конец файла)
# # f = open("text.txt", "w")              # запись (если файл существует, он будет очищен, если нет - создан)
# print(f.write("I am learning Python"))     # покажет количество символов которые мы записали
# f.close()

# with open("text.txt", "w") as f:    # контекстный менеджер with закрывает файл автоматически если не будет табуляции
#     print(f.write("0123456789"))
# print(f.closed)

# lst = [4.5, 2.8, 3.9, 0.3, 4.33]
#
#
# def get_line(lt):
#     lt = list(map(str, lt))      # в цикле к каждому элементу применим строковое значение
#     return " ".join(lt)          # список строковых значений преобразуем в строку через пробел
#
#
# with open("res.txt", "w") as f:
#     f.write(get_line(lst))     # вызываем функцию и потом полученную строку запишем в файл f
# print("Конец программы")

# так же мы можем эти все данные считать и найти сумму данных вещественных чисел
# with open("res.txt") as f:
#     nums = f.read()
#
# print(nums)
# print(list(map(float, nums.split())))  # чтобы просто посмотреть в print список элементов ф-ция list обязателено
# print(sum(map(float, nums.split())))  # в цикле map проходим по каждому элем. и преобразовать к типу данных float

# задача

# with open("res2.txt", "w") as f:
#     f.write("Файл — именованная область данных на носителе информации, используемая как базовый объект  "
#             "с данными в операционных системах.")  # взаимодействия
#
#
# def longest_words(file):
#     with open(file, "r") as text:
#         w = text.read().split()     # методом split строку разбиваем на список по символу разделителю по пробелу
#         max_lenght = len(max(w, key=len))
#         res = [word for word in w if len(word) == max_lenght]
#         if len(res) == 1:
#             return res[0]
#         return res
#
#
# print(longest_words("res2.txt"))


# text = "Строка №1\nСтрока №2\nСтрока №3\nСтрока №4\nСтрока №5\nСтрока №6\nСтрока №7\nСтрока №8\nСтрока №9\n
# Строка №10\n"
# with open("one.txt", "w", encoding="utf-8") as f:
#     f.write(text)
#
# with open("one.txt", "r", encoding="utf-8") as fr, open("two.txt", "w", encoding="utf-8") as fw:
#     for line in fr:
#         line = line.replace("Строка", "Линия -")
#         fw.write(line)
#
# import os
#
# print(os.getcwd())                                  # путь к текущей директории
#
# print(os.listdir())                                 # возвращает список директорий и файлов
# print(os.listdir(".."))
# print(os.listdir(".venv"))

# os.mkdir("folder")      # создать папку
# os.rmdir("folder.txt")  # удалить папку

# os.makedirs("nested1/nested2/nested3")                # создает директорию с промежуточными папками
#
# os.remove("xyz.txt")                                  # удалить файл
#
# os.rename("two.txt", "www.txt")                      # переименовали файл
#
# os.rename("www.txt", "folder/www.txt")               # переместили файл в заданную папку

# os.renames("text4.txt", "test/text4.txt")            # переместили файл, создавая промежуточные папки


# занятие 01.04

# import os

# print(os.walk("nested1"))                                      # генерирует имена файлов в дереве каталогов
# for root, dirs, files in os.walk("nested1", topdown=False):  # обход дерева снизу вверх, True - сверху вниз
#     print("Root:", root)
#     print("\tdirs:", dirs)
#     print("\tFiles:", files)

# import os.path                        # модуль работает непосредственно с путями файлов и папок
#
# print(os.path.split(r"E:\Python\Python416\nested1\nested2\nested3\text3.txt"))  # разбивает путь на кортэж и показывает посл. файл
#
# print(os.path.join("nested1", r"E:\Python416", "nested2", "nested3", "text5.txt")) # модуль, который предоставляет инструменты для работы с файловыми путями


# import os
#
# dirs = [r"Work\F1", r"Work\F2\F21"]
# for d in dirs:
#     os.makedirs(d)                         # создаем директорию с промежуточными папками
#
# files = {
#     "Work": ["w.txt"],
#     r"Work\F1": ["f11.txt", "f12.txt", "f13.txt"],
#     r"Work\F2\F21": ["f211.txt", "f212.txt"]
# }
#
# for d, files in files.items():                         # возвращаем ключи и значения в цикле
#     for file in files:
#         file_path = os.path.join(d, file)              #  методом join обьединяем пути и значения
#         # print(file_path)
#         open(file_path, "w").close()
#
#
# file_with_text = [r"Work\w.txt", r"Work\F1\f12.txt", r"Work\F2\F21\f211.txt", r"Work\F2\F21\f212.txt"]
#
# for file in file_with_text:
#     with open(file, "w", encoding="utf-8") as f:
#         f.write(f"Такой-то текст в файле {file}")
#
#
# def print_tree(root, topdown):
#     print(f"Обход {root} {'сверху вниз' if topdown else 'снизу вверх'}")
#     for root1, directory, file_name in os.walk(root, topdown):
#         print(root1)
#         print(directory)
#         print(file_name)
#     print("-" * 50)
#
#
# print_tree("Work", False)
# print_tree("Work", True)
#
# import os
# import time

# print(os.path.exists(r"nested1\nested2\nested3\text3.txt"))   # метод проверяет есть ли такой путь или нет (True, False)
# print(os.path.isfile(r"nested1\nested2\nested3\text5.txt"))    # метод позволяет проверить это файл или папка
# print(os.path.isdir(r"nested1\nested2\nested3"))      # метод позволяет проверять является ли последний элем. папкой
#

# file = "main.py"
#
# print(os.path.getsize(file))  # метод показывает размер файла в байтах
# print(os.path.getatime(file))  # возвращает время последнего доступа к файлу
# print(os.path.getmtime(file))  # возвращает время последнего изменения файла
# print(os.path.getctime(file))  # возвращает время создания файла
#
# kb = os.path.getsize(file)
# a = os.path.getatime(file)
# m = os.path.getmtime(file)
# c = os.path.getctime(file)
#
# print(time.strftime("%d.%m.%Y, %H:%M:%S", time.localtime(a)))
# print(time.strftime("%d.%m.%Y, %H:%M:%S", time.localtime(m)))
# print(time.strftime("%d.%m.%Y, %H:%M:%S", time.localtime(c)))
# print(kb // 1024)

# ООП


# class Point:
#     x = 1             # это свойства класса. К ним обращаются через экземпляр класса
#     y = 2             # это свойства класса. К ним обращаются через экземпляр класса
#
#
#
# p1 = Point()            # это имя класса (экземпляр класса)
# p1.x = 10
# p1.y = 20
# # Point.x = 100         # перезаписываем значение х в классе Point
# print(p1.x, p1.y)
# print(p1.__dict__)
#

# p2 = Point()
# print(p2.x, p2.y)
# p2.x = 5
# print(p2.__dict__)     # служебный метод показывает словарь из свойств которые принадлежат данному экземпляру p.2
#
# print(Point.__dict__)  # показывает словарь из свойств которые принадлежат данному классу Point


# class Point:
#     x = 1
#     y = 2

# def set_coord(self):  # Это метод класса. Пишется с одним пробелом
#     print(self.__dict__)


# p1 = Point()
# p1.x = 5
# p1.y = 10
# p1.set_coord()         # к методу обращаемся через имя экземпляра класса. В self приходит имя экземпляра класса p1
# Point.set_coord(p1)

# class Point:
#     """"Класс для предоставления координат точек на плоскости"""
#     x = 1
#     y = 2
#
#     def set_coord(self, x1, y1):
#         self.x = x1                   # self это как независимый элемент в который попадет ссылка на экземпляр класса
#         self.y = y1                   # в self приходит сколько угодно экземпляров класса


# p1 = Point()
# p1.x = 5
# p1.y = 10
# p1.set_coord(5,10)  # к методу обращаемся через имя экземпляра класса. В self приходит имя экземпляра класса p1
# print(p1.__dict__)
# Point.set_coord(p1,20,30)
# print(p1.__dict__)

# p2 = Point()                     # экземпляр класса (обьект)
# p2.set_coord(100,200)
# print(p2.__dict__)                # магический метод (служебный)
# print(Point.__doc__)              # магический метод (служебный) выводит документацию у класса


# p1 = Point()                      # экземпляр класса (объект)
# p1.set_coord(5, 3)
# print(p1.__dict__)
# print(Point.__doc__)
# print(Point.__dict__)
# print(type(p1))
# print(type(5))
# p1.x = 5
# p1.y = 10
# p1.set_coord(5, 10)
# print(p1.__dict__)
# print(p1.x)
# # Point.set_coord(p1, 20, 30)
# # print(p1.__dict__)
# #
# p2 = Point()
# p2.set_coord(100, 200)
# print(p2.__dict__)
# print(p2.x)

# 03/04/2025

# class Human:
#     name = "name"
#     birthday = "00.00.0000"
#     phone = "00-00-00"
#     country = "country"
#     city = "city"
#     address = "street, house"
#
#     def print_info(self):
#         print(" Персональные данные ".center(40, "*")) # метод строк center делает графическое оформление
#         print(f"Имя: {self.name}\nДата рождения: {self.birthday}\n"
#               f"Номер телефона: {self.phone}\nСтрана: {self.country}\n"
#               f"Город: {self.city}\nДомашний адрес: {self.address}")
#         print("=" * 40)
#
#     def input_info(self, first_name, birthday, phone, country, city, address):
#         self.name = first_name
#         self.birthday = birthday
#         self.phone = phone
#         self.country = country
#         self.city = city
#         self.address = address
#
#     def set_name(self, name):  # этот метод устанавливаем новое имя (сэттэры) set - установить
#         self.name = name
#
#     def get_name(self):        # этот методом получаем имя (геттеры) get - получить
#         return self.name
#
#
# h1 = Human()                                # cначала обращаемся к имени экземпляра класса
# h1.print_info()                             # а после этого обращаемся к методу класса
# h1.input_info("Юля", "23.05.1986", "45-46-98", "Россия", "Москва", "Чистопрудный бульвар, 1A")
# h1.print_info()
# h1.set_name("Юлия")
# h1.print_info()
# print(h1.get_name())

# class Person:
#     skill = 10                        # статическое свойство (постоянное)
#     # name = ""
#     # surname = ""
#
#     def __init__(self, name, surname):  # магический метод (инициализация наших свойств)
#         self.name = name                # динамические свойства в классе (изменяются)
#         self.surname = surname
#         # print("Инициализатор для", self.name, self.surname)
#
#     def print_info(self):  # инициализатор
#         print("Данные сотрудника:", self.name, self.surname)
#
#     def __del__(self):  # магический метод для удаления экземпляра (разрывается ссылка) т.е. финализатор
#         print("Удаление экземпляра")
#
#
#     def add_skill(self, k):
#         self.skill = self.skill + k
#         print("Квалификация сотрудника:", self.skill, "\n")
#
#
# p1 = Person("Виктор", "Резник")
# p1.print_info()
# p1.add_skill(3)
#
# del p1                # разрывает ссылку между 2 экз. классов (p1 и p2)
# print()
#
# p2 = Person("Анна", "Долгих")
# p2.print_info()
# p2.add_skill(2)
#
# class Point:  # задача - нужно посчитать сколько создано всего экземпляров класса
#     count = 0
#
#     def __init__(self, x=0, y=0):
#         self.x = x
#         self.y = y
#         Point.count += 1     # к статическим переменнным лучше обращаться через имя класса (Point), т.к. в каких то                                                   # моментах он может брать значение одного экземпляра класса и все
#
#
# p1 = Point()
# p2 = Point()
# p3 = Point()
# print(Point.count)  # получаем доступ к статическому свойству класса через имя класса
# print(p1.count)     # а также через имя экземпляра класса


# class Robot:
#     k = 0
#
#     def __init__(self, name):
#         self.name = name
#         print("Инициализация робота:", self.name)
#         Robot.k += 1
#
#     def __del__(self):
#         print(self.name, "выключается!")
#         Robot.k -= 1
#
#         if Robot.k == 0:
#             print(self.name, "был последним")
#         else:
#             print("Работающих роботов осталось:", Robot.k)
#
#     def say_hi(self):
#         print("Приветствую! Меня зовут:", self.name)
#
#
# droid1 = Robot("R2-D2")
# droid1.say_hi()
# print("Численность роботов:", Robot.k)
#
# droid2 = Robot("C-3PO")
# droid2.say_hi()
# print("Численность роботов:", Robot.k)
#
# droid3 = Robot("PC-3O")
# droid3.say_hi()
# print("Численность роботов:", Robot.k)
#
# print("\nЗдесь роботы могут проделать какую-то работу\n")
# print("Роботы закончили свою работу. Давайте их выключим.")
#
# del droid1
# del droid2
# del droid3
#
# print("Численность роботов:", Robot.k)


class Point:

    def __init__(self, x, y):
        self.__x = self.__y = 0
        if Point.__check_value(x) and Point.__check_value(y):
            self.__x = x
            self.__y = y

    def __check_value(s):
        if isinstance(s, int) or isinstance(s, float):
            return True
        return False

    def set_coord(self, x, y):
        if Point.__check_value(x) and Point.__check_value(y):
            self.__x = x
            self.__y = y
        else:
            print("Координаты должны быть числами")

    def set_coord_x(self, x):
        if Point.__check_value(x):
            self.__x = x
        else:
            print("Координаты должны быть числами")

    def set_coord_y(self, y):
        if Point.__check_value(y):
            self.__y = y
        else:
            print("Координаты должны быть числами")

    def get_coord(self):
        return self.__x, self.__y

    def get_coord_x(self):
        return self.__x

    def get_coord_y(self):
        return self.__y


p1 = Point(5, "10")
# print(p1.__dict__)
# p1.z = 20
# print(p1.__x, p1.__y)
# p1.__x = 50
# p1.__y = "abc"
p1.set_coord(5.2, 100)
print(p1.get_coord())
p1.set_coord_x(10)
p1.set_coord_y(50)

# p1._Point__x = "abc"
# print(p1._Point__x)
# print(p1.__dict__)
