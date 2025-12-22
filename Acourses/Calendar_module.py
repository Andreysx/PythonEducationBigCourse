import calendar
#
# day_name содержит полные имена всех дней недели
# day_abbr содержит короткие имен всех дней недели
# month_name содержит полные имена всех месяцев
# month_abbr содержит короткие имена всех месяцев

# print(list(calendar.day_name))
# print(list(calendar.day_abbr))
# print(list(calendar.month_name))
# print(list(calendar.month_abbr))


# Метод month используется для получения календаря месяца в виде многострочной строки
# calendar.month(2024, 3)
# month(year, month, w=0, l=0)
#
# Метод month возвращает в качестве своей работы отформатированную строку,
# представляющая собой значение календаря за один месяц.
# Поэтому нужно использовать функцию print для отображения.

# print(calendar.month(2024, 3))
# print(calendar.month(2024, 4, w=4))
# print(calendar.month(2024, 5, l=2))

# Метод prmonth
# Обратите внимание, что prmonth сама выводит на экран информацию без дополнительного вызова функции print.
# Метод prmonth ничего не возвращает
# calendar.prmonth(2024, 3)


# Метод month возвращает результат и ничего не печатает,
# метод prmonth наоборот печатает календарь, но ничего не возвращает


# Метод calendar
# print(calendar.calendar(2024))

# calendar(year, w=2, l=1, c=6, m=3)
# В нем имеются следующие параметры

# обязательный параметр  year - год, для которого должен быть создан календарь
# необязательный параметр  w - ширина между двумя колонками, по умолчанию принимает 2.
#
# необязательный параметр  l - количество строк между линиями календаря. Принимает значение 1 по умолчанию
# необязательный параметр  с - пространство между двумя месяцами, по умолчанию принимает значение в 6 пробелов.
# необязательный параметр  m - количество месяцев в одном ряду календаря, по умолчанию принимает значение 3.


# print(calendar.calendar(2023, m=2, c=4))

# Результатом вызова метода .calendar() является многострочная строка,
# в которой содержится информация о календаре за указанный год.


# Метод prcal
# calendar.prcal(2024)
# Метод .prcal() отличается от метода .calendar() только тем, что он ничего не возвращает (return None).
# Его предназначение именно в выводе не экран самого календаря,
# об этом говорят буквы «pr» в названии «prcal». Они обозначают слово «print».
# Значит для отображения календаря при помощи .prcal() нам не нужно дополнительно вызывать функцию print
# calendar.prcal(2023, m=2, c=4)


# Метод monthcalendar
# Метод monthcalendar() используется для получения вложенного списка, представляющего собой календарь месяца.
# Каждый элемент этого списка представляет собой неделю, в котором содержаться номера дней в месяце.
# Нулями представлены дни вне месяца, которые взяты для того, чтобы каждая неделя была полной и состояла из семи дней

# calendar.prmonth(2024, 3)
#
# print('-' * 20)
#
# days = calendar.monthcalendar(2024, 3)
# print(*days, sep='\n')


# Метод setfirstweekday
# calendar.MONDAY
# calendar.TUESDAY
# calendar.WEDNESDAY
# calendar.THURSDAY
# calendar.FRIDAY
# calendar.SATURDAY
# calendar.SUNDAY
# (MONDAY, TUESDAY, WEDNESDAY, THURSDAY, FRIDAY, SATURDAY, SUNDAY) = range(7)

# import calendar
#
# calendar.prmonth(2008, 7)
# days = calendar.monthcalendar(2008, 7)
# print(days)
#
# # import calendar
# calendar.setfirstweekday(calendar.FRIDAY)
# calendar.prmonth(2008, 7)
# days = calendar.monthcalendar(2008, 7)
# print(days)

#
# Метод firstweekday
# Метод firstweekday() используется для получения текущей настройки дня недели, с которого начинается каждая неделя.
# import calendar
# print(calendar.firstweekday())
#
# calendar.setfirstweekday(calendar.WEDNESDAY)
# print(calendar.firstweekday())
#
# calendar.setfirstweekday(6)
# print(calendar.firstweekday())


# Функция weekday
# Если мы хотим узнать, какой день конкретной даты, мы можем использовать функцию «weekday()».
# Эта функция принимает в качестве аргументов день, месяц и год. \
# Она вернет целое значение от 0 до 6, где 0 – понедельник, 1 – вторник, … 6 – воскресенье.
#
# Взгляните на реализацию функции weekday
#
# def weekday(year, month, day):
#     """Return weekday (0-6 ~ Mon-Sun) for year, month (1-12), day (1-31)."""
#     if not datetime.MINYEAR <= year <= datetime.MAXYEAR:
#         year = 2000 + year % 400
#     return datetime.date(year, month, day).weekday()
#
#
# Она принимает год, месяц, день и внутри себя создает объект даты по переданным аргументам.
# Затем вызывает одноименный метод weekday у объекта date
#
# Вот пример работы функции weekday
#
# import calendar
#
# calendar.prmonth(2008, 7)
#
# print(calendar.weekday(2024, 3, 5))
# print(calendar.weekday(2024, 3, 6))
# print(calendar.weekday(2024, 3, 7))
# print(calendar.weekday(2024, 3, 8))
# print(calendar.weekday(2024, 3, 9))
# print(calendar.weekday(2024, 3, 10))
# print(calendar.weekday(2024, 3, 11))
# print(calendar.weekday(2024, 3, 12))


# Метод weekheader
# Метод weekheader() используется для получения заголовка, содержащего сокращенные (при ширине меньше 9)
# или полные названия (при ширине от 9 и более) дней недели. Метод weekheader принимает значение ширины
#
# import calendar
# print(calendar.weekheader(1))
# print(calendar.weekheader(2))
# print(calendar.weekheader(3))
# print(calendar.weekheader(5))
# print(calendar.weekheader(9))
# print(calendar.weekheader(10))


# Функция monthrange
# Функция monthrange() используется для получения номера дня недели для первого дня месяца и
# количества дней в месяце для указанного года и месяца.
#
# def monthrange(year, month):
#     """Return weekday (0-6 ~ Mon-Sun) and number of days (28-31) for
#        year, month."""
#     if not 1 <= month <= 12:
#         raise IllegalMonthError(month)
#     day1 = weekday(year, month, 1)
#     ndays = mdays[month] + (month == February and isleap(year))
#     return day1, ndays
#
#
# Функция monthrange принимает сперва год, а затем номер месяца.
# Тип возвращаемого значения - кортеж из двух элементов
#
# import calendar
#
# print(calendar.monthrange(2024, 2))
# print(calendar.monthrange(2024, 3))
# print(calendar.monthrange(2024, 4))


# Функция isleap
# Мы можем проверить, является ли данный год високосным, используя функцию isleap(), находящуюся в модуле calendar.
# Эта функция принимает год в качестве аргумента и возвращает «True» или «False».
#
# Если вы думаете, что только деление года на 4 дает вам високосный год, то вы абсолютно ошибаетесь.
# Год является високосным, если он соответствует следующим правилам:
#
# Годы, делящиеся на 100 без остатка, не являются високосными, за исключением годов, которые делятся на
# 400 без остатка. Например, 1900 год не является високосным, а 2000 год — является.
# Годы делящиеся на 4 без остатка (например, 2016, 2024), являются високосными.
# Эти проверки как раз и реализуются внутри функции isleap()
#
# def isleap(year):
#     """Return True for leap years, False for non-leap years."""
#     return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)
#
#
# Вот пример ее работы
#
# import calendar
#
# print(2004, calendar.isleap(2004))
# print(2100, calendar.isleap(2100))
# print(2400, calendar.isleap(2400))
# print(2300, calendar.isleap(2300))
# print(2008, calendar.isleap(2008))


#  Функция leapdays
# Есть еще одна функция,  которая связана с високосными годами - leapdays().
# Она используется для получения количества високосных лет в указанном диапазоне лет.\
#     Принимает два года y1 и y2, причем y1 <= y2, и возвращает количество високосных лет в промежутке
# от y1 включительно до  y2 не включительно.
#
# def leapdays(y1, y2):
#     """Return number of leap years in range [y1, y2).
#        Assume y1 <= y2."""
#     y1 -= 1
#     y2 -= 1
#     return (y2//4 - y1//4) - (y2//100 - y1//100) + (y2//400 - y1//400)
#
#
# Вот пример ее работы
#
# import calendar
#
# print(calendar.leapdays(2015, 2018))
#
# print(calendar.leapdays(2015, 2020))
#
# print(calendar.leapdays(2015, 2021))


# import calendar
#
#
# def days_in_a_year(year: int) -> int:
#     count = 0
#
#     for i in range(1, 13):
#         days = calendar.monthrange(year, i)[1]
#         count += days
#
#     return count
# #
# #
# # print(days_in_a_year(int(input())))
# #
# # or
# #
# # print(isleap(int(input())) + 365)

# print(int(True))


# import calendar
#
# a = int(input().split()[2])
# b = int(input().split()[2])
#
#
# def count_leap(y1: int, y2: int) -> int:
#     if y2 > y1:
#         y1, y2 = y2, y1 # "множественное присваивание" (multiple assignment) или "обмен значений" (swap)
#     result = calendar.leapdays(y1, y2)
#     return abs(result) + 1
#
#
# print(count_leap(a, b))

# print(calendar.leapdays(2015, 2020))


# import calendar
#
# year = int(input())
# day = int(input())
#
# days = calendar.monthcalendar(year, day)
# temp = [j for i in days for j in i]
# result_2 = sum([1 for i in temp if i != 0])
#
# print(result_2)
#
# # или
# print(calendar.monthrange(year,day)[1])


# import calendar
# from collections import deque
#
#
# def get_forward_months(month: int) -> list:
#     month -= 1
#     if month not in range(0,13):
#         raise ValueError("Не правильный номер месяца")
#     deq = deque(calendar.month_abbr[1:])
#     deq.rotate(-month)
#     return list(deq)
#
#
#
# month = 32
# try:
#     print(get_forward_months(month))
# except ValueError as e:
#     print(e)


# import calendar
#
# calendar.prmonth(int(input()), int(input()), w=4, l=2)


import calendar

calendar.setfirstweekday(calendar.SUNDAY)
calendar.prmonth(int(input()), int(input()))
