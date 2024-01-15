# Использование from и as
#
# Помимо обычного импорта можно использовать более подробную форму записи.
# Зарезервированное слово from указывает на имя модуля или пакета, далее import и
# имена импортируемых объектов.
#
# from sys import builtin_module_names, path
# print(builtin_module_names)
# print(*path, sep='\n')
#
# Теперь при обращении к импортированным объектам не нужно указывать имя
# модуля. Мы явно добавили их в наш код, включили имена в область видимости.
# 💡 PEP-8! Конструкция from import допускает перечисление импортируемых
# имён объектов через запятую в одной строке. После from всегда указывается
# один модуль.
# Кроме выборочного импорта можно создавать псевдонимы для объектов через
# зарезервированное слово as. При этом доступ к объекту будет возможен только
# через псевдоним. Один объект — одно имя.
#
# import random as rnd
# from sys import builtin_module_names as bmn, path as p
# print(bmn)
# print(*p, sep='\n')
# print(rnd.randint(1, 6))
# print(path) # NameError: name 'path' is not defined
# print(sys.path) # NameError: name 'sys' is not defined
#
# В первой строке импортировали модуль random и присвоили ему имя rnd внутри
# текущей области видимости. Во второй строке импортировали переменную
# builtin_module_names под именем bmn и переменную path под именем p. Последние
# две строки вызывают ошибку имени. Мы не можем обратиться к переменной path,
# потому что дали ей другое имя — p. И обращение к модулю sys не работает, ведь мы
# его не импортировали. Только объекты из модуля.
# 🔥 Важно! Не стоит давать переменным короткие понятные лишь вам
# имена. Код должен легко читаться другими разработчиками. Исключения —
# общепризнанные сокращения, например import numpy as np.
# Плохой import * (импорт звёздочка)
# Ещё один вариант импорта: from имя_модуля import *
# Подобная запись импортирует из модуля все глобальные объекты за исключением
# тех, чьи имена начинаются с символа подчёркивания. Рассмотрим на примере.
#
# ● Файл super_module.py
# from random import randint
# SIZE = 100
# _secret = 'qwerty'
# __top_secret = '1q2w3e4r5t6y'
# def func(a: int, b: int) -> str:
# z = f'В диапазоне от {a} до {b} получили {randint(a, b)}'
# return z
# result = func(1, 6)
#
# В модуле есть следующие объекты:
# ● глобальная функция randint
# ● глобальная константа SIZE
# ● глобальная защищенная переменная _secret
# ● глобальная приватная переменная __top_secret
# ● глобальная функция func
# ● локальные параметры функции a и b
# ● локальная переменная функции z
# ● глобальная переменная result
# 🔥 Внимание! Если название объекта (переменной, функции и т.п.)
# начинается с символа подчёркивания, объект становится защищённым. Если
# имя начинается с двух подчёркиваний, объект становится приватным. Объекты
# без подчёркивания в начале имени — публичные. Подробнее разберём на
# лекциях по ООП.
# Импортируем модуль в основной файл программы через звёздочку и попробуем
# выполнить несколько операций.
#
# ● Файл main.py
# from super_module import *
# SIZE = 49.5
# print(f'{SIZE = }\n{result = }')
# print(f'{z = }') # NameError: name 'z' is not defined
# print(f'{_secret = }') # NameError: name '_secret' is not
# defined
# print(f'{func(100, 200) = }\n{randint(10, 20) = }')
# 8
# def func(a: int, b: int) -> int:
# return a + b
# print(f'{func(100, 200) = }')
#
# Первая строка импортирует в файл все глобальные публичные объекты. Далее мы
# определяем константу SIZE. В этот момент значение константы из модуля
# затирается новым значением. Возник конфликт имён и Python разрешил его в
# пользу нового значения константы. При этом содержимое переменной result
# берётся из модуля super_module, т.к. других определений переменной нет в файле.
# При попытке обратиться к локальной и защищённой переменным получаем ошибки.
# Они не были импортированы “звёздочкой”.
# Далее мы вызываем функции func и randint. Они верно отрабатывают код, т.к. обе
# были импортированы из внешнего модуля.
# В финале создаём свою функцию func. Возникает очередной конфликт имён,
# который Python разрешает в пользу новой функции. В результате вызов func() после
# её определения возвращает совсем другой результат, чем вызовом ранее.
# Промежуточный итог. Использование стиля from module import * зачастую приводит
# к неожиданным результатам, затрудняет отладку кода и мешает верному
# пониманию работы программы. Использовать подобный приём стоит в редких
# особенных случаях. Кроме того импорт всех доступных объектов может
# значительно замедлить работы программы, если таких объектов очень много.
#
# Переменная __all__
# При необходимости разработчик модуля может явно указать какие объекты нужно
# импортировать при использовании стиля from module import *. Для этого
# используется магическая переменная __all__ (два нижних подчёркивания до, слово
# all и два нижних подчёркивания после). Изменим код модуля super_module.py,
# добавив строку с __all__
#
# Файл super_module.py
# from random import randint
#
# __all__ = ['func', '_secret']
# SIZE = 100
# _secret = 'qwerty'
# __top_secret = '1q2w3e4r5t6y'
# def func(a: int, b: int) -> str:
# z = f'В диапазоне от {a} до {b} получили {randint(a, b)}'
# return z
# result = func(1, 6)
# Переменной __all__ присваивается список имён объектов, заключённых в кавычки,
# т.е. str типа. В основной модуль попадут только указанные в списке имена,
# независимо от того являются они публичными, защищёнными или приватными. При
# этом объект должен быть глобальным. Если указать в списке имя локального
# объекта, например переменную z — локальную переменную функции func, получим
# ошибку.
# Список __all__ в приведённом примере используется для формирования списка
# импортируемых объектов модуля. Кроме этого __all__ применяется для импорта
# модулей из пакета. Рассмотрим вариант импорта модулей из пакета далее на
# лекции.