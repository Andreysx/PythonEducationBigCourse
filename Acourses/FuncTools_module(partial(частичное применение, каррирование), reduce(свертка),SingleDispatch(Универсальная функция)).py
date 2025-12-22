
# Основное предназначение functools.partial - создание новой функции(чатично примененной) на основании уже имеющейся, с меньшим количеством аргументов.
# Это делается за счет фиксирования значений у некоторых аргументов.

from functools import partial


def power(base, exponent):
    return base ** exponent


# Создаем функцию square, которая возводит во 2ую степень
square = partial(power, exponent=2)
print(square(3))  # возводим 3 в квадрат
print(square(4))  # возводим 4 в квадрат

# Создаем функцию cub, которая возводит во 3ую степень
cub = partial(power, exponent=3)
print(cub(2))  # возводим 2 в 3ю степень
print(cub(4))  # возводим 4 в 3ю степень

#
# Но ваши функции могут терять свои метаданные в двух случаях:
#
# Когда функция используется для создания новой частично примененной функции с использованием functools.partial -  update_wrapper
# Когда функцию оборачивают при помощи декоратора @wraps





# Функция reduce
# functools.reduce — это функция высшего порядка в модуле functools,
# предназначенная для свертки (постепенного уменьшения) итерируемой последовательности (списка, кортежа и т. д.)
# с целью приведения последовательности к одному накопленному значению.
# Достигается это за счет последовательного применения функции с двумя аргументами к первым двум элементам последовательности,
# затем к результату и следующему элементу, и так далее, пока не будут обработаны все элементы.
# def reduce(function, sequence, initial=_initial_missing):

# from functools import reduce
#
# numbers = [1, 2, 3, 4, 5]
#
#
# def add(a, b):
#     return a + b
#
#
# total = reduce(add, numbers)
# print(total)
#
#
# print(reduce(add, (10, 20, 30), 5))
#
#
# total_1 = reduce(lambda a, b: a + b, numbers)
# print(total_1)
#
# product = reduce(lambda a, b: a * b, numbers)
# print(product)

# Универсальная функция
# Универсальная функция («generic function») - функция, состоящая из нескольких функций, реализующих одну и ту же операцию для разных типов.
# Какая реализация должна использоваться во время вызова, определяется алгоритмом диспетчеризации.

# Одиночная диспетчеризация («single-dispatch») - это алгоритм выбора реализации универсальной функции на основе  одного аргумента.


from functools import singledispatch


@singledispatch
def my_func(arg):
    print(f'default my_func({arg})')


@my_func.register(int)
def my_func_int(arg):
    print(f'my_func_int({arg})')


@my_func.register(list)
def my_func_list(arg):
    print('my_func_list()')
    print(*arg)


my_func('hello')
my_func(1)
my_func(42.3)
my_func(['a', 'b', 'c'])




































from functools import singledispatch
from datetime import date, datetime
from pathlib import Path
from os import path
from typing import Any


# Реализуйте функцию convert
@singledispatch
def convert(arg, is_need_time=True):
    raise TypeError(f"Unsupported type: {type(arg)}")


# Регистрация для базовых типов
@convert.register(float)
@convert.register(int)
@convert.register(str)
def _(arg):
    return arg


# Для Path
@convert.register
def _(arg: Path) -> str:
    return str(arg)


# Для datetime с поддержкой is_need_time
@convert.register
def convert_datetime(arg: datetime, is_need_time=True) -> str:
    if is_need_time:
        return arg.strftime("%d.%m.%Y %H:%M:%S")
    else:
        return arg.strftime("%d.%m.%Y")


# Для date с поддержкой is_need_time
@convert.register
def convert_date(arg: date, is_need_time=True) -> str:
    if is_need_time:
        return arg.strftime("%d.%m.%Y 00:00:00")
    else:
        return arg.strftime("%d.%m.%Y")


# Ниже располагаются проверки для функции convert

assert convert("Hello, World") == "Hello, World"
assert convert(42) == 42
assert convert(3.14) == 3.14

assert convert(Path("tmp/hello.txt")) == path.join('tmp', 'hello.txt')
assert convert(Path("some/path/to/file.txt")) == path.join('some', 'path', 'to', 'file.txt')

assert convert(datetime(2023, 10, 29, 5, 6)) == '29.10.2023 05:06:00'
assert convert(datetime(2021, 8, 12, 12, 8, 58), is_need_time=True) == '12.08.2021 12:08:58'
assert convert(datetime(1999, 9, 29, 5, 6), is_need_time=False) == '29.09.1999'

assert convert(date(2023, 10, 29), is_need_time=True) == '29.10.2023 00:00:00'
assert convert(date(2009, 12, 31)) == '31.12.2009 00:00:00'
assert convert(date(2023, 7, 11), is_need_time=False) == '11.07.2023'

try:
    print(convert([1, 2, 3]))
except TypeError:
    pass

try:
    print(convert({1: 2, 3: 4}))
except TypeError:
    pass

print('Good')
