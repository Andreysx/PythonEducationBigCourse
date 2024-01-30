# 4. Создание собственных исключений
# В финале пару примеров создания собственных исключений. Попробуем для класса
# User из прошлого примера создать свои исключения.
# Писать код исключений будем в отдельном файле error.py Начнём с того, что
# создадим своё собственное базовое исключение. От него будут наследоваться
# остальные наши исключения. Родительское исключение займёт пару строк кода
#
#
# class UserException(Exception):
#     pass
# А теперь добавим исключения для ошибок имени и возраста пользователя. Пока это
# будут исключения на минималках.
# class UserAgeError(UserException):
#     pass
# class UserNameError(UserException):
#     pass
# Теперь внесём правки в код инициализации пользователя. Заодно избавимся от
# магических чисел для минимальной и максимальной длины имени.
#
# from error import UserNameError, UserAgeError
#
#
# class User:
#     MIN_LEN = 6
#     MAX_LEN = 30
#     def __init__(self, name, age):
#         if self.MIN_LEN < len(name) < self.MAX_LEN:
#             self.name = name
#         else:
#             raise UserNameError
#         if not isinstance(age, (int, float)) or age < 0:
#             raise UserAgeError
#         else:
#             self.age = age
#
#
# user = User('Яков', '-12')
#
#
# Подобный код отлично справляется с поставленной задачей. Но стал менее
# информативен в случае возникновения ошибок.
# error.UserNameError
# Понятно, что ошибка в имени. Но не очень информативно. Исправим ситуацию.
# Методы __init__ и __str__ в классах своих
# исключений
# Чтобы исключение давало подробную информацию об ошибке, будем передавать
# ему проблемную переменную. Класс User доработаем в строках подъёма ошибок.
#
# from error import UserNameError, UserAgeError
#
# class User:
#     def __init__(self, name, age):
#         if 6 < len(name) < 30:
#             self.name = name
#         else:
#             raise UserNameError(name)
#         if not isinstance(age, (int, float)) or age < 0:
#             raise UserAgeError(age)
#         else:
#             self.age = age
#
#
# user = User('Яков', '-12')
#
#
# Благодаря наследованию переданные в исключение переменные могут выводится
# в тексте ошибки.
# raise UserNameError(name)
# error.UserNameError: Яков
# Уже лучше. Но без пары дандер методов в классах ошибок пока не идеально.
# Дорабатываем код в файле error.
#
# class UserException(Exception):
#     pass
#
# class UserAgeError(UserException):
#     def __init__(self, value):
#         self.value = value
#     def __str__(self):
#         return f'Возраст пользователя должен быть целым int() иливещественным float() больше нуля.\n' \
# f'У вас тип {type(self.value)}, а значение {self.value}'
#
#
# class UserNameError(UserException):
#     def __init__(self, name, lower, upper):
#         self.name = name
#         self.lower = lower
#         self.upper = upper
#
#     def __str__(self):
#         text = 'попадает в'
#         if len(self.name) < self.lower:
#             text = 'меньше нижней'
#         elif len(self.name) > self.lower:
#             text = 'больше верхней'
#         return f'Имя пользователя {self.name} содержит{len(self.name)} символа(ов).\n' \
#         f'Это {text} границы. Попадите в диапазон({self.lower}, {self.upper}).'
#
#
# В случае с возрастом просто получаем текущее значение в переменную value. Далее
# выводим информацию об ошибке без явного уточнения проблемы. Просто
# сообщаем о допустимых типе и значении, а также выводим переданное значение и
# его тип.
# При обработки ошибки имении дополнительно принимаем в инициализацию
# граничные значения длины. Переменная text внутри дандер __str__ получает
# значение в зависимости от границы: “меньше нижней” или “больше верхней”.
# Вывод точно указывает на то, в какую из границ мы не попали.
# 20
# 🔥 Внимание! В классе User надо исправит строку вызова ошибки имени,
# чтобы код сработал верно. Иначе исключение вернёт нам исключение
# TypeError: UserNameError.__init__() missing 2 required positional arguments:
# 'lower' and 'upper'
# ...
# def __init__(self, name, age):
#     if self.MIN_LEN < len(name) < self.MAX_LEN:
#         self.name = name
#     else:
#      raise UserNameError(name, self.MIN_LEN, self.MAX_LEN)
# ...
# Вывод
# На этой лекции мы:
# 1. Разобрались с обработкой ошибок в Python
# 2. Изучили иерархию встроенных исключений
# 3. Узнали о способе принудительного поднятия исключения в коде
# 4. Разобрались в создании собственных исклю