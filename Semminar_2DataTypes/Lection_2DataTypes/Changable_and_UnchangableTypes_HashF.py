# Changable: list, bytearray, set, dict
# Unchangable: int bool float complex str tuple bytes frozenset
# Как вы можете заметить все числа в Python относятся к неизменяемым типам
# данных. А значит любые математические операции создают новый объект в памяти.
# Пример ниже служит подтверждением.
# a = с = 2
# b = 3
# print(a, id(a), b, id(b), c, id(c))
# a = b + c
# print(a, id(a), b, id(b), c, id(c))
# Обратите внимание на первую строку кода. Подобное присваивание допустимо в
# Python. Переменные a и c будут указывать на один и тот же объект.
# После сложения переменная a указывает на новый объект. Переменная c по
# прежнему указывает на число 2, т.к. int — неизменяемый тип данных.
# Хэш hash() как проверка на неизменяемость
# Хеш — это криптографическая функция хеширования, которую обычно
# называют просто хэшем. Хеш-функция представляет собой алгоритм,
# который может преобразовать произвольный массив данных в набор бит
# фиксированной длины.
# В Python для получения хеша используется функция hash(). Если объект
# является неизменяемым, функция возвращает число — хеш-сумму.
# Изменяемые объекты хешировать нельзя исходя из самого определения
# хеш-функции. Если массив данных может меняться, значит будет меняться и
# хеш-сумма. Подобное поведение нарушало бы логику кода. Рассмотрим на
# примере.
# x = 42
# y = 'text'
# z = 3.1415
# print(hash(x), hash(y), hash(z))
# my_list = [x, y, z]
# print(hash(my_list)) # получим ошибку, т.к. list изменяемый
# 9
# Как видите нижняя строка кода вызывает ошибку TypeError: unhashable type:
# 'list' Если вдруг забыли изменяемый объект или нет, просто попробуйте
# получить его хеш.


