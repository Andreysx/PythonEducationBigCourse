# Значения по умолчанию
# Функция может содержать значения по умолчанию для своих параметров.
# Например:
#
#
# def quadratic_equations(a, b=0, c=0):
#     d = b ** 2 - 4 * a * c
#     if d > 0:
#         return (-b + d ** 0.5) / (2 * a), (-b - d ** 0.5) / (2 * a)
#     if d == 0:
#         return -b / (2 * a)
#
# print(quadratic_equations(2, -9))
#
#
# Переменная a должна быть передана в обязательном порядке. Если не передать 2-й
# и/или 3-й аргумент, в переменные попадут нули как значения по умолчанию.
# 🔥 PEP-8! Для указания значения по умолчанию используется знак
# равенства. До и после такого равно пробелы не ставятся.
# Изменяемый объект как значение
# по умолчанию
# В качестве значения по умолчанию нельзя указывать изменяемы типы: списки,
# словари и т.п. Это приведёт к неожиданным результатам:
#
# def from_one_to_n(n, data=[]):
#     for i in range(1, n + 1):
#         data.append(i)
#     return data
#
# new_list = from_one_to_n(5)
# print(f'{new_list = }')
# other_list = from_one_to_n(7)
# print(f'{other_list = }')
#
# other_list содержит в себе и новую последовательность и ту, которая была в списке
# new_list. Связано это с тем, что значение по умолчанию задаётся один раз при
# создании функции. Каждый вызов — работа со списком data и его очередное
# изменение.
# Если в качестве значения по умолчанию нужен изменяемый тип данных,
# используют особый приём с None
#
# def from_one_to_n(n, data=None):
#     if data is None:
#         data = []
#     for i in range(1, n + 1):
#         data.append(i)
#     return data
#
# Если изменяемый объект не передан, он создаётся по новой для каждого вызова
# функции.
#
# Позиционные и ключевые параметры
# Пришло время поговорить о позиционных и ключевых параметрах функции. Начнём
# с общего синтаксиса.
#
# def func(positional_only_parameters, /, positional_or_keyword_parameters, *,
# keyword_only_parameters):
#     pass
#
# При указании параметров функции вначале идут позиционные параметры. При
# вызове функции передаются значения без указания имени переменной-аргумента.
# Косая черта не является переменной. Это символ разделитель. После неё могут
# идти как позиционные, так и ключевые параметры. Далее символ разделитель
# звёздочка указывает только на ключевые параметры.
# 🔥 Важно! Косая черта и звёздочка одновременно или по отдельности
# могут отсутствовать при определении функции.
# Разберем передачу аргументов по позиции и по имени на примерах.
# ● Пример обычной функции:
#
# def standard_arg(arg):
#     print(arg) # Принтим для примера, а не для привычки
#
# standard_arg(42)
# standard_arg(arg=42)
#
# Функция может принимать значения по позиции и по ключу. Мы явно указали имя
# переменной.
# ● Пример только позиционной функции:
#
# def pos_only_arg(arg, /):
#     print(arg) # Принтим для примера, а не для привычки
#
# pos_only_arg(42)
# pos_only_arg(arg=42) # TypeError: pos_only_arg() got some
#
# positional-only arguments passed as keyword arguments: 'arg'
# Теперь функция принимает только позиционные параметры.
# ● Пример только ключевой функции:
#
# def kwd_only_arg(*, arg):
#     print(arg) # Принтим для примера, а не для привычки
#
# kwd_only_arg(42)
# kwd_only_arg(arg=42)
#
# А теперь наоборот, можем принимать только значения по ключу.
# ● Пример функции со всеми вариантами параметров:
# def combined_example(pos_only, /, standard, *, kwd_only):
#     print(pos_only, standard, kwd_only) # Принтим для примера, ане для привычки
#
# combined_example(1, 2, 3) # TypeError: combined_example() takes 2 positional arguments but 3 were given
# combined_example(1, 2, kwd_only=3)
# combined_example(1, standard=2, kwd_only=3)
# combined_example(pos_only=1, standard=2, kwd_only=3) # TypeError: combined_example() got some positional-only arguments passed as keyword arguments: 'pos_only'
# И наконец пример со всеми возможными вариантами параметров.
# 🔥 Важно! Если функция принимает несколько ключевых параметров,
# порядок передачи аргументов может отличаться.
#
# def triangulation(*, x, y, z):
#     pass
# triangulation(y=5, z=2, x=11)
