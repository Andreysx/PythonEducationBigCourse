# 6. Обработка атрибутов
# Python имеет четыре дандер метода, которые позволяют контролировать
# обращения к атрибутом экземпляра. Разберём их на простом примере класса
# вектор.
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
#
#
#
#
#
# Получение значения атрибута,__getattribute__
# Дандер __getattribute__ вызывается при любой попытке обращения к атрибутам
# экземпляра.
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
#     def __getattribute__(self, item):
#         if item == 'z':
#             raise AttributeError('У нас вектор на плоскости, а не в пространстве')
#         return object.__getattribute__(self, item)
#
# a = Vector(2, 4)
# print(a.z) # AttributeError: У нас вектор на плоскости, а не в пространстве
# print(f'{a = }')
#
# В параметр item попадает имя атрибута, к которому пытаются обратиться в виде str.
# Мы прописали проверку имён и если это третья координата z, вызываем ошибкуAttributeError.
# 🔥 Важно! Строка return object.__getattribute__(self, item) является
# обязательной. Без неё может возникнуть ошибка переполнения стека.
#
#
#
#
#
# Присвоение атрибуту значения, __setattr__
# Дандер __setattr__ срабатывает каждый раз, когда в коде есть операция
# присвоения. Слева от знака равно экземпляр со свойством - key, справа значение -value.
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
#     def __getattribute__(self, item):
#         if item == 'z':
#             raise AttributeError('У нас вектор на плоскости, а не в пространстве')
#         return object.__getattribute__(self, item)
#
#     def __setattr__(self, key, value):
#         if key == 'z':
#             raise AttributeError('У нас вектор на плоскости, а не в пространстве')
#         return object.__setattr__(self, key, value)
#
#
# a = Vector(2, 4)
# print(a.z) # AttributeError: У нас вектор на плоскости, а не в пространстве
# print(f'{a = }')
# a.z = 73 # AttributeError: У нас вектор на плоскости, а не в пространстве
# a.x = 3
# print(f'{a = }')
#
# Дандер __setattr__ запрещает присваивать значение свойству . Как и в случае с
# __getattribute__ важная последняя строка. Она позволяет избежать рекурсии и
# присвоить значение свойству, которое мы не обработали ранее.
#
#
#
#
#
#
# Обращение к несуществующему атрибуту,
# __getattr__
# Если свойство отсутствует, в первую очередь вызывается дандер __getattribute__. В
# случае возврата им ошибки AttributeError вызывается метод __getattr__. Он также
# может поднять ошибку. А может как-то иначе обработать запрос.
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
#     def __getattribute__(self, item):
#         if item == 'z':
#             raise AttributeError('У нас вектор на плоскости, а не в пространстве')
#         return object.__getattribute__(self, item)
#
#     def __setattr__(self, key, value):
#         if key == 'z':
#             raise AttributeError('У нас вектор на плоскости, а не в пространстве')
#         return object.__setattr__(self, key, value)
#
#     def __getattr__(self, item):
#         return None
#
#
# a = Vector(2, 4)
# print(a.z) # None
# print(f'{a = }')
#
# Мы пропасила возврат None для любого свойства, которое не удалось найти. Метод
# возвращает None и для свойства z, перехватывая исключение.
#
#
#
#
#
# Удаление атрибута, __delattr__
# При попытке удалить атрибут командой del можно использовать дандер __delattr__
# для изменения логики.
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
#     def __getattribute__(self, item):
#         if item == 'z':
#             raise AttributeError('У нас вектор на плоскости, а не в пространстве')
#         return object.__getattribute__(self, item)
#
#     def __setattr__(self, key, value):
#         if key == 'z':
#             raise AttributeError('У нас вектор на плоскости, а не в пространстве')
#         return object.__setattr__(self, key, value)
#
#     def __getattr__(self, item):
#         return None
#
#     def __delattr__(self, item):
#         if item in ('x', 'y'):
#             setattr(self, item, 0)
#         else:
#             object.__delattr__(self, item)
#
#
# a = Vector(2, 4)
# a.s = 73
# print(f'{a = }, {a.s = }')
# del a.x
# del a.s
# print(f'{a = }, {a.s = }')
#
#
# В нашем классе при попытке удалить икс или игрек, значение не удаляется. Вместо
# этого свойству присваивается ноль.
# Обратите внимание на свойство s. Мы смогли присвоить ему значение 73. Дандер
# __setattr__ контролирует только имя z. При удалении свойства z сработала ветка
# else и свойство было удалено. Однако мы не получили ошибки, обращаясь к
# несуществующему свойству, сработал дандер __getattr__.
# Функции setattr(), getattr() и delattr()
# В примере выше мы вызвали функцию setattr для присвоение у объекта self
# свойству item значения 0. В Python есть функции, которые позволяют делать тоже
# самое, что и рассмотренные выше дандер методы. Разница лишь в том, что метод
# реагирует на событие в коде, а функцию вы вызываете в тот момент, когда вам это
# нужно.
# ● setattr(object, name, value) — аналог object.name = value
# ● getattr(object, name[, default]) — аналог object.name or default
# ● delattr(object, name) — аналог del object.name
#
# Вывод
# На этой лекции мы:
# 1. Разобрались с созданием и удалением классов
# 2. Узнали о документировании классов
# 3. Изучили способы представления экземпляров
# 4. Узнали о возможностях переопределения математических операций
# 5. Разобрались со сравнением экземпляров
# 6. Узнали об обработке атрибутов
# Краткий анонс следующей лекции
# 1. Разберёмся в превращении объекта в функцию
# 2. Изучим способы создания итераторов
# 3. Узнаем о создании менеджеров контекста
# 4. Разберемся в превращении методов в свойства
# 5. Изучим работу дескрипторов
# 6. Узнаем о способах экономии памяти