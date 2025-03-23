# a = 1
# b = 2
# print(a, b)
#
# a, b = b, a
# print(a, b)
# from operator import index
#
# import builtins

# num = 97531
# a = num % 10
# print(a)
# num = num // 10
# b = num % 10
# print(b)
# num = num // 10
# c = num % 10
# print(c)
# num = num // 10
# d = num % 10
# print(d)
# num = num // 10
# e = num % 10
# print(e)
# rez_1 = a * b * c * d * e
# print(rez_1)
# rez_2 = (a + b + c + d + e)/5
# print(rez_2)

# n = int(input("Введите количество копеек от 1 до 99: "))
# a = n % 10
# if 11 <= n <= 14:
#     print("КОПЕЕК")
# elif 1 <= n <= 99:
#     if a == 1:
#         print("КОПЕЙКА")
#     elif  2 <= a <= 4 :
#         print("КОПЕЙКИ")
#     else:
#         print("КОПЕЕК")
# else:
#     print("Значения должны быть от 1 до 99")


# a = int(input("Введите количество символов: " ))
# c = input("Введите тип символа: ")
# b = int(input("Введите ориентацию линии: (0 - горизонтальная; 1 - вертикальная): "))
# i = 0
#
# while i < a:
#     if b == 1:
#         print(c)
#     else:
#         print(c, end=" ")
#     i += 1

# for i in a:
#     if i < 0:
#         s += i
#
# print("Сумма отрицательных элементов: ", s)


# a = [int(input("->: ")) for i in range(int(input("Введите количество элементов: n = ")))]    # -3, 9, -5, -1
# s = 0
#
# for i in range(len(a)):
#     if a[i] < 0:
#         s += a[i]
# print("Сумма отрицательных элементов: ", s)


# a = [1, 3, 5, 6, 2, 4, 6, 1, 2, 7]
# b = []
#
# for i in range(len(a)):
#     if a.count(a[i]) == 1:
#         b.append(a[i])
#
# print(b)

# import random
# mas = [random.randint(0, 100) for i in range(10)]
# print(mas)
# mas1 = mas.copy()
# mas1.sort()
# print(mas1)
# min_ = mas1[0]
# print("Min: ", min_)
# ind = mas.index(min_)
# print("Index min: ", ind)
# del mas[:ind]
# print(mas)

#  Д.З. Найти длину окружности
# from math import *
#
# #print("Введите радиус окружности: r = ")
# r = float(input("Введите радиус окружности: "))
# l = 2 * pi * r
# print(round(l, 2))


# variant = int(input("Выберите фигуры: \n1 - треугольник\n2 - прямоугольник\n3 - круг\n:  "))
# s = None
# if variant == 1:
#     a = int(input("Введите сторону a = "))
#     b = int(input("Введите сторону b = "))
#     c = int(input("Введите сторону c = "))
#     p = (a + b + c) / 2
#     s = math.sqrt(p * (p - a) * (p - b) * (p - c))
#
# elif variant == 2:
#     a = int(input("Введите сторону a = "))
#     b = int(input("Введите сторону b = "))
#     s = a * b
#
# elif variant == 3:
#     radius = int(input("Введите радиус = "))
#     s = math.pi * radius ** 2
#
# else:
#     print("Такой фигуры не существует")
#
# print(round(s, 2))


# def res(a=20, b='-'):
#     return a * b
#
#
# print(res(10, "+"))
# print(res(5, "*"))
# print(res(15, "#"))
# print(res(7))
# print(res())


# from random import *
# list_1 = tuple(randint(0, 5) for i in range(10))
# list_2 = tuple(randint(-5, 0) for i in range(10))
# list_3 = list_1 + list_2
# print(list_1, type(list_1))
# print(list_2, type(list_2))
# print(list_3, type(list_3))
# print("0 =",list_3.count(0))

# a = 'Python'
# b = 'Programming language'
# c = set(a) - set(b)
# # a = set(a)
# # b = set(b)
# # a -= b                                # a.difference.update(b) - удаляет из множества а все элементы входящие в b
# print(c)
# for i in c:
#     print(i, end=" ")
#
# print()
# print(type(a))

# d = {
#     "John": {
#         "N": "3056",
#         "S": "8463",
#         "E": "8441",
#         "W": "2694"
#     },
#     "Tom": {
#         "N": "4832",
#         "S": "6786",
#         "E": "4737",
#         "W": "3612"
#     },
#     "Anne": {
#         "N": "5239",
#         "S": "4802",
#         "E": "5820",
#         "W": "1859"
#     },
#     "Fiona": {
#         "N": "3904",
#         "S": "3645",
#         "E": "8821",
#         "W": "2451"
#     }
# }
# for x, y in d.items():
#     print(x)
#     for i, j in y.items():
#         print("\t", i, ":", j, sep="")
#
# name = (input("Введите имя (или выход для завершения): "))
# region = (input("Ведите регион (N/S/E/W): "))
# print(d[name][region])
# new = int(input("Введите новое знечение: "))
# d[name][region] = new
# print(d[name])

# student = {}
# n = int(input("Введите количество студентов: "))
# s = 0
# for i in range (n):
#     name = input(str(i + 1) + "-й студент: ")
#     point = int(input("Балл: "))
#     student[name] = point
#     s += point
#
# averege = s / n
# print(student)
# print("Средний балл: ", round(averege), ". Студенты с баллом выше среднего: ", sep ="")
#
# for i, j in student.items():
#     if j > averege:
#         print(i)


# s = 0
#
# def outer(a, b, c):           #  переменная обьявлена как глобальная
#     def inner(i, j):
#         return i * j
#
#     global s
#     s = 2 * (inner(a, b) + inner(a, c) + inner(b, c))
#
#
# outer(2, 4, 6)
# print(s)
# outer(5, 8, 2)
# print(s)
# outer(1, 6, 8)
# print(s)
#
#
# def outer(a, b, c):         # переменная обьявлена как не локальная
#     s = 0
#
#     def inner(i, j):
#         nonlocal s
#         s += i * j
#
#     inner(a, b)
#     inner(a, c)
#     inner(b, c)
#     return 2 * s
#
#
# print(outer(2, 4, 6))
# print(outer(5, 8, 2))
# print(outer(1, 6, 8))

# from math import pi
#
# area = {
#     "Circle": lambda x: pi * (x * x),
#     "Rectangle": lambda x, y: (x * y),
#     "Trapezoid": lambda a, b, h: ((a + b) * h / 2)
# }
#
#
# print(area['Circle'](2))
# print(area["Rectangle"](10, 13))
# print(area["Trapezoid"](7, 5, 3))

# def averege_decorator(fn):
#     def wrap(*args, **kwargs):
#         n = fn(*args)
#         return n / len(args)
#
#     return wrap
#
#
# @averege_decorator
# def sum_numbers(*args):
#     return sum(args)
#
#
# print("Среднее арифметическое:", sum_numbers(2, 3, 3, 4,))

# s = "I am learning Python. hello, WORLD!"
# # print(s.rfind('h') + 1)
# a = s[:s.find('h')]
# b = s[s.find('h'):s.rfind('h') + 1]
# c = s[s.rfind('h')+ 1:]
# print(a + b[::-1] + c)

# import re
#
# st = "123456@i.ru, 123_456@ru.name.ru, login@i.ru, логин-1@i.ru, login.3@i.ru, login.3-67@i.ru, 1login@ru.name.ru"
# reg = r"\w[0-9a-zA-Z][a-zA-Z0-9_.+-]+@[a-zA-Z0-9]+\.[a-zA-Z0-9]"
# print(re.findall(reg, st))
# print(re.split(r".\s", st))


# def negativ_number(n):
#     if not n:
#         return 0
#     count = 0
#     if n[0] < 0:
#         count += 1
#     return count + negativ_number(n[1:])
#
#
# lst = [-2, 3, 8, -11, -4, 6]
# print(negativ_number(lst))

print("Текст на удаленном репозитории")
print("Текст на удаленном и глобальном репозитории")
