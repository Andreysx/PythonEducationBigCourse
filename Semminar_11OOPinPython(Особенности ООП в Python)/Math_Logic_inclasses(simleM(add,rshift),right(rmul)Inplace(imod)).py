# 4. Математика и логика в классах
# Под математикой стоит понимать переопределение дандер методов, которые
# позволяют производить операции сложения, вычитания, умножения и т.п. с
# использованием математических символов. Что касается логики, речь идёт о
# логических операциях “и”, “или” и т.п. над объектами.
#
#
# Рассмотрим возможности
# Python в таблице.
# Операция в
# Python
#            Основной метод         Right метод                      In place метод
# +        __add__(self, other)        __radd__(self, other)         __iadd__(self, other)
# -        __sub__(self, other)        __rsub__(self, other)         __isub__(self, other)
# *        __mul__(self, other)        __rmul__(self, other)         __imul__(self, other)
# @        __matmul__(self, other)     __rmatmul__(self, other)      __imatmul__(self, other)
# /        __truediv__(self, other)    __rtruediv__(self, other)     __itruediv__(self, other)
# //       __floordiv__(self, other)   __rfloordiv__(self, other)    __ifloordiv__(self, other)
# %        __mod__(self, other)        __rmod__(self, other)         __imod__(self, other)
# divmod() __divmod__(self, other)     __rdivmod__(self, other)      __idivmod__(self, other)
# **, pow() __pow__(self, other[,modulo]) __rpow__(self, other[,modulo]) __ipow__(self, other[,modulo])
# <<       __lshift__(self, other)      __rlshift__(self, other)     __ilshift__(self, other)
# >>       __rshift__(self, other)      __rrshift__(self, other)     __irshift__(self, other)
# &        __and__(self, other)         __rand__(self, other)        __iand__(self, other)
# ^        __xor__(self, other)         __rxor__(self, other)        __ixor__(self, other)
# |        __or__(self, other)          __ror__(self, other)         __ior__(self, other)
#
#
#
# Переопределение перечисленных в таблице методов позволяет использовать
# указанные в первом столбце операции для вычисления результата. Рассмотрим
# некоторые из них на примерах.
#
#
#
#
#
# Обычные методы
# Начнём с методов из второго столбца. Если Python встречает два экземпляра класса
# с одним из знаков между ними, ищется соответствующий знаку дандер метод для
# вызовы. Если метод не определён, возвращается ошибка. При этом метод должен
# возвращать новый экземпляр класса без изменения исходных.
# Сложение через __add__
#
# Создадим класс вектор и научим вектора складываться.
#
# class Vector:
#
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#     def __repr__(self):
#         return f'Vector({self.x}, {self.y})'
#
#     def __add__(self, other):
#         x = self.x + other.x
#         y = self.y + other.y
#         return Vector(x, y)
#
#
# a = Vector(2, 4)
# b = Vector(3, 7)
# c = a + b
# print(f'{a = }\t{b = }\t{c = }')
#
# Помимо уже привычных методов __init__ и __repr__ определили метод __add__. В
# предпоследней строке пытаемся сложить вектора. Без метода __add__ получили бы
# ошибку вида: TypeError: unsupported operand type(s) for +: 'Vector' and 'Vector'.
# В самом методе используем два параметра — self для обращения к элементам
# экземпляра и other для обращения к элементам другого объекта, стоящего справа
# от знака плюс. Получив значения x, y для нового вектора метод возвращает его -
# новый экземпляр класса Vector.
#
#
#
#
#
# Сдвиг вправо, __rshift__
# Переопределение методов не обязательно должно быть для чисел. Напишем класс,
# который генерирует шкаф с одеждой и выбрасывает указанное количество вещей
# при правом сдвиге. Не забудем, что дандер метод должен возвращать новый
# экземпляр.
#
# from random import choices
#
#
# class Closet:
#
#     CLOTHES = ('брюки', 'рубашка', 'костюм', 'футболка',
#     'перчатки', 'носки', 'туфли')
#     def __init__(self, count: int, storeroom=None):
#         self.count = count
#         if storeroom is None:
#             self.storeroom = choices(self.CLOTHES, k=count)
#         else:
#             self.storeroom = storeroom
#
#     def __str__(self):
#         names = ', '.join(self.storeroom)
#         return f'Осталось вещей в шкафу {self.count}:\n{names}'
#
#     def __rshift__(self, other):
#         shift = self.count if other > self.count else other
#         self.count -= shift
#         return Closet(self.count, choices(self.storeroom, k=self.count))
#
# storeroom = Closet(10)
# print(storeroom)
#
# for _ in range(4):
#     storeroom = storeroom >> 3
#     print(storeroom)
#
# Константа CLOTHES хранит доступный список одежды. Из него будем выбирать
# count предметов. Внутри __rshift__ сделали проверку на оставшееся количество
# вещей, чтобы не выбросить больше, чем уже имеется. Метод возвращает новый
# экземпляр, где count уменьшился на сдвиг, а второй аргумент содержит выборку из
# уже лежащих в шкафу вещей.
# Создав экземпляр на 10 вещей и последовательно удаляем по три предмета в
# цикле. Но уйти в минус не удаётся, отрабатывает наша защита.
#
#
#
#
#
#
#
# Right методы
# Right методы срабатывают в том случае, если у левого аргумента в выражении
# метод не был найден. Например при записи x + y вначале производится поиска
# дандер метода x.__add__. Если он не найден, вызываем y.__radd__.
# Умножение текста на “продвинутый текст”
# методом __rmul__
# Создадим класс на основе str с методом __rmul__. Если слева оказывается обычная
# строка, будем между словами добавлять текст из “продвинутой строки”,
# перемножим их.
#
# class StrPro(str):
#
#     def __new__(cls, *args, **kwargs):
#         instance = super().__new__(cls, *args, **kwargs)
#         return instance
#
#     def __rmul__(self, other: str):
#         words = other.split()
#         result = self.join(words)
#         return StrPro(result)
#
# text = 'Каждый охотник желает знать где сидит фазан'
# s = StrPro(' (=^.^=) ')
# print(f'{text = }\n{s = }')
# print(text * s)
# print(s * text) # TypeError: 'str' object cannot be interpreted as an integer
# Метод __new__ позволили нам наследоваться от класса str и забрать все свойства и
# методы, определённые в нём. Мы добавили лишь __rmul__ где делим строку
# стоящую слева от знака умножить - other на отдельные слова. Далее собираем
# новую строку с добавление self- строки справа от знака умножения.
# При умножении str на StrPro получаем ожидаемый результат. Если же поменять
# значения местами, получаем ошибку. Обычную строку можно умножить на целое
# число, но не другой экземпляр.
#
#
#
#
#
#
# In place методы
# In place методы используются при короткой записи математического символа
# слитно со знаком равенства: a += b. Такая запись подразумевает внесение
# изменений в исходный объект, а не возврат нового экземпляра. Возвращать надо
# самого себя — self.
# Вычисление процентов вместо нахождения
# остатка от деления, __imod__
# Создадим простой класс Money, который будет увеличивать значение на указанный
# процент при записи Money %= float | int
#
# from decimal import Decimal
#
#
# class Money:
#
#     def __init__(self, value: int | float):
#         self.value = Decimal(value)
#
#     def __repr__(self):
#         return f'Money({self.value:.2f})'
#
#     def __imod__(self, other):
#         self.value = self.value * Decimal(1 + other / 100)
#         return self
#
#
# m = Money(100)
# print(m)
# m %= 50
# print(m)
# m %= 100
# print(m)
#
# Для точности вычислений используется класс Decimal. Поэтому при увеличении на
# указанный процент используем дополнительное обёртывание правого значение в
# Decimal.
# 🔥 Важно! Не забывайте return self при работе с in place дандер методами.
# Задание
# Перед вами несколько строк кода. Напишите что выведет программа, не запуская
# код. У вас 3 минуты. Класс склеит 2 кортежа
#
#
# class MyClass:
#
#     def __init__(self, data):
#         self.data = data
#
#     def __and__(self, other):
#         return MyClass(self.data + other.data)
#
#     def __str__(self):
#         return str(self.data)
#
# a = MyClass((1, 2, 3, 4, 5))
# b = MyClass((2, 4, 6, 8, 10))
# print(a & b)
