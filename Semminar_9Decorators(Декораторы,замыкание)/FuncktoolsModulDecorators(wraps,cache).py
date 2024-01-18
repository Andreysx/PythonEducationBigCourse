# 4. Декораторы functools
# Дополнительные возможности декорирования предоставляет модуль functools
# декоратор.
# Декоратор wraps
# Рассмотрим код из прошлой главы, но добавим строку документации в функцию
# factorial.
#
#
# ...
# @count(10)
# def factorial(n: int) -> int:
#     """Returns the factorial of the number n."""
#     f = 1
#     for i in range(2, n + 1):
#         f *= i
#     return f
#
#
# print(f'{factorial(1000) = }')
# print(f'{factorial.__name__ = }')
#
# help(factorial)
#
#
# Вместо ожидаемого вывода документации о функции и её названия получаем
# информацию об обёртке wrapper:
# factorial.__name__ = 'wrapper'
# Help on function wrapper in module __main__:
# wrapper(*args, **kwargs)
#
# Чтобы исправить ситуацию, воспользуемся декоратором wraps из functools.
#
# import time
# from typing import Callable
# from functools import wraps
#
#
# def count(num: int = 1):
#     def deco(func: Callable):
#     @wraps(func)
#         def wrapper(*args, **kwargs):
#             time_for_count = []
#             ...
#
#
# Декоратор wraps добавляется к функции wrapper, т.е. к самой глубоко вложенной
# функции. В качестве аргумента wraps должен получить параметр декларируемой
# функции. Теперь factorial возвращает свои название и строку документации.
#
#
#
# Декоратор cache
# Рассматривая возможности по замыканию переменных мы создали кэширующий
# декоратор. В модуле functools есть декоратор cache с подобным функционалом. При
# необходимости кэширования данных рекомендуется использовать именно его, как
# более оптимальное решение из коробки.
#
#
# from functools import cache
#
#
# @cache
# def factorial(n: int) -> int:
#     print(f'Вычисляю факториал для числа {n}')
#     f = 1
#     for i in range(2, n + 1):
#         f *= i
#     return f
#
#
# print(f'{factorial(10) = }')
# print(f'{factorial(15) = }')
# print(f'{factorial(10) = }')
# print(f'{factorial(20) = }')
# print(f'{factorial(10) = }')
# print(f'{factorial(20) = }')
#
#
# Как вы видите только первые вызовы запускают функцию. Повторный вызов с уже
# передававшимся аргументом обрабатывается декоратором cache.
