# 3. Наследование
# В Python все объекты являются наследниками класса object. В начале лекции мы
# рассмотрели пример создания класса:
# class Person:
#     pass
# Представленная запись создания класса является упрощённой. На самом деле
# класс Person наследуется от класса object. Т.е. object — родительский класс для
# Person, а Person — дочерний класс для object.
# class Person(object):
#     pass
# 🔥 Важно! Наследование от object принято опускать при создании класса.
# Создадим класс героя на основе класса персонажа.
# class Person:
#
#     __max_up = 3
#     _max_level = 80
#
#     def __init__(self, name, race='unknown', speed=100):
#         self.name = name
#         self.race = race
#         self.level = 1
#         self.health = 100
#         self._speed = speed
#         self.up = 3
#
#     def _check_level(self):
#         return self.level < self._max_level
#
#     def level_up(self):
#         if self._check_level():
#             self.level += 1
#
#     def change_health(self, other, quantity):
#         self.health += quantity
#         other.health -= quantity
#
#     def add_up(self):
#         self.up += 1
#         self.up = min(self.up, self.__max_up)
#
#
# class Hero(Person):
#     def __init__(self, power, *args, **kwargs):
#         self.power = power
#         super().__init__(*args, **kwargs)
#
#
# p1 = Hero('archery', 'Сильвана', 'Эльф', 120)
# print(f'{p1.name = }, {p1.up = }, {p1.power = }')
# Класс Person мы не изменяли. Он перенесён из главы про инкапсуляцию. Далее мы
# создаём класс Hero и указываем в скобках класс Person. Герой - дочерний класс для
# персонажа. Мы хотим добавить герою свойство power и прописываем его в методе
# инициализации. Далее вызываем метод super().__init__, т.е. метод инициализации
# родительского класса. Без такого вызова не будут созданы атрибуты родительского
# класса.
# Теперь при создании экземпляра класса Hero мы вначале передаём его аргументы,
# а далее аргументы родительского класса Person.
# Переопределение методов
# При наследовании мы можем использовать в дочернем классе все общедоступные
# свойства и методы родительского класса. Кроме того можно создать свои. И если
# имена будут совпадать, произойдёт переопределение. Будут браться значения
# дочернего класса.
# class Person:
#     ...
#
#
# class Hero(Person):
#     def __init__(self, power, *args, **kwargs):
#         self.power = power
#         super().__init__(*args, **kwargs)
#
#     def change_health(self, other, quantity):
#         self.health += quantity * 2
#         other.health -= quantity * 2
#
#     def add_many_up(self):
#         self.up += 1
#         self.up = min(self.up, self._Person__max_up * 2)
#
# p1 = Hero('archery', 'Сильвана', 'Эльф', 120)
# p2 = Person('Маг', 'Тролль')
# print(f'{p1.health = }, {p2.health = }')
# p1.change_health(p2, 10)
# print(f'{p1.health = }, {p2.health = }')
# p2.change_health(p1, 10)
# print(f'{p1.health = }, {p2.health = }')
# p1.add_many_up()
# print(f'{p1.up = }')
#
# В примере создан метод change_health с дополнительным множителем. Он
# срабатывает у героя. Но при вызове метода у экземпляра класса Person
# срабатывает старый метод.
# В методе add_many_ups для обхода инкапсуляции используем запись
# self._Person__max_up. Экземпляр обращается к приватному атрибуту родительского
# класса, напрямую указав его.
#
#
# Множественное наследование
# Python поддерживает множественное наследование. Класс может быть
# наследником сразу двух и более классов. В некоторых языках множественное
# наследование недоступно по причине усложнения кода. Например наследуя класс
# существо от классов птицы и рыбы позволит создать летающую рыбу или
# плавающую птицу?
# Рассмотрим вариант множественного наследования.
#
# class Person:
#     __max_up = 3
#     _max_level = 80
#     def __init__(self, name, race='unknown', speed=100):
#         self.name = name
#         self.race = race
#         self.level = 1
#         self.health = 100
#         self._speed = speed
#         self.up = 3
#
#     def _check_level(self):
#         return self.level < self._max_level
#
#     def level_up(self):
#         if self._check_level():
#             self.level += 1
#
#     def change_health(self, other, quantity):
#         self.health += quantity
#         other.health -= quantity
#
#     def add_up(self):
#         self.up += 1
#         self.up = min(self.up, self.__max_up)
#
#
# class Address:
#     def __init__(self, country, city, street):
#         self.country = country or ''
#         self.city = city or ''
#         self.street = street or ''
#
#     def say_address(self):
#         return f'Адрес героя: {self.country}, {self.city},{self.street}'\
#
#
# class Weapon:
#     def __init__(self, left_hand, right_hand):
#         self.left_hand = left_hand or 'Клинок'
#         self.right_hand = right_hand or 'Лук'
#
#
# class Hero(Person, Address, Weapon):
#     def __init__(self, power, name=None, race=None, speed=None,
#     country=None, city=None, street=None,
#     left_hand=None, right_hand=None):
#         self.power = power
#         Person.__init__(self, name, race, speed)
#         Address.__init__(self, country, city, street)
#         Weapon.__init__(self, left_hand, right_hand)
#
#     def change_health(self, other, quantity):
#         self.health += quantity * 2
#         other.health -= quantity * 2
#
#     def add_many_ups(self):
#         self.up += 1
#         self.up = min(self.up, self._Person__max_up * 2)
#
#
# p1 = Hero('archery', 'Сильвана', 'Эльф', 120,
# country='Эльфляндия', street='Ночного эльфа',
# left_hand='Стрела')
# print(f'{p1.say_address()}')
# print(f'{p1.right_hand = }, {p1.left_hand = }')
#
# Мы создали классы Address и Weapon. Добавив их к нашему герою, получаем
# сочетание атрибутов и методов всех перечисленных классов. Обратите внимание на
# то как происходит инициализация родительских классов внутри Hero __init__.
# Прописали все параметры из родительских классов в инициализации класса Hero.
# Далее вручную распределяем аргументы между методами __init__ каждого из
# родительских классов. Подобный приём не лучшая практика. При изменении
# параметров у родительских классов, дочерние могут перестать работать. При
# простых реализациях наследования достаточно функции super(). Обычно не стоит
# усложнять код до того состояния, когда внутренние механизмы не справляются с
# наследованием.
#
#
#
# MRO
# Аббревиатура MRO — method resolution order переводится как “порядок разрешения
# методов”. Относится этот порядок не только к методам, но и ко всем атрибутам
# класса. Это внутренний механизм, определяющий порядок наследования.
# Забегая вперёд, иногда механизм не справляется с задачей. И чаще всего это
# говорит о сложности кода и неверной логики построения наследования. Т.е.
# нерабочий механизм наследования намекает разработчику на проблемы в его коде.
# Рассмотрим работу MRO на нескольких простых классах.
# class A:
#     def __init__(self):
#         print('Init class A')
#         self.data_a = 'A'
#
#
# class B:
#     def __init__(self):
#         print('Init class B')
#         self.data_b = 'B'
#
#
# class C:
#     def __init__(self):
#         print('Init class C')
#         self.data_c = 'C'
#
#
# class D:
#     def __init__(self):
#         print('Init class D')
#         self.data_d = 'D'
#
#
# class X1(A, C):
#     def __init__(self):
#         print('Init class X1')
#         super().__init__()
#
#
# class X2(B, D):
#     def __init__(self):
#         print('Init class X2')
#         super().__init__()
#
#
# class X3(A, D):
#     def __init__(self):
#         print('Init class X3')
#         super().__init__()
#
#
# class Z(X1, X2, X3):
#     def __init__(self):
#         print('Init class Z')
#         super().__init__()
#
#
# print(*Z.mro(), sep='\n')
#
#
# 1. Четыре класса A, B, C, D не имеют родительского класса. Точнее они
# наследуются от прародителя object. У каждого из классов есть по параметру.
# 2. Далее три класса X имеют по два родительских класса.
# 3. В финале класс Z наследуется от трёх классов X.
# У каждого класса добавили текстовый вывод при вызове методу __init__. Также
# обратите внимание на наличие функции super, которая вызывает инициализацию
# родительского класса.
# На схеме наследование будет выглядеть так:
# У каждого класса есть метод mro, который вычисляет порядок наследования. Он
# отвечает за инициализацию каждого класса один раз в порядке слева направо и по
# старшинству, т.е. родитель не может быть инициализирован раньше дочернего
# класа.. Подробнее про то как работает “монотонная линеаризация суперкласса”
# можно прочитать по ссылке.
# Разберём результат работы mro с нашим классом Z.
# ● В первую очередь отрабатывает инициализация самого класса.
# ● Далее начинаем двигаться слева направо по списку родительских классов:
# X1, X2
# ● Следующим будет класс B. Почему он, а не X3? Класс B является
# родительским только для класса X2. Так мы не нарушаем порядок слева
# направо и старшинство.
# ● Следующим инициализируется X3, последний из родительских классов у Z.
# 23
# ● Далее идёт инициализация класса A. Он родитель для X1 и X3. Следовательно
# его инициализация была невозможна раньше дочерних классов.
# ● Классы С и D инициализируются последними, они правее A, B и С в списке
# родительских классов у “иксов”.
# ● Класс object всегда инициализируется в последнюю очередь.
# Поиск аргументов и методов в экземпляре класса Z будет происходить в порядке,
# представленном методом mro.
# Добавим несколько строк кода и посмотрим на результат:
# z = Z()
# print(f'{z.data_b = }')
# print(f'{z.data_a = }') # AttributeError: 'Z' object has no
# attribute 'data_a'
# Вызов метода __init__ остановился на классе B. Мы не дописали ему вызов super,
# считая что он и так не имеет наследников. В результате аргумент data_a не был
# создан в экземпляре класса z. Попробуем описать классу A дополнительный метод.
# class A:
#     def __init__(self):
#         print('Init class A')
#         self.data_a = 'A'
#
#     def say(self):
#         print('Текст')
#         print(self.data_b)
# ...
# z = Z()
# z.say()
# Вызов метода say из класса A отработал без ошибок. Мы нашли его двигаясь по
# цепочке линеаризации. При этом метод даже смог обратиться к свойству другого
# класса. Связано это с тем, что мы работаем из экземпляра класса Z и он собрал в
# себя аргументы и методы наследуемых классов.
# 🔥 Важно! Не стоит из родительских классов обращаться к аргументам и
# методам дочерних классов или классов того же уровня наследования.
#
# Задание
# Перед вами несколько строк кода. Напишите что выведет программа, не запуская
# код. У вас 3 минуты.
# class A:
#     name = 'A'
#     def call(self):
#         print(f'I am {self.name}')
#
#
# class B:
#     name = 'B'
#     def call(self):
#         print(f'I am {self.name}')
#
#
# class C:
#     name = 'C'
#     def call(self):
#         print(f'I am {self.name}')
#
#
# class D(C, A):
#     pass
#
#
# class E(D, B):
#     pass
#
#
# e = E()
# e.call()