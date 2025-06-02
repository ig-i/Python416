# a = 1
# b = 2
# print(a, b)
#
# a, b = b, a
# print(a, b)
# from operator import index
#
# import builtins
from fileinput import filename
from linecache import clearcache
from tkinter.scrolledtext import example
from unittest.mock import PropertyMock

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

# print("Текст на удаленном репозитории")

# f = open("test3.txt", "w")
# f.write("Замена строки в текстовом файле;\nизменить строку в списке;\nзаписать список в файл;\n")
# f.close()
#
# f = open("test3.txt", "r")
# read_line = f.readlines()
# print(read_line)
# f.close()
#
# pos1 = int(input("pos1 = "))
# pos2 = int(input("pos2 = "))
#
# if 0 <= pos1 < len(read_line) and 0 <= pos2 < len(read_line):
#     read_line[pos1], read_line[pos2] = read_line[pos2],  read_line[pos1]
# else:
#     print("Такой строки нет")
#
# print(read_line)
#
# f = open("test3.txt", "w")
# f.writelines(read_line)
# f.close()

# import os
# from os.path import split
#
# #  в папке nested3 находятся: text.txt, tex2.txt, text3.txt
#
# first_file = input("Введите имя для файла папки nested3: ")
# file = r"C:\Users\user\Desktop\Python\Python416\nested1\nested2\nested3"
# for root, dirs, files in os.walk(file, topdown=False):
#     if first_file in files:
#         print(split(file))
#         print(f"{os.path.split(file)[1]}/{first_file}", "-", "last access time", os.path.getatime(file), "sec")
#     else:
#         print("Нет такого файла")


# class Mobile:
#
#     def __init__(self, name, year, manufacturer, engine_power, color, price):  # инициализатор
#         self.__name = name
#         self.__year = year
#         self.__manufacturer = manufacturer
#         self.__engine_power = engine_power
#         self.__price = price
#         self.__color = color
#
#     def __check_value(s):
#         if isinstance(s, int):
#             return True
#         return False
#
#     def __check_value2(s):
#         if isinstance(s, str):
#             return True
#         return False
#
#     def print_info(self):
#         print(" Данные автомобиля ".center(40, "*"))
#         print(f"Название модели: {self.__name}\nГод выпуска: {self.__year}\nПроизводитель: {self.__manufacturer}\n"
#               f"Мощность двигателя: {self.__engine_power}\nЦвет машины: {self.__color}\nЦена: {self.__price}")
#         print("=" * 40)
#
#     def set_name(self, name):
#         if Mobile.__check_value2(name):
#             self.__name = name
#         else:
#             print("Введите строковое значение")
#
#     def get_name(self):
#         return self.__name
#
#     def set_year(self, year):
#         if Mobile.__check_value(year):
#             self.__year = year
#         else:
#             print("Введите числовое значение")
#
#     def get_year(self):
#         return self.__year
#
#     def set_manufacturer(self, manufacturer):
#         if Mobile.__check_value2(manufacturer):
#             self.__manufacturer = manufacturer
#         else:
#             print("Ведите строковое значение")
#
#     def get_manufacturer(self):
#         return self.__manufacturer
#
#     def set_engine_power(self, engine_power):
#         if Mobile.__check_value2(engine_power):
#             self.__engine_power = engine_power
#         else:
#             print("Введите строковое значение")
#
#     def get_engine_power(self):
#         return self.__engine_power
#
#     def set_color(self, color):
#         if Mobile.__check_value2(color):
#             self.__color = color
#         else:
#             print("Введите строковое значение")
#
#     def get_color(self):
#         return self.__color
#
#     def set_price(self, price):
#         if Mobile.__check_value(price):
#             self.__price = price
#         else:
#             print("Введите числовое значение")
#
#     def get_price(self):
#         return self.__price
#
#
# m1 = Mobile("X7 M50i", "2021", "BMW", "530 л.с.", "white", "10790000")
# m1.print_info()
# m1.set_name(555)
# print(m1.get_name())
# m1.set_year("abc")
# print(m1.get_year())
# m1.set_manufacturer(1985)
# print(m1.get_manufacturer())
# m1.set_engine_power(123)
# print(m1.get_engine_power())
# m1.set_color(489)
# print(m1.get_color())
# m1.set_price("def")
# print(m1.get_price())


# class Numbers:
#     __count = 0
#
#     @staticmethod
#     def get_count():
#         return Numbers.__count
#
#     @staticmethod
#     def area(a, b, c):     # площадь треугольника по формуле Герона.
#         s = (a + b + c) / 2
#         Numbers.__count += 1
#         return s
#
#     @staticmethod
#     def area_1(a, b):      # площадь треугольника через основание и высоту
#         s = (a * b) * 0.5
#         Numbers.__count += 1
#         return s
#
#     @staticmethod
#     def area_3(a):        # площадь квадрата
#         s = a ** 2
#         Numbers.__count += 1
#         return s
#
#     @staticmethod
#     def area_4(a, b):      # площадь прямоугольника
#         s = a * b
#         Numbers.__count += 1
#         return s
#
#
# print("Площадь треугольника по формуле Герона: ", Numbers.area(3, 4, 5))
# print("Площадь треугольника через основание и высоту: ", Numbers.area_1(6, 7))
# print("Площадь квадрата: ", Numbers.area_3(7))
# print("Площадь прямоугольника: ", Numbers.area_4(2, 6))
# print("Количество подсчетов площади: ", Numbers.get_count())


# -// вариант 1 //- (через @property # через декоратор Property можно передавать только 1 свойство)

# class Account:
#     rate_usd = 0.013                                  # статические свойства
#     rate_eur = 0.011
#     suffix = "RUB"
#     suffix_usd = "USD"
#     suffix_eur = "EUR"
#
#     def __init__(self, num, surname, percent, value):
#         self.__num = num                               # динамические свойства
#         self.__surname = surname
#         self.__percent = percent
#         self.__value = value
#         print(f"Счет #{self.__num} принадлежащий {self.__surname} был открыт.")
#         print("*" * 50)
#
#     def __del__(self):             # служебный метод DEL отработает после выполнения программы (разрывает ссылку)
#         print("*" * 50)
#         print(f"Счет #{self.__num} принадлежащий {self.__surname} был закрыт.")
#         # del self.__num
#
#     @staticmethod
#     def convert(value, rate):
#         return value * rate
#
#     @classmethod
#     def set_usd_rate(cls, rate):
#         cls.rate_usd = rate
#
#     @classmethod
#     def set_eur_rate(cls, rate):
#         cls.rate_eur = rate
#
#     @staticmethod
#     def __check_value(z):
#         if isinstance(z, str) or isinstance(z, int):
#             return True
#         return False
#
#     @property
#     def num(self):
#         return self.__num
#
#     @num.setter
#     def num(self, num):
#         if Account.__check_value(self):
#             self.__num = num
#         else:
#             print("Неверный формат")
#
#     @property
#     def surname(self):
#         return self.__surname
#
#     @surname.setter
#     def surname(self, surname):
#         if Account.__check_value(self):
#             self.__surname = surname
#         else:
#             print("Неверный формат")
#
#     @property
#     def percent(self):
#         return self.__percent
#
#     @percent.setter
#     def percent(self, percent):
#         if Account.__check_value(self):
#             self.__percent = percent
#         else:
#             print("Неверный формат")
#
#     @property
#     def val(self):
#         return self.__value
#
#     @val.setter
#     def val(self, value):
#         if Account.__check_value(self):
#             self.__value = value
#         else:
#             print("Неверный формат")
#
#     def convert_to_usd(self):
#         usd_val = Account.convert(self.__value, Account.rate_usd)
#         print(f"Состояние счета: {usd_val} {Account.suffix_usd}")
#
#     def convert_to_eur(self):
#         eur_val = Account.convert(self.__value, Account.rate_eur)
#         print(f"Состояние счета: {eur_val} {Account.suffix_eur}")
#
#     def edit_owner(self, surname):
#         self.__surname = surname
#
#     def add_percents(self):
#         self.__value += self.__value * self.__percent
#         print("Проценты были успешно начислены")
#         self.print_balance()
#
#     def withdraw_money(self, val):
#         if val > self.__value:
#             print(f"К сожалению у вас нет {val} {Account.suffix}")
#         else:
#             self.__value -= val
#             print(f"{val} {Account.suffix} было успешно снято")
#         self.print_balance()
#
#     def add_money(self, val):
#         self.__value += val
#         print(f"{val} {Account.suffix} было успешно добавлено!")
#         self.print_balance()
#
#     def print_balance(self):
#         print(f"Текущий баланс {self.__value} {Account.suffix}")
#
#     def print_info(self):
#         print("Информация о счете: ")
#         print("-" * 20)
#         print(f"#{self.__num}")
#         print(f"Владелец: {self.__surname}")
#         self.print_balance()
#         print(f"Проценты: {self.__percent:.0%}")               # 0 - это количество символов после точки с процентом
#         print("-" * 20)
#
#
# acc = Account("12345", "Долгих", 0.03, 1000)
# # acc.print_balance()
# # acc.num = 5
# # print(acc.num)
# acc.print_info()
# acc.convert_to_usd()
# acc.convert_to_eur()
# print()
# Account.set_usd_rate(2)
# acc.convert_to_usd()
# Account.set_eur_rate(3)
# acc.convert_to_eur()
# print()
# acc.edit_owner("Дюма")
# acc.print_info()
# print()
# acc.add_percents()
# print()
#
# acc.withdraw_money(100)
# print()
#
# # acc.withdraw_money(3000)
# # print()
#
# acc.add_money(5000)
# print()
#
# acc.withdraw_money(3000)
# print()


# -// ВАРИАНТ 2 //- (через get, set)


# class Account:
#     rate_usd = 0.013  # статические свойства
#     rate_eur = 0.011  # статические свойства
#     suffix = "RUB"  # статические свойства
#     suffix_usd = "USD"  # статические свойства
#     suffix_eur = "EUR"  # статические свойства
#
#     def __init__(self, num, surname, percent, value):  # инициализатор
#         self.__num = num  # динамические свойства
#         self.__surname = surname
#         self.__percent = percent
#         self.__value = value
#         print(f"Счет #{self.__num} принадлежащий {self.__surname} был открыт.")
#         print("*" * 50)
#
#     def __del__(self):  # служебный метод DEL отработает после выполнения программы (разрывает ссылку)
#         print("*" * 50)
#         print(f"Счет #{self.__num} принадлежащий {self.__surname} был закрыт.")
#
#     @staticmethod
#     def convert(value, rate):
#         return value * rate
#
#     @classmethod
#     def set_usd_rate(cls, rate):
#         cls.rate_usd = rate
#
#     @classmethod
#     def set_eur_rate(cls, rate):
#         cls.rate_eur = rate
#
#     def __check_value(self):  # метод проверки
#         if isinstance(self, int) or isinstance(self, float):
#             return True
#         return False
#
#     def set_coord(self, num, surname, percent, value):
#         if Account.__check_value(self):
#             self.__num = num
#             self.__surname = surname
#             self.__percent = percent
#             self.__value = value
#         else:
#             print("Неверный формат")
#
#     def get_coord_num(self):
#         return self.__num
#
#     def get_coord_surname(self):
#         return self.__surname
#
#     def get_coord_percent(self):
#         return self.__percent
#
#     def get_coord_value(self):
#         return self.__value
#
#     def convert_to_usd(self):
#         usd_val = Account.convert(self.__value, Account.rate_usd)
#         print(f"Состояние счета: {usd_val} {Account.suffix_usd}")
#
#     def convert_to_eur(self):
#         eur_val = Account.convert(self.__value, Account.rate_eur)
#         print(f"Состояние счета: {eur_val} {Account.suffix_eur}")
#
#     def edit_owner(self, surname):
#         self.__surname = surname
#
#     def add_percents(self):
#         self.__value += self.__value * self.__percent
#         print("Проценты были успешно начислены")
#         self.print_balance()
#
#     def withdraw_money(self, val):
#         if val > self.__value:
#             print(f"К сожалению у вас нет {val} {Account.suffix}")
#         else:
#             self.__value -= val
#             print(f"{val} {Account.suffix} было успешно снято")
#         self.print_balance()
#
#     def add_money(self, val):
#         self.__value += val
#         print(f"{val} {Account.suffix} было успешно добавлено!")
#         self.print_balance()
#
#     def print_balance(self):
#         print(f"Текущий баланс {self.__value} {Account.suffix}")
#
#     def print_info(self):
#         print("Информация о счете: ")
#         print("-" * 20)
#         print(f"#{self.__num}")
#         print(f"Владелец: {self.__surname}")
#         self.print_balance()
#         print(f"Проценты: {self.__percent:.0%}")  # 0 - это количество символов после точки с процентом
#         print("-" * 20)
#
#
# acc = Account("12345", "Долгих", 0.03, 1000)
# # acc.print_balance()
# acc.print_info()
# acc.convert_to_usd()
# acc.convert_to_eur()
# print()
#
# Account.set_usd_rate(2)
# acc.convert_to_usd()
# Account.set_eur_rate(3)
# acc.convert_to_eur()
# print()
#
# acc.edit_owner("Дюма")
# acc.print_info()
# print()
#
# acc.add_percents()
# print()
#
# acc.withdraw_money(100)
# print()
#
# # acc.withdraw_money(3000)
# # print()
#
# acc.add_money(5000)
# print()
#
# acc.withdraw_money(3000)
# print()

# class Rect:
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height
#
#     def show_rect(self):
#         print(f"Прямоугольник:\nШирина: {self.width}\nВысота: {self.height}")
#
#
# class RectFon(Rect):
#     def __init__(self, width, height, background):
#         super().__init__(width, height)
#         self.fon = background
#
#     def show_rect(self):
#         super().show_rect()
#         print("Фон:", self.fon)
#
#
# class RectBorder(Rect):
#     def __init__(self, width, height, thin, typed, color):
#         super().__init__(width, height)
#         self.thin = thin
#         self.typed = typed
#         self.color = color
#
#     def show_rect(self):
#         super().show_rect()
#         print("Толщина рамки:", self.thin)
#         print("Тип рамки:", self.typed)
#         print("Цвет рамки:", self.color)
#
#
# shape1 = RectFon(400, 200, "yellow")
# shape1.show_rect()
# print()
# shape2 = RectBorder(600, 300, "1px", "solid", "red")
# shape2.show_rect()


# class Student:
#     def __init__(self, name):
#         self.name = name
#         self.note = self.Noteboock()
#
#     def show(self):
#         print(self.name, end="")
#         self.note.show()             # обращаемся к методу show вложенному в класс Noteboock
#
#     class Noteboock:
#         def __init__(self):
#             self.model = "HP"
#             self.cpu = "i7"
#             self.ddr = "16"
#
#         def show(self):
#             print(f" => {self.model}, {self.cpu}, {self.ddr}")
#
#
# s1 = Student("Roman")
# s2 = Student("Vladimir")
#
# s1.show()
# s2.show()

# import math
# from abc import ABC, abstractmethod
#
#
# class Shape(ABC):  # родительский класс
#     def __init__(self, color):
#         self.color = color
#
#     @abstractmethod
#     def perimeter(self):
#         pass
#
#     @abstractmethod
#     def square(self):
#         pass
#
#     @abstractmethod
#     def draw(self):
#         pass
#
#     @abstractmethod
#     def print_info(self):
#         pass
#
#
# class Square(Shape):  # квадрат
#     def __init__(self, side, color):
#         super().__init__(color)
#         self.side = side
#
#     def square(self):
#         return self.side * self.side
#
#     def perimeter(self):
#         return 4 * self.side
#
#     def draw(self):
#         return ("* " * self.side + "\n") * self.side
#
#     def print_info(self):
#         print(f"=== Квадрат ===\nСторона: {self.side}\nЦвет: {self.color}\nПлощадь:"
#               f" {self.square()}\nПериметр: {self.perimeter()}\n{self.draw()}")
#
#
# class Rectangle(Shape):  # прямоугольник
#     def __init__(self, length, width, color):
#         super().__init__(color)
#         self.length = length
#         self.width = width
#
#     def square(self):
#         return self.length * self.width
#
#     def perimeter(self):
#         return 2 * (self.length + self.width)
#
#     def draw(self):
#         return ("* " * self.width + "\n") * self.length
#
#     def print_info(self):
#         print(f"=== Прямоугольник ===\nДлина: {self.length}\nШирина: {self.width}\nЦвет: {self.color}\nПлощадь:"
#               f" {self.square()}\nПериметр: {self.perimeter()}\n{self.draw()}")
#
#
# class Triangle(Shape):  # треугольник
#     def __init__(self, side_1, side_2, side_3, color):
#         super().__init__(color)
#         self.side_1 = side_1
#         self.side_2 = side_2
#         self.side_3 = side_3
#
#     def square(self):
#         p = self.perimeter() / 2
#         return round(math.sqrt(p * (p - self.side_1) * (p - self.side_2) * (p - self.side_3)), 2)
#
#     def perimeter(self):
#         return self.side_1 + self.side_2 + self.side_3
#
#     def draw(self):
#         rows = []
#         for i in range(self.side_2):
#             rows.append(" " * i + "*" * (self.side_1 - 2 * i))
#         return "\n".join(reversed(rows))
#
#     def print_info(self):
#         print(f"=== Треугольник ===\nСторона 1: {self.side_1}\nСторона 2: {self.side_2}\nСторона 3: "
#               f"{self.side_3}"
#               f"\nЦвет: {self.color}\nПлощадь: {self.square()}\nПериметр: {self.perimeter()}\n{self.draw()}")
#
#
# group = [
#     Square(3, "red"),
#     Rectangle(3, 7, "green"),
#     Triangle(11, 6, 6, "yellow")
#     ]
#
# for i in group:
#     i.print_info()

# ДЗ 13/05/25

# class Car:
#     def __init__(self, brand, model, year, mileage):
#         self.brand = brand
#         self.model = model
#         self.year = year
#         self.mileage = mileage
#
#     def print_info(self):
#         print(f"{self.brand}, {self.model}, {self.year} год, {self.mileage} км")
#
#
# class ElectroCar(Car):
#     def __init__(self, brand, model, year, mileage, power):
#         super().__init__(brand, model, year, mileage)
#         self.power = power
#
#     def get_battery(self):
#         print(f"Этот автомобиль имеет мощность {self.power} %")
#
#
# m1 = ElectroCar("Tesla", "T", 2018, 99000, 100)
# m1.print_info()
# m1.get_battery()


# import json
# from random import choice
#
#
# def gen_person():
#     name = ''
#     tel = ''
#
#     letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
#     nums = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
#
#     while len(name) != 7:
#         name += choice(letters)
#     # print(name)
#
#     while len(tel) != 10:
#         tel += choice(nums)
#     # print(tel)
#
#     person = {
#         'name': name,
#         'tel': tel
#     }
#
#     return person, tel
#
#
# def write_json(person_dict, num):
#     try:
#         data = json.load(open("persons1.json"))
#     except FileNotFoundError:
#         data = {}
#
#     data[num] = person_dict
#
#     with open("persons1.json", "w") as f:
#         json.dump(data, f, indent=2)
#
#
# for i in range(5):
#     write_json(gen_person()[0], gen_person()[1])


# import csv
#
# with open("data2.csv", encoding='utf-8') as f:
#     # file_names = ['hostname', 'vendor', 'model', 'location']
#     file_reader = csv.reader(f, delimiter=";")
#     for row in file_reader:
#         print(row)

# import csv
# import requests
# from bs4 import BeautifulSoup
#
#
# def get_html(url):
#     row = requests.get(url)
#     return row.text
#
#
# def get_data(html):
#     soup = BeautifulSoup(html, "lxml")
#     element = soup.find_all("div",  class_="col-lg-6 col-md-4 col-sm-6 col-xs-6")
#     for elem in element:
#         product = elem.find("a", class_='catalog-item__name').text
#         price = elem.find("div", class_='current-price').text
#         data = {
#             "product": product,
#             "price": price
#         }
#         print(data)
#         # write_csv(data)
#
#
# def write_csv(data):
#     with open("plugin2.csv", "w", encoding='utf-8') as f:
#         writer = csv.writer(f, delimiter=";", lineterminator="\r")
#         writer.writerow((data["product"],
#                          data["price"]))
#
#
# def main():
#     url = "https://www.olant-shop.ru/"
#
#     print(get_data(get_html(url)))
#
#
# if __name__ == '__main__':
#     main()


# Проверка доступа к сайту
# row = requests.get("https://www.olant-shop.ru/")
# print(row)


# ДЗ (Паттерн MVS)


