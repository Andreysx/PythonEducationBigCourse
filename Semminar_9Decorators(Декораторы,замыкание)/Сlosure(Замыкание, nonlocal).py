# Термины лекции
# ● Замыкание (англ. closure) в программировании — функция первого класса,
# в теле которой присутствуют ссылки на переменные, объявленные вне тела
# этой функции в окружающем коде и не являющиеся её параметрами.
# ● Декоратор — структурный шаблон проектирования, предназначенный для
# динамического подключения дополнительного поведения к объекту.
# Подробный текст лекции
#
# 1. Что такое замыкания
# Прежде чем погрузиться в декораторы поговорим о замыканиях в
# программировании вообще и в Python в частности. Плюс стоит вспомнить об
# областях видимости в Python.
# Области видимости
#
# def func(a):
#     x = 42
#     res = x + a
#     return res
#
# x = 73
# print(func(64))
#
# В этом примере глобальная переменная x равна 73, но при сложении внутри
# функции к значению a прибавляется 42 — значение локальной переменной x.
# Функция как объект высшего порядка
# Рассмотрим простой пример функции:
#
# def add_str(a: str, b: str) -> str:
#     return a + ' ' + b
# print(add_str('Hello', 'world!'))
#
# На вход передаём две строки и возвращаем новую из двух старый и пробела
# посередине. Но функцию можно переписать иначе. Вспомним, что в Python все
# функции высшего порядка. А это значит, что их можно передавать как объекты в
# другие функции:
#
# from typing import Callable
#
# def add_one_str(a: str) -> Callable[[str], str]:
#     def add_two_str(b: str) -> str:
#         return a + ' ' + b
#     return add_two_str
#
# print(add_one_str('Hello')('world!'))
#
#
# Результат получили такой же, но код работает иначе.
#
# ● Функция add_one_str принимает на вход один параметр в качестве начала
# строки и возвращает локальную функцию add_two_str. Обратите внимание на
# отсутствие круглых скобок. Функцию передаём , а не вызываем.
# ● Функция add_two_str принимает вторую часть строки, соединяет её с первой
# и возвращает ответ.
# ● При вызове функций значения указывается в отдельных круглых скобках.
# Первое попадает в параметр a. Далее часть строки: add_one_str('Hello')
# возвращает функцию add_two_str и уже она вызывается и принимает
# аргумент во вторых скобках.
# Благодаря передаче одной функции другой мы можем создавать замыкания.
# Замыкаем функцию с параметрами
#
# Внесём небольшие правки в пример кода:
# from typing import Callable
#
# def add_one_str(a: str) -> Callable[[str], str]:
#     def add_two_str(b: str) -> str:
#         return a + ' ' + b
#     return add_two_str
#
# hello = add_one_str('Hello')
# bye = add_one_str('Good bye')
#
# print(hello('world!'))
# print(hello('friend!'))
# print(bye('wonderful world!'))
#
# print(f'{type(add_one_str) = }, {add_one_str.__name__ = },{id(add_one_str) = }')
# print(f'{type(hello) = }, {hello.__name__ = }, {id(hello) = }')
# print(f'{type(bye) = }, {bye.__name__ = }, {id(bye) = }')
#
# Во-первых мы не изменяли исходную функцию. Но мы создали две переменные
# hello и bye и поместили в них результат работы функции add_one_str с разными
# аргументами. Теперь мы можем вызывать новые функции и получать объединённые
# 5
# строки передавая только окончание. Первая часть строки оказалась замкнута в
# локальной области видимости. И у каждой из двух новых функций область своя и
# начало строки своё.
# А теперь посмотрите на результат работы трёх нижних строк кода. Все три
# переменные являются функциями, что очевидно. Но если функция add_one_str
# является самой собой, то функции hello и bye на самом деле являются двумя
# разными экземплярами функции add_two_str. id, т.е. адреса в оперативной памяти
# разные, а названия указывают на оригинал.
# Замыкаем изменяемые и неизменяемые
# объекты
#
# В очередной раз внесём правки в пример кода:
# from typing import Callable
#
# def add_one_str(a: str) -> Callable[[str], str]:
#     names = []
#     def add_two_str(b: str) -> str:
#         names.append(b)
#         return a + ', ' + ', '.join(names)
#     return add_two_str
#
# hello = add_one_str('Hello')
# bye = add_one_str('Good bye')
#
# print(hello('Alex'))
# print(hello('Karina'))
# print(bye('Alina'))
# print(hello('John'))
# print(bye('Neo'))
#
# Во внешнюю функцию добавлен список names. При каждом вызове внутренней
# функции в список добавляется новое значение из параметра b и возвращается
# полное содержимое списка в виде строки. У каждой из двух функций hello и bye
# оказывается свой список names. Они не связаны между собой, но каждый хранит
# список имён до конца работы программы. Обратите внимание, что list является
# изменяемым типом данных. Что будет, если мы перепишем код и заменим list на
# неизменяемый str?
#
#
# from typing import Callable
#
# def add_one_str(a: str) -> Callable[[str], str]:
#     text = ''
#     def add_two_str(b: str) -> str:
#         nonlocal text
#         text += ', ' + b
#         return a + text
#
#     return add_two_str
#
# hello = add_one_str('Hello')
# bye = add_one_str('Good bye')
#
# print(hello('Alex'))
# print(hello('Karina'))
# print(bye('Alina'))
# print(hello('John'))
# print(bye('Neo'))
#
# Изменения способа получения строки c join для списка на конкатенацию для строки
# не принципиально. Но стоит помнить, что сложение строк более дорогая операция
# по времени и по памяти, особенно если она находится внутри цикла.
# Что более важно - неизменяемый тип данных у строки text. Без добавления строчки
# кода nonlocal text была бы получена ошибка UnboundLocalError: local variable 'text'
# referenced before assignment. Мы явно указали, что хотим обращаться к
# неизменяемому объекту для изменения его значения.
# Как можно изменить неизменяемое? Мы создаём новый объект и присваиваем ему
# старое имя. Старый объект будет удалён сборщиком мусора. А команда nonlocal
# сообщает Python, что изменения ссылки на объект должны затронуть область
# видимости за пределами функции add_two_str.
# Подведём промежуточный итог. Благодаря тому что в Python всё объект, а функции
# являются функциями высшего порядка, мы можем вкладывать во внешнюю
# функцию различные переменные и внутренние функции. Далее возвращая из
# внешней функции внутреннюю создаём замыкания.

# Задание
# Перед вами несколько строк кода. Напишите что выведет программа, не запуская
# код. У вас 3 минуты.


# from typing import Callable
#Функция main принимает на вход параметр х - целое число
# Возвращает эта функция какой-то вызываемый объект, то есть другую функцию
# Эта другая функция принимает на вход целое число
# А возвращает словарь где ключом является int , а значением является int
# При аннотации типов если мы хотим указать ключ и значение словаря
# Мы используем dict[int - тип ключа, int - тип значения]
# def main(x: int) -> Callable[[int], dict[int, int]]:
#     d = {}
#     def loc(y: int) -> dict[int, int]:
#         for i in range(y):
#             d[i] = x ** i
#         return d
#     return loc
#
# small = main(42)
# big = main(73)
#
# print(small(7))
# print(big(7))
# print(small(3))
#
# Вывод:
# {0: 1, 1: 42, 2: 1764, 3: 74088, 4: 3111696, 5: 130691232, 6: 5489031744}
# {0: 1, 1: 73, 2: 5329, 3: 389017, 4: 28398241, 5: 2073071593, 6: 151334226289}
# {0: 1, 1: 42, 2: 1764, 3: 74088, 4: 3111696, 5: 130691232, 6: 5489031744}