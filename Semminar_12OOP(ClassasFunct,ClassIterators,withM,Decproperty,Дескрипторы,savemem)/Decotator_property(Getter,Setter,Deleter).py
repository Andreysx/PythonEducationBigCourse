# 4. Декоратор @property
# На прошлой лекции мы работали с классом треугольник и пометили его свойства
# защищёнными, добавив символ подчёркивания в начале имени. Но что если доступ
# к свойству нужен. Хотя бы на чтение. Для этого отлично подойдёт функция
# декоратор property(). Рассмотрим на более простом и коротком примере.
#
# class User:
#     def __init__(self, name):
#         self._name = name
#
#     @property
#     def name(self):
#         return self._name
#
#
# user = User('Стивен')
# print(f'{user.name = }')
# user.name = 'Славик' # AttributeError: can't set attribute 'name'
#
#
# Класс User получает имя пользователя и сохраняет его в защищённой переменной
# экземпляра _name.
# Далее создали метод name который возвращает значение из защищённого
# свойства _name. К методу применён декоратор property. Теперь Python
# воспринимает name не как имя вызываемого метода, а как название свойства.
# При обращении к свойству name получаем результат — имя пользователя. Если же
# сделать попытку на изменение свойства, получим ошибку.
#
#
#
# ● Getter
# Декоратор property позволяет создавать “геттеры”. Это методы, которые выдают
# себя за свойства, позволяют прочитать результат, но блокируют возможность
# записи. Рассмотрим другой пример “геттера”.
# class User:
#     def __init__(self, first_name, last_name):
#         self.first_name = first_name
#         self.last_name = last_name
#
#     @property
#     def full_name(self):
#         return f'{self.first_name} {self.last_name}'
#
#
# user = User('Стивен', 'Спилберг')
# print(f'{user.first_name = }\n{user.last_name = }\n{user.full_name = }')
# user.full_name = 'Стивен Хокинг' # AttributeError: can't set attribute 'full_name'
# user.last_name = 'Хокинг'
# print(f'{user.first_name = }\n{user.last_name = }\n{user.full_name = }')
#
#
# Теперь у пользователя есть два публичных свойства для имени и фамилии. Кроме
# того есть свойство (а не метод) для вывода полного имени, т.е. с фамилией. Все три
# свойства работают на чтение. А вот перезаписать полное имя мы не можем. Зато
# ничего не мешает изменить фамилию и получить обновлённое полное имя.
#
#
#
#
# ● Setter
# Python позволяет к “геттеру” добавить “сеттер” — метод контролирующий
# изменение свойства. Добавим пользователю возраст и будем контролировать
# чтобы новый возраст был больше старого. Например мы вручную обновляем
# данные раз в 5-10 лет.
# class User:
#     def __init__(self, first_name, last_name):
#         self.first_name = first_name
#         self.last_name = last_name
#         self._age = 0
#
#     @property
#     def full_name(self):
#         return f'{self.first_name} {self.last_name}'
#
#     @property
#     def age(self):
#         return self._age
#
#     @age.setter
#     def age(self, value):
#         if value > self._age:
#             self._age = value
#         else:
#             raise ValueError(f'Новый возраст должен быть больше текущего: {self._age}')
#
#
# user = User('Стивен', 'Спилберг')
# user.age = 75
# print(f'Меня зовут {user.full_name} и мне {user.age} лет.')
# print('Прошёл один год.')
# user.age = 76
# print(f'Меня зовут {user.full_name} и мне {user.age} лет.')
# print('Прошло несколько лет. Изобретена технология омоложения. Но возраст она не уменьшает.')
# user.age = 25 # ValueError: Новый возраст должен быть большетекущего: 76
#
# Что получилось:
# 1. защёщенное свойство _age получает значение ноль при рождении
# экземпляра, в дандер __init__
# 2. используя декоратор property создали свойство age для чтения текущего
# возраста
# 3. создаём “сеттер” для контроля записи новых значений в свойство _age
# ➢ применяем декоратор @age.setter. Имя между @ и точкой должно
# совпадать с именем “геттера”.
# ➢ методу присваиваем такое же имя как и у свойства и он должен
# принимать значения помимо self
# ➢ внутри метода делаем проверку на увеличения возраста
# ➢ если возраст увеличивается, обновляем свойство _age
# ➢ если возраст не увеличился вызываем ошибку ValueError и сообщаем
# её причину
# 4. В основном коде запросто увеличиваем возраст пользователя, но не можем
# его уменьшить.
# При создании “сеттера” не обязательно вызывать ошибки. В целом внутри может
# быть прописана любая логика. Например вы работает с финансовой программой и
# присваиваете новую сумму денег. “Сеттер” будет приводить сумму к типу Decimal
# перед присваиванием.
#
#
#
#
#
# ● Deleter
# Помимо “геттера” и “сеттера” можно создать “делейтер”. Он выполняется при
# вызове команды del для свойства. Один из возможных вариантов использования
# “делейтера” - заменять значение на какое-то по умолчанию или помечать элемент
# скрытым вместо удаления.
# class User:
#     def __init__(self, first_name, last_name):
#         self.first_name = first_name
#         self.last_name = last_name
#         self._age = 0
#
#     @property
#     def full_name(self):
#         return f'{self.first_name} {self.last_name}'
#
#     @property
#     def age(self):
#         return self._age
#
#     @age.setter
#     def age(self, value):
#         if value > self._age:
#             self._age = value
#         else:
#             raise ValueError(f'Новый возраст должен быть больше текущего: {self._age}')
#
#     @age.deleter
#     def age(self):
#         self._age = 0
#
#
# user = User('Стивен', 'Спилберг')
# user.age = 75
# print(f'Меня зовут {user.full_name} и мне {user.age} лет.')
# print('Прошло много лет. Изобретена технология перерождения.')
# del user.age
# print(f'Меня зовут {user.full_name} и мне {user.age} лет.')
#
# Создание “делейтера” аналогично “сеттеру”. Также используется декоратор с
# именем свойства, но после точки пишем deleter. Внутри метода прописываются
# действия для удаления.
#
#
#
#
# Антипаттерн геттера, сеттера, делейтера
# Представленный ниже код является кодам ради кода и не имеет смысла в языке
# Python. Избегайте подобного. И да, код работает верно. Просто он не делает ничего
# нового.
# class BadPattern:
#     def __init__(self, x):
#         self._x = x
#
#     @property
#     def x(self):
#         return self._x
#
#     @x.setter
#     def x(self, value):
#         self._x = value
#
#     @x.deleter
#     def x(self):
#         del self._x
# Все три декоратора ничего не делают. Подобный код в Python должен выглядеть
# так, без защиты переменной x
# class GoodPattern:
#     def __init__(self, x):
#         self.x = x
#
#
#
#
# Задание
# Перед вами несколько строк кода. Напишите что выведет программа, не запуская
# код. У вас 3 минуты.
# class MyCls:
#     def __init__(self, first_name, last_name):
#         self.first_name = first_name
#         self.last_name = last_name
#
#     @property
#     def full_name(self):
#         return self.first_name + ' ' + self.last_name
#
#     @full_name.setter
#     def full_name(self, value: str):
#         self.first_name, self.last_name, _ = value.split()
#
#
# x = MyCls('Стивен', 'Хокинг')
# print(x.full_name)
# x.full_name = 'Гвидо ван Россум'
# print(x.full_name)
