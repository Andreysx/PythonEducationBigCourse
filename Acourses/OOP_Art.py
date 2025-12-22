# class Stack:
#     def __init__(self):
#         self.values = []
#
#     def push(self, item):
#         self.values.append(item)
#
#     def pop(self):
#         if self.is_empty():
#             print('Empty Stack')
#         else:
#             return self.values.pop()
#
#     def peek(self):
#         if self.is_empty():
#             print('Empty Stack')
#             return None
#         else:
#             return self.values[-1]
#
#     def is_empty(self):
#         return len(self.values) == 0
#
#     def size(self):
#         return len(self.values)
#
#
# s = Stack()
# assert s.values == []
# assert isinstance(s, Stack)
#
# s.peek()  # распечатает 'Empty Stack'
# assert s.is_empty() is True
# s.push('cat')
# assert s.size() == 1
# assert s.peek() == 'cat'
#
# s.push('dog')
# assert s.size() == 2
# assert s.peek() == 'dog'
#
# s.push(True)
# assert s.size() == 3
# assert s.is_empty() is False
#
# s.push(777)
# assert s.size() == 4
#
# assert s.pop() == 777
# assert s.size() == 3
#
# assert s.pop() is True
# assert s.size() == 2
#
# s.push(123)
# s.push(123456)
# assert s.peek() == 123456
# assert s.size() == 4
#
# assert s.pop() == 123456
# assert s.pop() == 123
# assert s.pop() == 'dog'
# assert s.is_empty() is False
# assert s.pop() == 'cat'
# assert s.is_empty() is True
#
# d = Stack()
# assert d.peek() is None  # Печатает "Empty Stack"
# assert d.pop() is None  # Печатает "Empty Stack"
# d.push('hello')
# assert d.size() == 1
# d.push('world')
# assert d.size() == 2
# assert d.peek() == 'world'
# assert d.pop() == 'world'
# assert d.peek() == 'hello'
# print('Good')
import math
import string
from typing import List

#
# class Worker:
#     def __init__(self, name, salary, gender, passport):
#         self.name = name
#         self.salary = salary
#         self.gender = gender
#         self.passport = passport
#
#     def get_info(self):
#         print(f"Worker {self.name}; passport-{self.passport}")
#
#
# persons = [
#     ('Allison Hill', 334053, 'M', '1635644202'),
#     ('Megan Mcclain', 191161, 'F', '2101101595'),
#     ('Brandon Hall', 731262, 'M', '6054749119'),
#     ('Michelle Miles', 539898, 'M', '1355368461'),
#     ('Donald Booth', 895667, 'M', '7736670978'),
#     ('Gina Moore', 900581, 'F', '7018476624'),
#     ('James Howard', 460663, 'F', '5461900982'),
#     ('Monica Herrera', 496922, 'M', '2955495768'),
#     ('Sandra Montgomery', 479201, 'M', '5111859731'),
#     ('Amber Perez', 403445, 'M', '0602870126')
# ]
#
# worker_objects = []
#
# for per in persons:
#     worker_objects.append(Worker(per[0], per[1], per[2], per[3]))
#
# for worker in worker_objects:
#     worker.get_info()

#
# class CustomLabel:
#     def __init__(self, text: str, **kwargs: dict):
#         self.text = text
#         if kwargs:
#             for k, v in kwargs.items():
#                 setattr(self, k, v)
#
#     def config(self, **kwargs: dict):
#         if kwargs:
#             for k, v in kwargs.items():
#                 setattr(self, k, v)
#
#
# label1 = CustomLabel(text="Hello Python", fg="#eee", bg="#333")
# label2 = CustomLabel(text="Username")
# label3 = CustomLabel(text="Password", font=("Comic Sans MS", 24, "bold"), bd=20, bg='#ffaaaa')
# label4 = CustomLabel(text="Hello", bd=20, bg='#ffaaaa')
# label5 = CustomLabel(text="qwwerty", a=20, b='#ffaaaa', r=[3, 4, 5, 6], p=32)
#
# assert label1.__dict__ == {'text': 'Hello Python', 'fg': '#eee', 'bg': '#333'}
# assert label2.__dict__ == {'text': 'Username'}
# assert label3.__dict__ == {'text': 'Password', 'font': ('Comic Sans MS', 24, 'bold'), 'bd': 20, 'bg': '#ffaaaa'}
# assert label4.__dict__ == {'text': 'Hello', 'bd': 20, 'bg': '#ffaaaa'}
# assert label5.__dict__ == {'text': 'qwwerty', 'a': 20, 'b': '#ffaaaa', 'r': [3, 4, 5, 6], 'p': 32}
#
# print(label1.__dict__)
# print(label2.__dict__)
# print(label3.__dict__)
# print(label4.__dict__)
# print(label5.__dict__)
#
# label4.config(color='red', bd=100)
# label5.config(color='red', bd=100, a=32, b=432, p=100, z=432)
#
# assert label4.__dict__ == {'text': 'Hello', 'bd': 100, 'bg': '#ffaaaa', 'color': 'red'}
# assert label5.__dict__ == {'text': 'qwwerty', 'a': 32, 'b': 432, 'r': [3, 4, 5, 6], 'p': 100,
#                            'color': 'red', 'bd': 100, 'z': 432}


# Мы можем создать полноценную игру
# «Камень-Ножницы-Бумага» при помощи двух классов.
# class Player:
#     def __init__(self, name):
#         self.name = name
#         self.choice = None
#
#     def choose(self):
#         self.choice = input(f"{self.name}, choose rock, "\
#         f"paper or scissors: ").lower()
#
#
# class Game:
#     def __init__(self, player1, player2):
#         self.player1 = player1
#         self.player2 = player2
#         self.rules = {
#             "rock": "scissors",
#             "paper": "rock",
#             "scissors": "paper"
#         }
#
#     def get_winner(self):
#         if self.player1.choice == self.player2.choice:
#             return None
#         elif self.rules[self.player1.choice] == self.player2.choice:
#             return self.player1
#         else:
#             return self.player2
#
#     def play(self):
#         self.player1.choose()
#         self.player2.choose()
#         winner = self.get_winner()
#         if winner:
#             print(f"{winner.name} победил!")
#         else:
#             print("У нас ничья.")
#

# Попробуйте аналогичным образом создать игру «Крестики-Нолики».
#
# # Пример использования
# player1 = Player("Игрок 1")
# player2 = Player("Игрок 2")
# game = Game(player1, player2)
# game.play()


#
# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def display_person_info(self):
#         print(f'Person: {self.name}, {self.age}')
#
#
# class Company:
#     def __init__(self, company_name, location):
#         self.company_name = company_name
#         self.location = location
#
#     def display_company_info(self):
#         print(f'Company: {self.company_name}, {self.location}')
#
#
# class Employee:
#     def __init__(self, name, age, company_name, location):
#         self.personal_data = Person(name, age)
#         self.work = Company(company_name, location)
#
#
# emp = Employee('Jessica', 28, 'Google', 'Atlanta')
# print(emp.personal_data.name)
# print(emp.personal_data.age)
# emp.personal_data.display_person_info()
# print(emp.work.company_name)
# print(emp.work.location)
# emp.work.display_company_info()


#
#
# class Task:
#     def __init__(self, name, description, status=False):
#         self.name = name
#         self.description = description
#         self.status = status
#
#     def display(self):
#         print(f'{self.name} {"(Сделана)" if self.status == True else "(Не сделана)"}')
#
#
# class TaskList:
#     def __init__(self):
#         self.tasks = []
#
#     def add_task(self, task):
#         self.tasks.append(task)
#
#     def remove_task(self, task):
#         self.tasks.remove(task)
#
#
# class TaskManager:
#     def __init__(self, tasklist_instance):
#         self.task_list = tasklist_instance
#
#     def mark_done(self, task_instance):
#         # Подсказка self.task_list это класс TaskList (нельзя итерировать)
#         # self.task_list.__dict__['tasks'] это класс Список (можно итерировать)
#         for task in self.task_list.__dict__['tasks']:
#             if task == task_instance:
#                 task.status = True
#
#     def mark_undone(self, task_instance):
#         for task in self.task_list.__dict__['tasks']:
#             if task == task_instance:
#                 task.status = False
#
#     def show_tasks(self):
#         for task in self.task_list.__dict__['tasks']:
#             task.display()
#
#
# todo = TaskList()
# assert todo.tasks == []

# # Создаем несколько задач и добавляем их в список
# task1 = Task("Стирка", "Постирать трусы, носки, слюнявчики")
# assert task1.name == 'Стирка'
# assert task1.description == 'Постирать трусы, носки, слюнявчики'
# assert task1.status is False
# task1.display()
#
# todo.add_task(task1)
# assert len(todo.tasks) == 1
#
# task2 = Task("Продукты", "Купить лук чеснок огурцы хлеб и биток")
# assert task2.name == 'Продукты'
# assert task2.description == 'Купить лук чеснок огурцы хлеб и биток'
# assert task2.status is False
#
# todo.add_task(task2)
# assert len(todo.tasks) == 2
#
# # Создаем менеджер задач и показываем список задач
# manager = TaskManager(todo)
# assert isinstance(manager.task_list, TaskList)
# print('-----Список дел-----')
# manager.show_tasks()
#
# # Отмечаем первую задачу выполненной и показываем список задач
# manager.mark_done(task1)
#
# # Проверяем изменился ли статус 2мя способами
# assert task1.status is True
# assert manager.task_list.tasks[0].status is True
#
# print('-----Список дел-----')
# manager.show_tasks()
#
# # Удаляем вторую задачу и показываем список задач
# todo.remove_task(task2)
#
# assert len(todo.tasks) == 1
# assert len(manager.task_list.tasks) == 1
#
# print('-----Список дел-----')
# manager.show_tasks()
#
#
#

# print('123')

#
# class Employee:
#     def __init__(self, name, salary):
#         self.__name = name
#         self.__salary = salary
#
#     def __get_name(self):
#         return self.__name
#
#     def __get_salary(self):
#         return self.__salary
#
#     def __set_salary(self, value):
#         if isinstance(value, int | float) and value > 0:
#             self.__salary = value
#         else:
#             print(f'ErrorValue:{value}')
#
#     title = property(fget=__get_name)
#     reward = property(fget=__get_salary, fset=__set_salary)
#
#
# employee = Employee("John Doe", 50000)
# assert employee.title == "John Doe"
# assert employee._Employee__name == "John Doe"
# assert isinstance(employee, Employee)
# assert isinstance(type(employee).title, property), 'Вы не создали property title'
# assert isinstance(type(employee).reward, property), 'Вы не создали property reward'
#
# assert employee.reward == 50000
# employee.reward = -100  # ErrorValue:-100
#
# employee.reward = 1.5
# assert employee.reward == 1.5
#
# employee.reward = 70000
# assert employee.reward == 70000
# employee.reward = 'hello'  # Печатает ErrorValue:hello
# employee.reward = '777'  # Печатает ErrorValue:777
# employee.reward = [1, 2]  # Печатает ErrorValue:[1, 2]
# assert employee.reward == 70000
# employee._Employee__set_salary(55000)
# assert employee._Employee__get_salary() == 55000

#
# class UserMail:
#     def __init__(self, login, email):
#         self.login = login
#         self.email = email
#
#     def get_email(self):
#         return self.__email
#
#     def set_email(self, value):
#         if isinstance(value, str) and value.count('@') == 1 and '.' in value and value.index('.') > value.index('@'):
#             self.__email = value
#         else:
#             raise ValueError(f"ErrorMail:{value}")
#
#     email = property(fget=get_email, fset=set_email)
#
#
# k = UserMail('belosnezhka', 'prince@wait.you')
# print(k.email)
# print(k.login)
# for value in [True, 'prince@still@.wait', 'prince@stillwait']:
#     try:
#         k.email = value
#     except ValueError as e:
#         print(e)
#
# k.email = 'prince@still.wait'
# print(k.get_email())
# try:
#     k.email = 'pri.nce@stillwait'
# except ValueError as e:
#     print(e)
# print(k.email)\

#
# class UserMail:
#     users = []
#     current_user = None
#
#     def __init__(self, login, email):
#         self.login = login
#         self.email = email
#
#     def get_login(self):
#         return self.name
#
#     def set_login(self, value):
#
#         # if value not in self.users:
#             if value != self.current_user:
#                 if not isinstance(value, str):
#                     raise TypeError(f'{value}не является строкой')
#                 else:
#                     self.name = value
#                     self.current_user = self.name
#                     # self.users.append(self.name)
#             else:
#                 raise ValueError(f'Логин {value} уже имеется в системе')
#
#     def get_email(self):
#         return self.__email
#
#     def set_email(self, value):
#         if isinstance(value, str) and value.count('@') == 1 and '.' in value and value.index('.') > value.index('@'):
#             self.__email = value
#         else:
#             raise ValueError(f"ErrorMail:{value}")
#
#     email = property(fget=get_email, fset=set_email)
#     login = property(fget=get_login, fset=set_login)
#
#
# jim = UserMail("aka47", 'hello@com.org')
# print(isinstance(type(jim).login, property))
# print(f'Jim login is {jim.login}')
# try:
#     bim = UserMail("aka47", 'world@com.org')
# except ValueError as e:
#     print(e)
# jim.login = 'aka48'
# print(f'Jim login is {jim.login}')
# bim = UserMail("aka47", 'world@com.org')
# print(f'Bim login is {bim.login}')


# def divide(x, y):
#     try:
#         result = x / y
#     except ZeroDivisionError:
#         print("division by zero!")
#     else:
#         print("result is", result)
#     finally:
#         print("executing finally clause")
#
# divide(4,4)


# class TimeZone:
#     def __init__(self, name, offset_hours, offset_minutes):
#         self.name = name
#         self.offset_hours = offset_hours
#         self.offset_minutes = offset_minutes
#
#     @property
#     def name(self):
#         return self._name
#
#     @name.setter
#     def name(self, value):
#         if value and isinstance(value, str) and len(value.strip()) > 0:
#             self._name = value.strip()
#         else:
#
#             raise ValueError(f'Timezone bad name - {value}')
#
#     @property
#     def offset_hours(self):
#         return self._offset_hours
#
#     @offset_hours.setter
#     def offset_hours(self, value):
#         if not isinstance(value, int):
#             raise ValueError('Hour offset must be an integer.')
#
#         if value not in range(-12, 15):
#             raise ValueError('Offset must be between -12:00 and +14:00.')
#         else:
#             self._offset_hours = value
#
#     @property
#     def offset_minutes(self):
#         return self._offset_minutes
#
#     @offset_minutes.setter
#     def offset_minutes(self, value):
#         if not isinstance(value, int):
#             raise ValueError('Minutes offset must be an integer.')
#         if value not in range(-59, 60):
#             raise ValueError('Minutes offset must between -59 and 59.')
#         else:
#             self._offset_minutes = value
#
#
# try:
#     TimeZone(' Abc ', -20.5, 34)
# except ValueError as e:
#     print(e)
#
# try:
#     TimeZone(' Abc ', -15, 34)
# except ValueError as e:
#     print(e)
#
# try:
#     TimeZone(' Abc ', 15, 34)
# except ValueError as e:
#     print(e)
#
# tz = TimeZone(' Abc ', 10, 34)
# print(tz.name)
# print(tz.offset_hours)
# print(tz.offset_minutes)


# print(1 or [])

#
# class Rectangle:
#     def __init__(self, length, width):
#         self._length, self._width = length, width
#         self.__area, self.__perimeter = None, None
#
#     @property
#     def length(self):
#         return self._length
#
#     @length.setter
#     def length(self, value):
#         self._length = value
#         self.__area = None
#         self.__perimeter = None
#
#     @property
#     def width(self):
#         return self._width
#
#     @width.setter
#     def width(self, value):
#         self._width = value
#         self.__area = None
#         self.__perimeter = None
#
#     @property
#     def area(self):
#         if self.__area is None:
#             self.__area = self._width * self._length
#         return self.__area
#
#     @property
#     def perimeter(self):
#         if self.__perimeter is None:
#             self.__perimeter = 2 * (self._width + self._length)
#         return self.__perimeter
#
# #Вариант короче
# # class Rectangle:
# #     def __init__(self, a, b):
# #         self.a, self.b = a, b
# #
# #     @property
# #     def area(self):
# #         return self.a * self.b
# #
# #     @property
# #     def perimeter(self):
# #         return (self.a + self.b) * 2
#
#
# r2 = Rectangle(15, 3)
# print(r2.area)
# print(r2.perimeter)
#
# r3 = Rectangle(43, 232)
# print(r3.area)
# print(r3.perimeter)


#
# class Date:
#     def __init__(self, day, month, year):
#         self._day = day
#         self._month = month
#         self._year = year
#
#     @property
#     def day(self):
#         if len(str(self._day)) == 1:
#             self._day = '0' + str(self._day)
#         return str(self._day)
#
#     @property
#     def month(self):
#         if len(str(self._month)) == 1:
#             self._month = '0' + str(self._month)
#         return str(self._month)
#
#     @property
#     def year(self):
#         if len(str(self._year)) < 4:
#             self._year = str(self.year).rjust(4,'0')
#         return str(self._year)
#
#     @property
#     def date(self):
#         return f'{self.day}/{self.month}/{self.year}'
#
#     @property
#     def usa_date(self):
#         return f'{self.month}-{self.day}-{self.year}'
#
#
#
# d1 = Date(5, 10, 2001)
# assert isinstance(d1, Date)
#
# # print(d1.day, d1.month, d1.year)
# # print(d1.date)
# assert d1.date == '05/10/2001'
# assert d1.usa_date == '10-05-2001'
# assert isinstance(type(d1).date, property), 'Вы не создали property date'
# print(d1.date, d1.usa_date)
#
# d2 = Date(15, 3, 999)
# assert isinstance(d2, Date)
# assert d2.date == '15/03/0999'
# assert d2.usa_date == '03-15-0999'
# assert isinstance(type(d2).date, property), 'Вы не создали property date'
# print(d2.date, d2.usa_date)
#
# d3 = Date(3, 5, 3)
# assert d3.date == '03/05/0003'
# assert d3.usa_date == '05-03-0003'
# print(d3.date, d3.usa_date)
#


# class Desk:
#     def __init__(self, name):
#         self._name = name
#
#     @property
#     def name(self):
#         return self._name
#
#     @name.setter
#     def name(self, value):
#         self._name = value
#
#     @name.deleter
#     def name(self):
#         del self._name
#
#
#
# test = Desk('Test')
# print(test.__dict__)
# test.name = 'OOO'
# print(test.__dict__)
# print(test.name)
# del test.name
# print(test.__dict__)

#
# class TemperatureConverter:
#
#     @staticmethod
#     def celsius_to_fahrenheit(c):
#         return c * (9 / 5) + 32
#
#     @staticmethod
#     def fahrenheit_to_celsius(f):
#         return (f - 32) * (5 / 9)
#
#     @staticmethod
#     def celsius_to_kelvin(c):
#         return c + 273.15
#
#     @staticmethod
#     def kelvin_to_celsius(k):
#         return k - 273.15
#
#     @staticmethod
#     def fahrenheit_to_kelvin(f):
#         return round((((5 / 9) * (f - 32)) + 273.15),2)
#
#     @staticmethod
#     def kelvin_to_fahrenheit(k):
#         return round((((9 / 5) * (k - 273.15)) + 32), 2)
#
#     @staticmethod
#     def format(degree, symbol):
#         match symbol:
#             case 'F':
#                 return f'{degree}°F'
#             case 'C':
#                 return f'{degree}°C'
#             case 'K':
#                 return f'{degree}°K'
#
#
# assert TemperatureConverter.celsius_to_fahrenheit(0) == 32.0
# assert TemperatureConverter.celsius_to_fahrenheit(10) == 50.0
# assert TemperatureConverter.celsius_to_fahrenheit(15) == 59.0
# assert TemperatureConverter.celsius_to_fahrenheit(20) == 68.0
# assert TemperatureConverter.celsius_to_fahrenheit(25) == 77.0
# assert TemperatureConverter.celsius_to_fahrenheit(30) == 86.0
#
# assert TemperatureConverter.fahrenheit_to_celsius(86) == 30.0
# assert TemperatureConverter.fahrenheit_to_celsius(77) == 25.0
# assert TemperatureConverter.fahrenheit_to_celsius(68) == 20.0
# assert TemperatureConverter.fahrenheit_to_celsius(59) == 15.0
# assert TemperatureConverter.fahrenheit_to_celsius(50) == 10.0
# assert TemperatureConverter.fahrenheit_to_celsius(32) == 0
#
# converter = TemperatureConverter()
# assert converter.celsius_to_kelvin(100) == 373.15
# assert converter.kelvin_to_celsius(273.15) == 0
# # print(converter.fahrenheit_to_kelvin(50))
# # print(converter.kelvin_to_fahrenheit(50))
# assert converter.fahrenheit_to_kelvin(50) == 283.15
# assert converter.fahrenheit_to_kelvin(134.33) == 330.0
# assert converter.kelvin_to_fahrenheit(54.0) == -362.47
# assert converter.kelvin_to_fahrenheit(1653.0) == 2515.73
# assert converter.format(1653.0, 'K') == '1653.0°K'
# assert converter.format(45, 'F') == '45°F'
# assert converter.format(36.6, 'C') == '36.6°C'
#
# print('Good')


# class RobotVacuumCleaner:
#     name = 'Henry'
#     charge = 25
#
#     @classmethod
#     def update_charge(cls, new_value):
#         cls.charge = new_value
#
#     @staticmethod
#     def hello(name):
#         return f'Привет, {name}'
#
#     @property
#     def data(self):
#         return {
#             'name': self.name,
#             'charge': self.charge
#         }
#
#     def make_clean(self):
#         if self.charge < 30:
#             return 'Кожаный, заряди меня! Я слаб'
#         return 'Я вычищу твою берлогу!!!'
#
#
# # код ниже не нужно удалять, в нем находятся проверки
# print(RobotVacuumCleaner.hello('Господин'))
# RobotVacuumCleaner.update_charge(50)
#
# robot = RobotVacuumCleaner()
# print(robot.make_clean())
# print(robot.data)
#
# RobotVacuumCleaner.update_charge(False)
# print(robot.make_clean())
# print(RobotVacuumCleaner.__dict__)
# print(dir(robot))


# class Date:
#     def __init__(self, day: int, month: int, year: int):
#         self.day, self.month, self.year = day, month, year
#
#     @classmethod
#     def from_str(cls, value):
#         day, month, year = value.split('-')
#         return cls(int(day), int(month), int(year))
#
#
# day_1 = Date.from_str('12-4-2024')
# day_2 = Date.from_str('06-09-2022')
# print(day_1.day, day_1.month, day_1.year)
# print(day_2.day, day_2.month, day_2.year)


# class Circle:
#
#     def __init__(self, radius):
#         if not Circle.is_positive(radius):
#             raise ValueError("Радиус должен быть положительным")
#         self.radius = radius
#
#     @classmethod
#     def from_diameter(cls, diameter):
#         return cls(diameter / 2)
#
#     @staticmethod
#     def is_positive(number):
#         return True if number > 0 else False
#
#     @staticmethod
#     def area(radius):
#         return 3.14 * (radius ** 2)
#
#
#
#
# # код ниже не нужно удалять, в нем находятся проверки
# circle_1 = Circle.from_diameter(10)
# assert isinstance(circle_1, Circle)
# assert circle_1.radius == 5.0
# print(f"circle_1.radius={circle_1.radius}")
# assert Circle.is_positive(10)
# assert not Circle.is_positive(-5)
# assert Circle.area(1) == 3.14
# assert Circle.area(2) == 12.56
#

#
# Настройки приложения
# Очень часто настройки приложения выносят в отдельный файл и при старте приложения подгружают из него значения.
#
# Вам необходимо разработать простой конфигурационный менеджер для вашего приложения.
# Для этого необходимо реализовать класс AppConfig, который предоставляет методы для загрузки
# конфигурации из JSON-файла и получения значений конкретных параметров.
#
# В классе AppConfig должно быть реализовано следующее:
#
# метод load_config, который загружает конфигурацию из указанного JSON-файла
#
# метод get_config, который принимает ключ и возвращает соответствующее значение из загруженной конфигурации. Если ключ не найден,
# метод должен возвращать None. Также необходимо предоставить возможность обращаться к вложенным параметрам через точку.
#
# Вам будет предоставлен файл 'app_config.json', который имеет следующее содержимое
#
# Необходимо реализовать возможность вызова перечисленных методов как через класс, так и через экземпляр.
# Также необходимо обеспечить распространение значений параметров на все экземпляры класса AppConfig. Это значит, что все экземпляры AppConfig должны иметь одинаковые значения конфигурации приложения.
#
# Выбор реализации данной задачи остается за вами.

#
# import json
# #импорт встроенного модуля json
#
#
# class AppConfig:
#     data = dict()
#     # Создание атрибута класса - пустого списка
#
#     @classmethod
#     def load_config(cls, filename):
#         """Метод для загрузки файла и сохранения его в атрибут data"""
#         with open(filename) as f:
#             cls.data = json.load(f)
#             # Функция load загрузила объект из файла и произвела его десериализацию —превращение в словарь dict.
#         return cls
#
#     @classmethod
#     def get_config(cls, key: str):
#         #Метод для доступа к значениям json(Атрибута data)
#         keys = key.split('.')
#         if len(keys) == 1:
#             return cls.data.get(keys[0])
#         return cls.data.get(keys[0], {}).get(keys[1])
#         #чтобы не было ошибки в первый get в значение по умолчанию вставить пустой словарь,
#         # потому что метода get нет у None (у всех нет кроме словарей).
#
#
# AppConfig.load_config('app_config.json')
# print(AppConfig.data)
#
# # Получение значения конфигурации
# assert AppConfig.get_config('database') == {
#     'host': '127.0.0.1', 'port': 5432,
#     'database_name': 'postgres_db',
#     'user': 'owner',
#     'password': 'ya_vorona_ya_vorona'}
# assert AppConfig.get_config('database.user') == 'owner', 'HellNOOO'
# assert AppConfig.get_config('database.password') == 'ya_vorona_ya_vorona'
# assert AppConfig.get_config('database.pass') is None
# assert AppConfig.get_config('password.database') is None
#
# config = AppConfig()
# assert config.get_config('max_connections') == 10
# assert config.get_config('min_connections') is None
#
# conf = AppConfig()
# assert conf.get_config('max_connections') == 10
# assert conf.get_config('database.user') == 'owner'
# assert conf.get_config('database.host') == '127.0.0.1'
# assert conf.get_config('host') is None
#
# print('Good')


# a = {
#   "database": {
#     "host": "127.0.0.1",
#     "port": 5432,
#     "database_name": "postgres_db",
#     "user": "owner",
#     "password": "ya_vorona_ya_vorona"
#   },
#   "api_key": "hUFHu834837248jhoiHF89",
#   "log_level": "debug",
#   "max_connections": 10
# }
#
# # print(a.update({'one': 1}))
# # a.setdefault('LLL', 5555)
# d = a.popitem()
# print(d)
# print(a)


# def bubble_sort(lst):
#     n = len(lst)
#     for i in range(n):
#         for j in range(0, n - i - 1):
#             if lst[j] > lst[j + 1]:
#                 lst[j], lst[j + 1] = lst[j + 1], lst[j]
#     return lst
#
# a = [9,5,2,1,8]
# print(bubble_sort(a))


# Есть файл с большими терабайтами слов,
# как прочитать из него слова и загрузить в другой файл только те что длиннее 10 букв?

# Для обработки очень большого файла с текстом (в терабайтах), чтобы прочитать из него слова и записать в другой файл только те, что длиннее 10 букв,
# нужно использовать построчное или по частям чтение файла, чтобы не загружать весь файл в память целиком.
# Это позволит избежать ошибок нехватки памяти и эффективно работать с большими объемами данных.

# Пример алгоритма на Python:
# Открыть исходный файл на чтение в текстовом режиме с указанием кодировки (например, UTF-8).
# Открыть новый файл на запись.
# Построчно читать исходный файл.
# Для каждой строки разбивать её на слова (например, по пробелам или другим разделителям).
# Проверять длину каждого слова, и если длина больше 10, записывать это слово в новый файл (каждое слово с новой строки или с нужным разделителем).
#
# Закрыть оба файла.


# import time
# from datetime import datetime
#
# input_file = 'big_input.txt'
# output_file = 'filtered_output.txt'
#
# start_with_time = time.time()
# start_with_datetime = datetime.now()
#
# # time.sleep(10)
#
# with open(input_file, 'r', encoding='utf-8') as fin, open(output_file, 'w', encoding='utf-8') as fout:
#     for line in fin:
#         words = line.split()
#         for word in words:
#             if len(word) > 10:
#                 fout.write(word.strip('.').strip('(').strip(')').strip('),') + '\n')
#
#
# end_with_time = time.time()
# end_with_datetime = datetime.now()
#
#
#
# print(f'With time: {round(end_with_time - start_with_time, 2)}')
# print(f'With datetime modul: {end_with_datetime - start_with_datetime}')


# class Perimeter:
#     def __init__(self, height, weight):
#         self.__height = height
#         self.__weight = weight
#         self.__perimeter = None
#
#     @property
#     def height(self):
#         return self.__height
#
#     @height.setter
#     def height(self, value):
#         self.__height = value
#         self.__perimeter = None
#
#     @property
#     def weight(self):
#         return self.__weight
#
#     @weight.setter
#     def weight(self, value):
#         self.__weight = value
#         self.__perimeter = None
#
#     @property
#     def perimeter(self):
#         if self.__perimeter is None:
#             print('Calc')
#             self.__perimeter = self.__weight * self.__height
#         return self.__perimeter
#
# p1 = Perimeter(4,5)
# print(p1.perimeter)
# print(p1.perimeter)
# p1.height = 5
# print(p1.perimeter)


# class MyClass:
#     class_attribute = "I am a class attribute"
#
#     @staticmethod
#     def change(new_value):
#         MyClass.class_attribute = new_value
#
#
# example_1 = MyClass()
# example_2 = MyClass()
# print(example_1.__dict__)
# print(example_2.__dict__)
#
# print(example_1.class_attribute)
# print(example_2.class_attribute)
#
# example_1.change("Class attribute modified")
#
# print(example_1.__dict__)
# print(example_2.__dict__)
#
#
# print(example_1.class_attribute)
# print(example_2.class_attribute)


# class MyClass:
#     class_attribute = "I am a class attribute"
#
#     def __init__(self):
#         self.instance_attribute = "I am an instance attribute"
#
#     @classmethod
#     def create_attr(cls, attr_name, attr_value):
#         setattr(cls, attr_name, attr_value)
#
#
# example_1 = MyClass()
# example_2 = MyClass()
# example_3 = MyClass()
#
# print(example_1.__class__.__name__)
# # # print(example_2.__dict__)
# # print(example_3.__dict__)
# # print(MyClass.__dict__)
#
# example_1.create_attr('new_attr', "Hello world")
# # print(MyClass.__dict__)
#
#
# print(example_1.new_attr)
# print(example_2.__dict__)
# print(example_3.__dict__)
#

# print(example_1.new_attr)
# print(example_2.new_attr)
# print(example_3.new_attr)


# class Container:
#     items = []
#
#     def add_item(self, value):
#         self.items = [value] + self.items
#
#
# box1 = Container()
# box1.add_item(2)
# box1.add_item(4)
#
#
# box2 = Container()
# box2.add_item(5)
# box2.add_item(7)
#
# print(Container.items)

#
# class Robot:
#     population = 0
#
#     def __init__(self, name):
#         self.name = name
#         Robot.population += 1
#         print(f'Робот {name} был создан')
#
#     def destroy(self):
#         Robot.population -= 1
#         print(f'Робот {self.name} был уничтожен')
#
#     def say_hello(self):
#         print(f'Робот {self.name} приветствует тебя, особь человеческого рода')
#
#     @classmethod
#     def how_many(cls):
#         print(f'{cls.population}, вот сколько нас еще осталось')
#
#
# droid1 = Robot("R2-D2")
# assert droid1.name == 'R2-D2'
# assert Robot.population == 1
# droid1.say_hello()
# Robot.how_many()
# droid2 = Robot("C-3PO")
# assert droid2.name == 'C-3PO'
# assert Robot.population == 2
# droid2.say_hello()
# Robot.how_many()
# droid1.destroy()
# assert Robot.population == 1
# droid2.destroy()
# assert Robot.population == 0
# Robot.how_many()


# class MyClass:
#     class_attribute = "I am a class attribute"
#
#     def __init__(self):
#         self.instance_attribute = "I am an instance attribute"
#
#
# example_1 = MyClass()
# example_2 = MyClass()
# example_3 = MyClass()
#
# example_1.class_attribute = "Class attribute modified"
# print(example_1.__dict__)
#
# print(example_2.class_attribute)
# print(example_2.__dict__)
#
# print(example_3.class_attribute)
# print(example_3.__dict__)


# class User:
#     def __init__(self, name, role):
#         self.name = name
#         self.role = role
#
#
# class Access:
#     __access_list = ['admin', 'developer']
#
#     @staticmethod
#     def __check_access(role_name):
#         if role_name in Access.__access_list:
#             return True
#         return False
#
#     @staticmethod
#     def get_access(instance):
#         if isinstance(instance, User):
#             if Access.__check_access(instance.role):
#                 print(f'User {instance.name}: success')
#             else:
#                 print(f'AccessDenied')
#
#         else:
#             print(f'AccessTypeError')


# user1 = User('batya99', 'admin')
# assert Access.get_access(user1) == 'User batya99: success'  # печатает "User batya99: success"
# zaya = User('milaya_zaya999', 'user')
# Access.get_access(zaya) # печатает AccessDenied

# Access.get_access(5) # печатает AccessTypeError


# class BankAccount:
#     bank_name = 'Tinkoff Bank'
#
#     address = 'Москва, ул. 2-я Хуторская, д. 38А'
#
#     def __init__(self, name, balance):
#         self.name = name
#         self.balance = balance
#
#     @classmethod
#     def create_account(cls, name, summ):
#         return cls(name, summ)
#
#     @classmethod
#     def bank_info(cls):
#         return f'{cls.bank_name} is located in {cls.address}'

#
# from string import digits
#
#
# class User:
#
#     def __init__(self, login, password):
#         self.login = login
#         self.password = password
#         self.__secret = 'abracad'
#
#     @property
#     def password(self):
#         print('getter called')
#         return self.__password
#
#     @property
#     def secret(self):
#         s = input('Введите ваш пароль: ')
#         if s == self.password:
#             return self.__secret
#         else:
#             raise ValueError('Доступ закрыт')
#
#     @staticmethod
#     def is_different_pass(password):
#         with open("pass.txt", 'r', encoding='UTF-8') as f:
#             for line in f:
#                 words = line.split()
#                 for word in words:
#                     if word == password:
#                         return False
#             return True
#
#     @staticmethod
#     def is_include_number(password):
#         for digit in digits:
#             if digit in password:
#                 return True
#         return False
#
#     @password.setter
#     def password(self, value):
#         print('setter called')
#         if not isinstance(value, str):
#             raise TypeError('Пароль должен быть строкой')
#         if len(value) < 4 or len(value) > 12:
#             raise ValueError('Пароль должен быть не менее 4 и не более 12 символов')
#         if not User.is_include_number(value):#при момощи not False превращается в True
#             raise ValueError('Пароль должен содержать хотя бы одну цифру')
#         if not User.is_different_pass(value):
#             raise ValueError('Пароль слишком распространен')
#         self.__password = value


# x = User('Zai', 'seven77')

# assert x.secret == 'abracad'
# print('Good')


# Пицца
# class Pizza:
#     def __init__(self, ingredients=None):
#         if ingredients is None:
#             ingredients = []
#         self.ingredients = ingredients
#
#
#     @classmethod
#     def margherita(cls):
#         return cls(['mozzarella', 'tomatoes'])
#
#     @classmethod
#     def peperoni(cls):
#         return cls(['mozzarella', 'peperoni', 'tomatoes'])
#
#     @classmethod
#     def barbecue(cls):
#         return cls(['mozzarella', 'red onion', 'sause bbq', 'chicken'])
#
#
#
# bbq = Pizza.barbecue()
# peperoni = Pizza.peperoni()
# margherita = Pizza.margherita()
# print(sorted(bbq.ingredients))
# print(sorted(peperoni.ingredients))
# print(sorted(margherita.ingredients))

# Задача «Регистрация»
# from string import ascii_letters, digits, ascii_lowercase, ascii_uppercase
#
#
# class Registration:
#     def __init__(self, login, password):
#         self.login = login
#         self.password = password
#
#     @property
#     def login(self):
#         return self.__login
#
#     @login.setter
#     def login(self, value):
#         if not isinstance(value, str):
#             raise TypeError
#         if '@' not in value:
#             raise ValueError
#         if '.' not in value.partition('@')[2]:
#             raise ValueError
#         self.__login = value
#
#     @property
#     def password(self):
#         return self.__password
#
#     @staticmethod
#     def is_include_digit(password):
#         for digit in digits:
#             if digit in password:
#                 return True
#         return False
#
#     @staticmethod
#     def is_include_all_register(password):
#         flag = False
#         for letter in password:
#             if letter in ascii_uppercase:
#                 flag = True
#             if letter in ascii_lowercase:
#                 flag = True
#         return flag
#
#     @staticmethod
#     def is_include_only_latin(password):
#         flag = False
#         for letter in password:
#             if letter in ascii_letters:
#                 flag = True
#         return flag
#
#     @staticmethod
#     def check_password_dictionary(password):
#         with open('easy_passwords.txt', 'r', encoding='UTF-8') as f:
#             file = f.read()
#             if password not in file:
#                 return False
#             return True
#
#     @password.setter
#     def password(self, value):
#         if not isinstance(value, str):
#             raise TypeError("Пароль должен быть строкой")
#         if not 4 < len(value) < 12:
#             ValueError('Пароль должен быть длиннее 4 и меньше 12 символов')
#         if not Registration.is_include_digit(value):
#             raise ValueError('Пароль должен содержать хотя бы одну цифру')
#         if not Registration.is_include_all_register(value):
#             raise ValueError('Пароль должен содержать хотя бы один символ верхнего и нижнего регистра')
#         if not Registration.is_include_only_latin(value):
#             raise ValueError('Пароль должен содержать только латинский алфавит')
#         if Registration.check_password_dictionary(value):
#             raise ValueError('Ваш пароль содержится в списке самых легких')
#         self.__password = value
#
#
# try:
#     s2 = Registration("fga", "asd12")
# except ValueError as e:
#     pass
# else:
#     raise ValueError("Registration('fga', 'asd12') как можно записать такой логин?")
#
# try:
#     s2 = Registration("fg@a", "asd12")
# except ValueError as e:
#     pass
# else:
#     raise ValueError("Registration('fg@a', 'asd12') как можно записать такой логин?")
#
# s2 = Registration("translate@gmail.com", "as1SNdf")
# try:
#     s2.login = "asdsa12asd."
# except ValueError as e:
#     pass
# else:
#     raise ValueError("asdsa12asd как можно записать такой логин?")
#
# try:
#     s2.login = "asdsa12@asd"
# except ValueError as e:
#     pass
# else:
#     raise ValueError("asdsa12@asd как можно записать такой логин?")
#
# assert Registration.check_password_dictionary('QwerTy123'), 'проверка на пароль в слове не работает'
#
# try:
#     s2.password = "QwerTy123"
# except ValueError as e:
#     pass
# else:
#     raise ValueError("QwerTy123 хранится в словаре паролей, как его можно было сохранить?")
#
# try:
#     s2.password = "KissasSAd1f"
# except ValueError as e:
#     pass
# else:
#     raise ValueError("KissasSAd1f хранится в словаре паролей, как его можно было сохранить?")
#
# try:
#     s2.password = "124244242"
# except ValueError as e:
#     pass
# else:
#     raise ValueError("124244242 пароль НЕОЧЕНЬ, как его можно было сохранить?")
#
# try:
#     s2.password = "RYIWUhjkdbfjfgdsffds"
# except ValueError as e:
#     pass
# else:
#     raise ValueError("RYIWUhjkdbfjfgdsffds пароль НЕОЧЕНЬ, как его можно было сохранить?")
#
# try:
#     s2.password = "CaT"
# except ValueError as e:
#     pass
# else:
#     raise ValueError("CaT пароль НЕОЧЕНЬ, как его можно было сохранить?")
#
# try:
#     s2.password = "monkey"
# except ValueError as e:
#     pass
# else:
#     raise ValueError("monkey пароль НЕОЧЕНЬ, как его можно было сохранить?")
#
# try:
#     s2.password = "QwerTy123"
# except ValueError as e:
#     pass
# else:
#     raise ValueError("QwerTy123 пароль есть в слове, нельзя его использовать")
#
# try:
#     s2.password = "HelloQEWq"
# except ValueError as e:
#     pass
# else:
#     raise ValueError("HelloQEWq пароль НЕОЧЕНЬ, как его можно было сохранить?")
#
# try:
#     s2.password = [4, 32]
# except TypeError as e:
#     pass
# else:
#     raise TypeError("Пароль должен быть строкой")
#
# try:
#     s2.password = 123456
# except TypeError as e:
#     pass
# else:
#     raise TypeError("Пароль должен быть строкой")
#
# print('U r hacked Pentagon')

# Задача «Корзина»
#
# class File:
#     def __init__(self, name):
#         self.name = name
#         self.in_trash = False
#         self.is_deleted = False
#
#     def restore_from_trash(self):
#         print(f'Файл {self.name} восстановлен из корзины')
#         self.in_trash = False
#
#     def remove(self):
#         print(f'Файл {self.name} был удален')
#         self.is_deleted = True
#
#     def read(self):
#         if self.is_deleted:
#             return print(f'ErrorReadFileDeleted({self.name})')
#         elif self.in_trash:
#             return print(f'ErrorReadFileTrashed({self.name})')
#         else:
#             print(f'Прочитали все содержимое файла {self.name}')
#
#     def write(self, content):
#         if self.is_deleted:
#             return print(f'ErrorWriteFileDeleted({self.name})')
#         elif self.in_trash:
#             return print(f'ErrorWriteFileTrashed({self.name})')
#         else:
#             print(f'Записали значение {content} в файл {self.name}')
#
#
# class Trash:
#     content = []
#
#     @staticmethod
#     def add(file):
#         if isinstance(file, File):
#             Trash.content += [file]
#             file.in_trash = True
#         else:
#             return print('В корзину можно добавлять только файл')
#
#     @staticmethod
#     def clear():
#         print('Очищаем корзину')
#         for file in Trash.content:
#             file.remove()
#         Trash.content.clear()
#
#         print('Корзина пуста')
#
#     @staticmethod
#     def restore():
#         print('Восстанавливаем файлы из корзины')
#         for file in Trash.content:
#             file.restore_from_trash()
#         Trash.content.clear()
#         print('Корзина пуста')
#
#
# f1 = File('puppies.jpg')
# f2 = File('cat.jpg')
# f3 = File('xxx.doc')
# passwords = File('pass.txt')
#
# for file in [f1, f2, f3, passwords]:
#     assert file.is_deleted is False
#     assert file.in_trash is False
#
# f3.read()
# f3.remove()
# assert f3.is_deleted is True
# f3.read()
# f3.write('hello')
#
# assert Trash.content == []
#
# Trash.add(f2)
# Trash.add(passwords)
# Trash.add(f3)
#
# f1.read()
# Trash.add(f1)
# f1.read()
#
# for file in [f1, f2, f3, passwords]:
#     assert file.in_trash is True
#
# for f in [f2, passwords, f3, f1]:
#     assert f in Trash.content
#
# Trash.restore()
# assert Trash.content == [], 'После восстановления корзина должна была очиститься'
#
# Trash.add(passwords)
# Trash.add(f2)
# Trash.add('hello')
# Trash.add(f1)
#
# for f in [passwords, f2, f1]:
#     assert f in Trash.content
#
# Trash.clear()
#
# for file in [passwords, f2, f1]:
#     assert file.is_deleted is True
#
# assert Trash.content == [], 'После удаления файлов корзина должна была очиститься'
#
# f1.read()


# from f


# Задача «Оформление заказа» - 2

# class Product:
#     def __init__(self, name, price):
#         self.name = name
#         self.price = price
#
#
# class User:
#     def __init__(self, login, balance=0):
#         self.login = login
#         self.balance = balance
#
#     def __str__(self):
#         return f'Пользователь {self.login}, баланс - {self.balance}'
#
#     @property
#     def balance(self):
#         return self.__balance
#
#     @balance.setter
#     def balance(self, value):
#         self.__balance = value
#
#     def deposit(self, value):
#         self.__balance += value
#
#     def is_money_enough(self, value):
#         return self.__balance >= value
#
#     def payment(self, value):
#         if self.is_money_enough(value):
#             self.__balance -= value
#             return self.__balance
#         else:
#             return print('Не хватает средств на балансе. Пополните счет')
#
#
# class Cart:
#     def __init__(self, user):
#         self.user = user
#         self.goods = dict()
#         self.__total = 0
#
#     def add(self, product, count=1):
#         self.goods[product] = 0
#         self.goods[product] += count
#         self.__total += product.price * count
#
#     def remove(self, product, count=1):
#         # if self.goods[product] - count > 0:
#         #     self.goods[product] -= count
#         #     if self.__total - product.price * count > 0:
#         #         self.__total -= product.price * count
#         #     else:
#         #         self.__total = 0
#         # else:
#         #     self.goods[product] = 0
#
#         if count > self.goods[product]:
#             self.__total -= self.goods[product] * product.price
#             del self.goods[product]
#             return
#         self.goods[product] = self.goods.get(product, 0) - count
#         self.__total -= count * product.price
#
#     @property
#     def total(self):
#         return self.__total
#
#     def order(self):
#         if self.user.payment(self.total):
#             return print('Заказ оплачен')
#         else:
#             return print('Проблема с оплатой')
#
#     def print_check(self):
#         print('---Your check---')
#         sorted_lst = sorted(self.goods, key=lambda x: x.name)
#         for elem in sorted_lst:
#             if self.goods[elem] > 0:
#                 print(f'{elem.name} {elem.price} {self.goods[elem]} {elem.price * self.goods[elem]}')
#         print(f'---Total: {self.total}---')
#
# billy = User('billy@rambler.ru')
# print(billy )
# lemon = Product('lemon', 20)
# carrot = Product('carrot', 30)
# zara = Product('zara', 1530)
#
# cart_billy = Cart(billy)
# assert cart_billy.goods == {}, 'Создайте пустой словарь в goods'
# cart_billy.add(lemon, 5)
# cart_billy.add(zara, 5)
# cart_billy.add(carrot)
# # print(cart_billy.goods)
# assert cart_billy.total == 7780, 'Должен пересчитываться при добавлении.__total'
# assert cart_billy.goods[lemon] == 5, 'Должно быть пять лимонов хранится в goods'
#
# cart_billy.remove(lemon, 100)
# # cart_billy.goods.get(lemon)
# assert cart_billy.goods.get(lemon, 0) == 0, 'Нельзя удалить из корзины больше чем было'
# cart_billy.print_check()
# cart_billy.add(lemon, 3)
# cart_billy.print_check()
# cart_billy.remove(lemon, 6)
# cart_billy.print_check()
# print(cart_billy.total)
# cart_billy.add(lemon, 5)
# cart_billy.print_check()
# cart_billy.order()
# cart_billy.user.deposit(8150)
# print(cart_billy.user.balance)
# cart_billy.order()
# print(cart_billy.user.balance)


# class BankAccount:
#     def __init__(self, name, balance):
#         self.name = name
#         self.balance = balance
#
#     def __str__(self):
#         return f'{self.name} - {self.balance}'
#
#     def __add__(self, other):
#         print('call __add__')
#         if isinstance(other, BankAccount):
#             return BankAccount(self.name, self.balance + other.balance)
#         if isinstance(other, (int, float)):
#             return BankAccount(self.name, self.balance + other)
#         raise NotImplemented
#
#
#
#     def __radd__(self, other): #не обязательно прописывать сложную логику,
#         print('call __radd__') # можно просто поменять местами операнды в ретерне
#         return self + other # и тем самым задействовать метод __add__  для эк с уже описанной логикой
#
# t = BankAccount('y', 100)
#
# print(t+12)
#
# print(12 + t)

#
# a = '12'
# a.

# class City:
#     def __init__(self, name):
#         self.name = name.title()
#
#     def __str__(self):
#         return f"{self.name}"
#
#     def __bool__(self):
#         return False if self.name[-1] in 'aeiou' else True
#
#
# p1 = City('new york')
# assert p1.name == "New York"
# assert p1.__str__() == "New York"
# assert isinstance(p1, City)
# print(p1)
# assert bool(p1)
#
# p2 = City('SaN frANCISco')
# assert isinstance(p2, City)
# assert p2.name == "San Francisco"
# print(p2)
# assert not bool(p2)
#
# p3 = City('NIZHNY NoVGORod')
# assert p3.name == "Nizhny Novgorod"
# print(p3)
# assert bool(p3)
# assert isinstance(p3, City)

#
# class Quadrilateral:
#     def __init__(self, width, height=None):
#         # Для тех кто забыл что делать когда возможен либо 1 либо 2 аргумента.
#         # height обьявляем как None по умолчанию, а к self.height присваиваем выражение -генератор"
#         self.width = width
#         self.height = height if height else width
#
#     def __bool__(self):
#         if self.width == self.height:
#             return True
#         else:
#             return False
#
#     def __str__(self):
#         if bool(Quadrilateral(self.width, self.height)):
#             return f'Квадрат размером {self.width}х{self.height}'
#         else:
#             return f'Прямоугольник размером {self.width}х{self.height}'

# @property
# def width(self):
#     return self.__width
#
# @width.setter
# def width(self, *args):
#     self.__width = args
#
# def __bool__(self):
#     # if len(self.__width) == 1:
#     #     return True
#     if len(self.__width) > 1:
#         if self.__width[0] == self.__width[1]:
#             return True
#         else:
#             return False
#     else:
#         return False
#
# def __str__(self):
#     if len(self.__width) == 1:
#         return f'Квадрат размером {self.__width[0]}х{self.__width[0]}'
#     elif bool(self.__width):
#         return f'Квадрат размером {self.__width[0]}х{self.__width[1]}'
#     else:
#         return f'Прямоугольник размером {self.__width[0]}х{self.__width[1]}'


# print(callable('hello'))

# a = 1


# class QuadraticFunction:
#     def __init__(self, a, b, c):
#         self.a = a
#         self.b = b
#         self.c = c
#
#     def __call__(self, x):
#         return self.a * (x**2) + self.b * x + self.c
#
#
# f = QuadraticFunction(2, 5, 7)
# assert f(1) == 14
# assert f(-3) == 10
# assert f(2) == 25
# assert f(5) == 82
#
# f_2 = QuadraticFunction(-1, 2, 4)
# assert f_2(5) == -11
# assert f_2(2) == 4
# assert f_2(-3) == -11
# assert f_2(1) == 5
# print('Good')

#
# class Addition:
#
#     def __call__(self, *args):
#         summa = 0
#         for i in args:
#             if isinstance(i, int) or isinstance(i, float):
#                 summa += i
#         return f'Сумма переданных значений = {summa}'
#
#
# add = Addition()
# assert add(10, 20) == "Сумма переданных значений = 30"
# assert add(1, 2, 3.4) == "Сумма переданных значений = 6.4"
# assert add(1, 2, 'hello', [1, 2], 3) == "Сумма переданных значений = 6"
#
#
# add2 = Addition()
# assert add2(10, 20, 3, 3, 4, 3, 2, 43, 43) == "Сумма переданных значений = 131"
# assert add2() == "Сумма переданных значений = 0"
# assert add2('hello') == "Сумма переданных значений = 0"
#
# print('Good')


# from time import time
#
#
# class Timer:
#     def __init__(self, func):
#         self.f = func
#
#     def __call__(self, *args, **kwargs):
#         start = time()
#         self.f(*args, **kwargs)
#         stop = time()
#         print(f'Время работы {stop - start}')
#
#
# @Timer
# def calculate():
#     for i in range(10000000):
#         2 ** 100


# calculate()
# print(calculate())


# a = list(map(int, input().split()))
#
# print(a)


# class DateUSA:
#     def __init__(self, day, month, year):
#         self._day = day
#         self._month = month
#         self._year = year
#
#     @property
#     def day(self):
#         if len(str(self._day)) == 1:
#             self._day = str(self._day).zfill(2)
#         return str(self._day)
#
#     @property
#     def month(self):
#         if len(str(self._month)) == 1:
#             self._month = str(self._month).zfill(2)
#         return str(self._month)
#
#     @property
#     def year(self):
#         if len(str(self._year)) < 4:
#             self._year = str(self._year).rjust(4, '0')
#         return str(self._year)
#
#     def format(self):
#         return f'{self.month}/{self.day}/{self.year}'
#
#     def isoformat(self):
#         return f'{self.year}-{self.month}-{self.day}'
#
#
# class DateEurope:
#
#     def __init__(self, day, month, year):
#         self._day = day
#         self._month = month
#         self._year = year
#
#     @property
#     def day(self):
#         if len(str(self._day)) == 1:
#             self._day = str(self._day).zfill(2)
#         return str(self._day)
#
#     @property
#     def month(self):
#         if len(str(self._month)) == 1:
#             self._month = str(self._month).zfill(2)
#         return str(self._month)
#
#     @property
#     def year(self):
#         if len(str(self._year)) < 4:
#             self._year = str(self._year).rjust(4, '0')
#         return str(self._year)
#
#     def format(self):
#         return f'{self.day}/{self.month}/{self.year}'
#
#     def isoformat(self):
#         return f'{self.year}-{self.month}-{self.day}'


# d = DateEurope(5, 12, 2001)
# print(d.format())
# print(d.isoformat())
#
# d = DateUSA(1, 5, 890)
# print(d.format())
# print(d.isoformat())


# print(dir(a))
# print(type(a))
# print(isinstance(a, int))
# print(id(a))
#
# from functools import total_ordering
#
#
# @total_ordering
# class BankAccount:
#     def __init__(self, name, balance):
#         self.name = name
#         self.balance = balance
#
#     def __str__(self):
#         return self.name
#
#     def __eq__(self, other):
#         if isinstance(other, BankAccount):
#             return self.balance == other.balance
#         else:
#             return self.balance == other
#
#     def __lt__(self, other):
#         if isinstance(other, BankAccount):
#             return self.balance < other.balance
#         else:
#             return self.balance < other


# class BankAccount:
#     def __init__(self, name, balance):
#         self.name = name
#         self.balance = balance
#
#     def __str__(self):
#         return self.name
#
#     # def __add__(self, other):
#     #     if isinstance(other, BankAccount):
#     #         return self.balance + other.balance
#     #     elif isinstance(other, Numbers):
#     #         return self.balance + other.summ
#     #     elif isinstance(other, int):
#     #         return self.balance + other
#
#     def __radd__(self, other):
#         if isinstance(other, BankAccount):
#             return other.balance + self.balance
#         elif isinstance(other, Numbers):
#             return sum(other._values) + self.balance
#         elif isinstance(other, int) or isinstance(other, float):
#             return other + self.balance
#
#
# class Numbers:
#     def __init__(self, values: list):
#         self._values = values
#
#     # @property
#     # def summ(self):
#     #     return sum(self._values)
#
#     # def __add__(self, other):
#     #     if isinstance(other, BankAccount):
#     #         return self.summ + other.balance
#     #     elif isinstance(other, Numbers):
#     #         return self.summ + other.summ
#     #     elif isinstance(other, int) or isinstance(other, float):
#     #         return self.summ + other
#
#     def __radd__(self, other):
#         if isinstance(other, BankAccount):
#             return other.balance + sum(self._values)
#         elif isinstance(other, Numbers):
#             return sum(other._values) + sum(self._values)
#         elif isinstance(other, int) or isinstance(other, float):
#             return other + sum(self._values)
#
#
# lst = [
#     BankAccount('Jack', 1000),
#     Numbers([1, 2, 3, 4, 5]),
#     BankAccount('Ivan', 30),
#     7.5,
#     Numbers([10, 20, 30, 40, 50]),
#     BankAccount('Frank', 2000),
#     10
# ]
# print(sum(lst))


# class Vector:
#     def __init__(self, *args):
#         self.values = list(args)
#
#     def __repr__(self):
#         return f'Vector({", ".join([str(value) for value in self.values])})'
#
#     def __getitem__(self, value):
#         data = [i for i, v in enumerate(self.values, 1) if value == v]
#         if not data:
#             raise ValueError(f"В векторе отсутствует значение {value}")
#         return data if len(data) > 1 else data[0]
#
#
#
# v1 = Vector(5, 5, 5, 4, 4, 3)
# print(v1[4])  # [4, 5]
# print(v1[5])  # [1, 2, 3]
# print(v1[3])  # 6
# try:
#     print(v1[2])
# except ValueError as e:
#     print(e)


# class Vector:
#     def __init__(self, *args):
#         self.values = list(args)
#
#     def __repr__(self):
#         return f'Vector({", ".join([str(value) for value in self.values])})'
#
#     def __getitem__(self, item):
#         if isinstance(item, int):
#             if 1 <= item <= len(self.values):
#                 return self.values[item-1]
#             else:
#                 raise IndexError(f"Индекс {item} находится за пределами вектора")
#         elif isinstance(item, str):
#             if 1 <= len(item) <= len(self.values):
#                 return self.values[len(item)-1]
#             else:
#                 raise IndexError(f"Индекс {len(item)} находится за пределами вектора")
#
#     #ИЛИ
#     # def __getitem__(self, item):
#     #     item = item if isinstance(item, int) else len(item)
#     #     if 0 < item <= len(self.values):
#     #         return self.values[item - 1]
#     #     else:
#     #         raise IndexError(f"Индекс {item} находится за пределами вектора")

# v = Vector(3, 655, 323, 672, 11, 6)
# print(v[1])  # 3
# print(v[2])  # 655
# print(v['cat'])  # 323
# print(v['park'])  # 672
# try:
#     print(v[''])
# except IndexError as e:
#     print(e)


# class Vector:
#     def __init__(self, *args):
#         self.values = list(args)
#
#     def __repr__(self):
#         return f'Vector({", ".join([str(value) for value in self.values])})'
#
#     def __getitem__(self, item):
#         if 0 <= item < len(self.values):
#             return self.values[item]
#         else:
#             raise IndexError(f"Индекс {item} находится за пределами вектора")
#
#     def __delitem__(self, value):
#         if value in self.values:
#             while value in self.values:
#                 self.values.remove(value)
#         else:
#             raise ValueError(f'Значение {value} отсутствует в векторе')
#
#
# v1 = Vector(5, 5, 5, 4, 4, 3)
# print(v1)
# del v1[4]
# print(v1)
# del v1[5]
# print(v1)
# try:
#     del v1[10]
# except ValueError as e:
#     print(e)
#
#
# class Building:
#     def __init__(self, floors):
#         self.floors = {floor: None for floor in range(0, floors + 1)}
#
#     def __getitem__(self, item):
#         if 0 <= item <= len(self.floors):
#             return self.floors[item]
#         else:
#             raise ValueError(f'В здании нет такого этажа - {item}')
#
#     def __setitem__(self, key, value):
#         if 0 <= key <= len(self.floors):находится ли индекс в пределах длины атрибута
#             if self.floors[key] is None:
#                 self.floors[key] = value
#         else:
#             raise ValueError(f'В здании нет такого этажа - {key}')
#
#     def __delitem__(self, key):
#         if key in self.floors:
#             self.floors[key] = None
#         else:
#             raise ValueError(f'В здании нет такого этажа - {key}')
#
#
#
#         # или
#     #
#     # def __init__(self, floors):
#     #     self.floors = [None] * floors
#     #
#     # def __setitem__(self, floor, cmp_name):
#     #     self.floors[floor] = cmp_name
#     #
#     # def __getitem__(self, floor):
#     #     return self.floors[floor]
#     #
#     # def __delitem__(self, floor):
#     #     self.floors[floor] = None
#
# iron_building = Building(22)  # Создаем здание с 22 этажами
# print(iron_building.floors)
# iron_building[0] = 'Reception'
# print(iron_building.floors)
# iron_building[1] = 'Oscorp Industries'
# print(iron_building.floors)
# iron_building[2] = 'Stark Industries'
# print(iron_building.floors)
#
# print(iron_building[2])
# del iron_building[2]
# print(iron_building[2])
#


# class Song:
#     def __init__(self, title, artist):
#         self.title = title
#         self.artist = artist
#
#
# class Playlist:
#     def __init__(self):
#         self.songs = []
#
#     def __getitem__(self, item):
#         return self.songs[item]
#
#     def __setitem__(self, key, value):
#         self.songs.insert(key, value)
#
#     def add_song(self, value):
#         self.songs.append(value)
#
# playlist = Playlist()
# assert len(playlist.songs) == 0
# assert isinstance(playlist, Playlist)
# playlist.add_song(Song("Paradise", "Coldplay"))
# assert playlist[0].title == 'Paradise'
# assert playlist[0].artist == 'Coldplay'
# assert len(playlist.songs) == 1
# print(playlist.songs)
#
# playlist[0] = Song("Resistance", "Muse")
# assert playlist[0].title == 'Resistance'
# assert playlist[0].artist == 'Muse'
# assert playlist[1].title == 'Paradise'
# assert playlist[1].artist == 'Coldplay'
#
# playlist[1] = Song("Helena", "My Chemical Romance")
# assert playlist[1].title == 'Helena'
# assert playlist[1].artist == 'My Chemical Romance'
#
# assert playlist[2].title == 'Paradise'
# assert playlist[2].artist == 'Coldplay'
# print('Good')
#
#
# class ShoppingCart:
#     def __init__(self):
#         self.items = dict()
#
#     def __getitem__(self, item):
#         return self.items.get(item, 0)
#
#     def __setitem__(self, key, value):
#         if key in self.items:
#             self.items[key] += value
#         self.items[key] = value
#
#     def __delitem__(self, key):
#         del self.items[key]
#
#     def add_item(self, good, count=1):
#         if good in self.items:
#             self.items[good] += count
#         else:
#             self.items[good] = count
#
#     def remove_item(self, good, count=1):
#         if good in self.items:
#             if count >= self.items[good]:
#                 del self.items[good]
#             else:
#                 self.items[good] -= count
#         # else:
#         #     print('Товар отсутствует в корзине')
#
#
# cart = ShoppingCart()
#
# # Add some items to the cart
# cart.add_item('Apple', 3)
# cart.add_item('Banana', 2)
# cart.add_item('Orange')
#
# assert cart['Banana'] == 2
# assert cart['Orange'] == 1
# assert cart['Kivi'] == 0
#
# cart.add_item('Orange', 9)
# assert cart['Orange'] == 10
#
# print("Shopping Cart:")
# for item_name in cart.items:
#     print(f"{item_name}: {cart[item_name]}")
#
# cart['Apple'] = 5
# cart['Banana'] = 7
# cart['Kivi'] = 11
# assert cart['Apple'] == 5
# assert cart['Banana'] == 7
# assert cart['Kivi'] == 11
#
# print("Updated Shopping Cart:")
# for item_name in cart.items:
#     print(f"{item_name}: {cart[item_name]}")
#
# # Remove an item from the cart
# cart.remove_item('Banana')
# assert cart['Banana'] == 6
#
# cart.remove_item('Apple', 4)
# assert cart['Apple'] == 1
#
# cart.remove_item('Apple', 2)
# assert cart['Apple'] == 0
# assert 'Apple' not in cart.items
#
# cart.remove_item('Potato')
#
# del cart['Banana']
# assert cart['Banana'] == 0
# assert 'Banana' not in cart.items
#
# print("Updated Shopping Cart:")
# for item_name in cart.items:
#     print(f"{item_name}: {cart[item_name]}")


# class SparseArray:
#     def __init__(self, *args):
#         self.__array = list(args)
#
#     def __getitem__(self, item):
#         if item > len(self.__array):
#             diff = item - len(self.__array)
#             self.__array.extend([None] * diff + [None])
#         else:
#             return self.__array[item]
#
#     def __setitem__(self, key, value):
#         if key > len(self.__array):
#             diff = key - len(self.__array)
#             self.__array.extend([None] * diff + [None])
#             self.__array[key] = value
#         else:
#             self.__array[key] = value
#
#     def __delitem__(self, key):
#         if key <= len(self.__array):
#             self.__array[key] = None
#
#     def __len__(self):
#         return len(self.__array)
#
#     @property
#     def values(self):
#         return tuple(self.__array)
#
#
# array = SparseArray(1, 2, 3)
# print(array.values)
# print(array[7])
# print(array.values)
# array[6] = 100
# print(array.values)
# array[10] = 200
# print(array.values)
# del array[1]
# print(array.values)
# print(len(array))


# class AttributeChecker:
#     def __contains__(self, item):
#         return item in self.__dict__


# class Shape:
#     pass
#
#
# class Ellipse(Shape):
#     pass
#
#
# class Circle(Ellipse):
#     pass
#
#
# class Polygon(Shape):
#     pass
#
#
# class Triangle(Polygon):
#     pass
#
#
# class Rectangle(Polygon):
#     pass
#
#
# class Square(Rectangle):
#     pass
#
#
# shapes = [
#     Polygon(), Triangle(), Ellipse(), Polygon(), Triangle(), Ellipse(), Polygon(), Square(), Polygon(), Circle(),
#     Shape(), Polygon(), Triangle(), Circle(), Ellipse(), Shape(), Circle(), Rectangle(), Circle(), Circle(),
#     Square(), Square(), Circle(), Rectangle(), Rectangle(), Polygon(), Polygon(), Polygon(), Square(), Square(),
#     Rectangle(), Square(), Rectangle(), Polygon(), Circle(), Triangle(), Rectangle(), Shape(), Rectangle(),
#     Polygon(), Polygon(), Ellipse(), Square(), Circle(), Shape(), Polygon(), Ellipse(), Triangle(), Square(),
#     Polygon(), Triangle(), Circle(), Rectangle(), Rectangle(), Ellipse(), Triangle(), Rectangle(), Polygon(),
#     Shape(), Circle(), Rectangle(), Polygon(), Triangle(), Circle(), Polygon(), Rectangle(), Polygon(), Square(),
#     Triangle(), Circle(), Ellipse(), Circle(), Shape(), Circle(), Triangle(), Ellipse(), Square(), Circle(),
#     Triangle(), Polygon(), Square(), Polygon(), Circle(), Ellipse(), Polygon(), Shape(), Triangle(), Rectangle(),
#     Circle(), Square(), Triangle(), Triangle(), Ellipse(), Square(), Circle(), Rectangle(), Ellipse(), Shape(),
#     Triangle(), Ellipse(), Circle(), Shape(), Polygon(), Polygon(), Ellipse(), Rectangle(), Square(), Shape(),
#     Circle(), Triangle(), Circle(), Circle(), Circle(), Triangle(), Ellipse(), Polygon(), Circle(), Ellipse(),
#     Rectangle(), Circle(), Shape(), Polygon(), Polygon(), Triangle(), Rectangle(), Polygon(), Shape(), Circle(),
#     Shape(), Circle(), Triangle(), Ellipse(), Square(), Circle(), Triangle(), Ellipse(), Square(), Circle(),
# ]
#
# c = 0
# r = 0
# e = 0
# for i in shapes:
#     if isinstance(i, Circle):
#         c += 1
#     elif isinstance(i, Rectangle):
#         r += 1
#     elif isinstance(i, Polygon):
#         e += 1
#
# print(c, r, e+r, sep='\n')
# d = Shape
# print(d.__class__)


# class PrettyPrint:
#     def __str__(self):
#         return f'{self.__class__.__name__}({", ".join([f"{k}={v}" for k, v in self.__dict__.items()])})'
#
#
# class Person(PrettyPrint):
#     def __init__(self, first_name, last_name, age):
#         self.first_name = first_name
#         self.last_name = last_name
#         self.age = age
#
#
# artem = Person('Artem', 'Egorov', 33)
# ivan = Person('Ivan', 'Ivanov', 45)
# print(artem)
# print(ivan)


# class Rectangle:
#     def __init__(self, length, width):
#         self.length = length
#         self.width = width
#
#     def area(self):
#         return self.length * self.width
#
#     def perimeter(self):
#         return 2 * self.length + 2 * self.width
#
#
# class Square(Rectangle):
#     def __init__(self, length):
#         super().__init__(length, length)


# class Person:
#     def __init__(self, name, passport):
#         self.name = name
#         self.passport = passport
#
#     def display(self):
#         print(f'{self.name}: {self.passport}')
#
# class Employee(Person):
#     def __init__(self, name, passport, salary, department):
#         super().__init__(name, passport)
#         self.salary = salary
#         self.department = department


# class Vehicle:
#     def __init__(self, name, mileage, capacity):
#         self.name = name
#         self.mileage = mileage
#         self.capacity = capacity
#
#     def fare(self):
#         return self.capacity * 100
#
#     def display(self):
#         print(f'Total {self.name} fare is: {self.fare()}')
#
#
# class Bus(Vehicle):
#     def __init__(self, name, mileage):
#         super().__init__(name, mileage, capacity=50)
#
#     def fare(self):
#         return super().fare() + super().fare() * 0.1
#
#
# class Taxi(Vehicle):
#
#     def __init__(self, name, mileage):
#         super().__init__(name, mileage, capacity=4)
#
#     def fare(self):
#         return super().fare() + super().fare() * 0.35
#
#
# sc = Vehicle('Scooter', 100, 2)
# sc.display()
#
# merc = Bus("Mercedes", 120000)
# merc.display()
#
# polo = Taxi("Volkswagen Polo", 15000)
# polo.display()
#
#
# t = Taxi('x', 111)
# assert t.__dict__ == {'name': 'x', 'mileage': 111, 'capacity': 4}
# t.display()
# b = Bus('t', 123)
# assert b.__dict__ == {'name': 't', 'mileage': 123, 'capacity': 50}
# b.display()


# class Transport:
#     def __init__(self, brand, max_speed, kind=None):
#         self.brand = brand
#         self.max_speed = max_speed
#         self.kind = kind
#
#     def __str__(self):
#         return f'Тип транспорта {self.kind} марки {self.brand} может развить скорость {self.max_speed} км/ч'
#
#
# class Car(Transport):
#     def __init__(self, brand, max_speed, mileage, gasoline_residue):
#         super().__init__(brand, max_speed, 'Car')
#         self.mileage = mileage
#         self.__gasoline_residue = gasoline_residue
#
#     @property
#     def gasoline(self):
#         # if isinstance(self, Car)
#         return f'Осталось бензина {self.__gasoline_residue} л'
#
#     @gasoline.setter
#     def gasoline(self, value):
#         if isinstance(value, int):
#             self.__gasoline_residue += value
#             print(f'Объем топлива увеличен на {value} л и составляет {self.__gasoline_residue} л')
#         else:
#             print(f'Ошибка заправки автомобиля')
#
#
# class Boat(Transport):
#
#     def __init__(self, brand, max_speed, owners_name):
#         super().__init__(brand, max_speed, kind='Boat')
#         self.owners_name = owners_name
#
#     def __str__(self):
#         return f'Этой лодкой марки {self.brand} владеет {self.owners_name}'
#
#
# class Plane(Transport):
#
#     def __init__(self, brand, max_speed, capacity):
#         super().__init__(brand, max_speed, kind='Plane')
#         self.capacity = capacity
#
#     def __str__(self):
#         return f'Самолет марки {self.brand} вмещает в себя {self.capacity} людей'
#
#
# p1 = Transport('Chuck', 50)
# print(p1)
# assert isinstance(p1, Transport)
# assert p1.kind == None
# assert p1.brand == 'Chuck'
# assert p1.max_speed == 50
# assert p1.__dict__ == {'kind': None, 'brand': 'Chuck', 'max_speed': 50}
#
# c1 = Car('RRR', 50, 150, 999)
# print(c1)
#
# assert isinstance(c1, Car)
# assert c1.kind == "Car"
# assert c1.brand == 'RRR'
# assert c1.max_speed == 50
# assert c1.mileage == 150
# assert c1.gasoline == 'Осталось бензина 999 л'
# c1.gasoline = 100
# assert c1.gasoline == 'Осталось бензина 1099 л'
# assert c1.__dict__ == {'kind': 'Car', 'brand': 'RRR', 'max_speed': 50,
#                        'mileage': 150, '_Car__gasoline_residue': 1099}
#
# b1 = Boat('XXX', 1150, 'Arkasha')
# print(b1)
# assert isinstance(b1, Boat)
# assert b1.kind == "Boat"
# assert b1.brand == 'XXX'
# assert b1.max_speed == 1150
# assert b1.owners_name == 'Arkasha'
#
# pla = Plane('www', 2150, 777)
# print(pla)
# assert isinstance(pla, Plane)
# assert pla.kind == "Plane"
# assert pla.brand == 'www'
# assert pla.max_speed == 2150
# assert pla.capacity == 777
# print('GOOD')
#
# transport = Transport('Telega', 10)
# print(transport)  # Тип транспорта None марки Telega может развить скорость 10 км/ч
# bike = Transport('shkolnik', 20, 'bike')
# print(bike)  # Тип транспорта bike марки shkolnik может развить скорость 20 км/ч
#
# first_plane = Plane('Virgin Atlantic', 700, 450)
# print(first_plane)  # Самолет марки Virgin Atlantic может вмещать в себя 450 людей
# first_car = Car('BMW', 230, 75000, 300)
# print(first_car)  # Тип транспорта Car марки BMW может развить скорость 230 км/ч
# print(first_car.gasoline)  # Осталось бензина на 300 км
# first_car.gasoline = 20  # Печатает 'Объем топлива увеличен на 20 л и составляет 320 л'
# print(first_car.gasoline)  # Осталось бензина на 350 км
# second_car = Car('Audi', 230, 70000, 130)
# second_car.gasoline = [None]  # Печатает 'Ошибка заправки автомобиля'
# first_boat = Boat('Yamaha', 40, 'Petr')
# print(first_boat)  # Этой лодкой марки Yamaha владеет Petr


#
# from functools import total_ordering
#
# class Initialization:
#
#     def __init__(self, capacity, food):
#         if isinstance(capacity, int):
#             self.capacity = capacity
#             self.food = food
#         else:
#             print('Количество людей должно быть целым числом')
#
#
# class Vegetarian(Initialization):
#
#     def __init__(self, capacity, food):
#         super().__init__(capacity, food)
#
#     def __str__(self):
#         return f'{self.capacity} людей предпочитают не есть мясо! Они предпочитают {self.food}'
#
#
# class MeatEater(Initialization):
#
#     def __init__(self, capacity, food):
#         super().__init__(capacity, food)
#
#     def __str__(self):
#         return f'{self.capacity} мясоедов в Москве! Помимо мяса они едят еще и {self.food}'
#
# @total_ordering
# class SweetTooth(Initialization):
#
#     def __init__(self, capacity, food):
#         super().__init__(capacity, food)
#
#     def __str__(self):
#         return f'Сладкоежек в Москве {self.capacity}. Их самая любимая еда: {self.food}'
#
#
#     def __eq__(self, other):
#         if isinstance(other, int):
#             return self.capacity == other
#         elif isinstance(other, Vegetarian) or isinstance(other, MeatEater):
#             return self.capacity == other.capacity
#         else:
#             return f'Невозможно сравнить количество сладкоежек с {other}'
#
#     def __lt__(self, other):
#         if isinstance(other, int):
#             return self.capacity < other
#         elif isinstance(other, Vegetarian) or isinstance(other, MeatEater):
#             return self.capacity < other.capacity
#         else:
#             return f'Невозможно сравнить количество сладкоежек с {other}'
#
#     # def __gt__(self, other):
#     #     if isinstance(other, int):
#     #         return self.capacity > other
#     #     elif isinstance(other, Vegetarian) or isinstance(other, MeatEater):
#     #         return self.capacity > other.capacity
#     #     else:
#     #         return f'Невозможно сравнить количество сладкоежек с {other}'
#
# p1 = Initialization('Chuck', [])
# assert isinstance(p1, Initialization)
# assert not hasattr(p1, 'capacity'), 'Не нужно создавать атрибут "capacity", если передается не целое число'
# assert not hasattr(p1, 'food'), 'Не нужно создавать атрибут "food", если передается не целое число'
#
# c1 = Vegetarian(100, [1, 2, 3])
# print(c1)
# assert isinstance(c1, Vegetarian)
# assert c1.capacity == 100
# assert c1.food == [1, 2, 3]
#
# b1 = MeatEater(1000, ['Arkasha'])
# print(b1)
# assert isinstance(b1, MeatEater)
# assert b1.capacity == 1000
# assert b1.food == ['Arkasha']
#
# pla = SweetTooth(444, [2150, 777])
# print(pla)
# assert isinstance(pla, SweetTooth)
# assert pla.capacity == 444
# assert pla.food == [2150, 777]
# assert pla > 100
# assert not pla < 80
# assert not pla == 90
# assert pla > c1
# assert not pla < c1
# assert not pla == c1
# assert not pla > b1
# assert pla < b1
# assert not pla == b1
#
# v_first = Vegetarian(10000, ['Орехи', 'овощи', 'фрукты'])
# print(v_first)  # 10000 людей предпочитают не есть мясо! Они предпочитают ['Орехи', 'овощи', 'фрукты']
# v_second = Vegetarian([23], ['nothing'])  # Количество людей должно быть целым числом
#
# m_first = MeatEater(15000, ['Жареную картошку', 'рыба'])
# print(m_first)  # 15000 мясоедов в Москве! Помимо мяса они едят еще и ['Жареную картошку', 'рыба']
# s_first = SweetTooth(30000, ['Мороженое', 'Чипсы', 'ШОКОЛАД'])
# print(s_first)  # Сладкоежек в Москве 30000. Их самая любимая еда: ['Мороженое', 'Чипсы', 'ШОКОЛАД']
# print(s_first > v_first)  # Сладкоежек больше, чем людей с другим вкусовым предпочтением
# print(30000 == s_first)  # Количество сладкоежек из опрошенных людей совпадает с 30000
# print(s_first == 25000)  # Количество людей не совпадает
# print(100000 < s_first)  # Количество сладкоежек в Москве не больше, чем 100000
# print(100 < s_first)  # Количество сладкоежек больше, чем 100


#
# def validate_age(age):
#     if age < 0 or age > 110:
#         raise ValueError("Invalid age")
#     return age
#
#
# try:
#     age = validate_age(int(input()))
# except ValueError as e:
#     print(e)
# else:
#     print('Возраст прошел проверку')


# class UserNotFoundError(Exception):
#     def __str__(self):
#         return f'User not found'
#
#
# users = {
#     "alice": {"name": "Alice Smith", "email": "alice@example.com"},
#     "bob": {"name": "Bob Johnson", "email": "bob@example.com"},
#     "jack": {"name": "Jack Wild", "email": "jack_wild@example.com"}
# }
#
#
# def get_user(username):
#     if username in users:
#         return users[username]['name']
#     else:
#         raise UserNotFoundError
# try:
#     username = get_user(input())
# except UserNotFoundError as e:
#     print(e)
# else:
#     print(username)


# class NegativeDepositError(Exception):
#     def __str__(self):
#         return f'Нельзя пополнить счет отрицательным значением'
#
#
# class InsufficientFundsError(Exception):
#     def __str__(self):
#         return f'Недостаточно средств для снятия'
#
#
# class BankAccount:
#     def __init__(self, balance):
#         self.balance = balance
#
#     def deposit(self, value):
#         if value < 0:
#             raise NegativeDepositError
#         self.balance += value
#
#     def withdraw(self, value):
#         if value > self.balance:
#             raise InsufficientFundsError
#         self.balance -= value

import string

#
#
# class PasswordInvalidError(Exception):
#     pass
#
#
# class PasswordLengthError(PasswordInvalidError):
#     def __str__(self):
#         return f'Пароль должен быть не менее 8 символов'
#
#
# class PasswordContainUpperError(PasswordInvalidError):
#     def __str__(self):
#         return f'Пароль должен содержать хотя бы одну заглавную букву'
#
#
# class PasswordContainDigitError(PasswordInvalidError):
#     def __str__(self):
#         return f'Пароль должен содержать хотя бы одну цифру'
#
#
# class User:
#     def __init__(self, username, password=None):
#         self.username = username
#         self.password = password
#
#     def set_password(self, passwd):
#         if len(passwd) < 8:
#             raise PasswordLengthError
#         elif not any(char.isupper() for char in passwd):
#             raise PasswordContainUpperError
#         elif not any(char.isdigit() for char in passwd):
#             raise PasswordContainDigitError
#         else:
#             self.password = passwd
#
#
# assert issubclass(PasswordInvalidError, Exception)
# assert issubclass(PasswordLengthError, PasswordInvalidError)
# assert issubclass(PasswordContainUpperError, PasswordInvalidError)
# assert issubclass(PasswordContainDigitError, PasswordInvalidError)
#
# user = User("johndoe")
#
# try:
#     user.set_password("weakpwd")
# except PasswordLengthError as e:
#     print(e)
#
# try:
#     user.set_password("strongpassword8")
# except PasswordContainUpperError as e:
#     print(e)
#
# try:
#     user.set_password("Safepassword")
# except PasswordContainDigitError as e:
#     print(e)
#
# user.set_password("SecurePass123")
# assert user.password == 'SecurePass123'
#
#
# def a(a: int):

# from functools import total_ordering
# from typing import List
# class A:
#     def s(self):
#         print('1111')
#
# class B(A):
#     pass
#
# b = B()
# b.s()


# class SequenceIterable:
#
#     def __init__(self, values):
#         self.values = values
#
#     def __getitem__(self, item):
#         return self.values[item]
#
#
# container = SequenceIterable([1, 5, 4, 6, 43, True, 'hello'])
# for i in container:
#     print(i)


# class Countdown:
#
#     def __init__(self, n):
#         self.n = n
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         temp = self.n
#         if self.n >= 0:
#             self.n -= 1
#             return temp
#         else:
#             raise StopIteration
#
# for i in Countdown(3):
#     print(i)

#
# class PowerTwo:
#
#     def __init__(self, number):
#         self.number = number
#         self.temp = -1
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if self.temp >= self.number:
#             raise StopIteration
#         self.temp += 1
#         return 2 ** self.temp
#
#
# # ИЛИ
#
#     # class PowerTwo:
#     #     def __init__(self, power):
#     #         self.pow_gen = (2 ** p for p in range(power + 1))
#     #
#     #     def __iter__(self):
#     #         return self
#     #
#     #     def __next__(self):
#     #         return next(self.pow_gen)
#
# numbers = PowerTwo(2)
#
# assert hasattr(numbers, '__next__') is True
# assert hasattr(numbers, '__iter__') is True
#
# iterator = iter(numbers)
# print('Элементы итератора PowerTwo(2)')
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# try:
#     print(next(iterator))
#     raise ValueError('Не реализовали StopIteration')
# except StopIteration:
#     pass
#
# print('-' * 15)
# print('Элементы итератора PowerTwo(20)')
# for i in PowerTwo(20):
#     print(i)


# class Card:
#     def __init__(self, rank, suit):
#         self.rank = rank
#         self.suit = suit
#
#     def __str__(self):
#         return f'{self.rank} {self.suit}'
# class Deck:
#     ranks = [str(n) for n in range(2, 11)] + list('JQKA')
#     suits = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
#
#     def __init__(self):
#         self.cards = [Card(rank, suit) for suit in self.suits for rank in self.ranks]
#
#     # def __getitem__(self, item):
#     #     return self.cards[item]
#
#     def __iter__(self):
#         return iter(self.cards)
#         #__iter__ всегда возвращает итератор


# deck = Deck()
# # print(deck.cards)
# for card in deck:
#     print(card)


# class FileReader:
#     def __init__(self, filename):
#         self.file = open(filename)
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         return self.file.__next__().strip()
# # self.file  - это итерируемый объект , так как метод open(filename) возвращает объект у которого есть метод __iter__
# # и одновременно это итератор , так как метод метод open(filename) также возвращает объект у которого есть метод __next__
# # Итак, мы получили итератор self.file  и теперь вызываем у него метод __next__
# # self.file.__next__()  . Этот момент метод __next__ возвращает первую строку у итератора self.file.
# # Если строк больше нет → выбрасывает StopIteration.
# #
# # То есть, self.file.__next__() = следующая строка из файла, и не нужно городить readlines() и split()
# #
# # Далее, чтобы очистить строку от пробелов применяем метод strip()
# # self.file.__next__().strip()
# # и в итоге возвращаем эту строку очищенную от пробелов в нашем def __next__(self):
#
# #
# for line in FileReader('lorem.txt'):
#     print(line)

# f = FileReader('lorem.txt')
# print(f.file)

#
# class StackIterator:
#     def __init__(self, stack: "Stack"):
#         #Мы используем строковый тип подсказки 'Stack', чтобы указать Python,
#         # что это тип Stack, который будет определен позже.
#         self.stack = stack
#         self.index = len(self.stack.items)
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if self.index <= 0:
#             raise StopIteration
#         self.index -= 1
#         return self.stack.items[self.index]
#
#
# class Stack:
#     def __init__(self):
#         self.items = []
#
#     def push(self, item):
#         self.items.append(item)
#
#     def pop(self):
#         if len(self.items) == 0:
#             print("Empty Stack")
#         else:
#             return self.items.pop()
#
#     def peek(self):
#         if len(self.items) == 0:
#             print("Empty Stack")
#         else:
#             return self.items[-1]
#
#     def is_empty(self):
#         return len(self.items) == 0
#
#     def size(self):
#         return len(self.items)
#
#     def __iter__(self):
#         return StackIterator(self)
#
#
# stack = Stack()
#
# stack.push(100)
# stack.push(True)
# stack.push('hello')
# stack.push('world')
#
# # Используем итератор для обхода стека
# for item in stack:
#     print(item)

#
# Создайте объект итератор FibonacciIterator, который умеет выдавать последовательность Фибоначчи из n чисел.
# Число n поступает при инициализации класса FibonacciIterator.
#
# Будем считать, что последовательность Фибоначчи следующая:
# 0, 1, 1, 2, 3, 5, 8, 13, 21 и т.д.
# Каждое следующее число получается суммой двух предыдущих.

# class FibonacciIterator:
#
#     def __init__(self, n):
#         self.n = n
#         self.index = 0
#         self.previous = 0
#         self.current = 1
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if self.index >= self.n:
#             raise StopIteration
#         if self.index == 0:
#             self.index += 1
#             return self.previous
#         self.index += 1
#         self.current, self.previous = self.previous, self.current + self.previous
#         # множественное присваивание
#         return self.previous
#
#
# fibonacci_iter = FibonacciIterator(7)
#
# for number in fibonacci_iter:
#     print(number)

#


# class Book:
#     def __init__(self, title, pages):
#         self.title = title
#         self.pages = pages
#
#
# class Library:
#     def __init__(self):
#         self.books = []
#
#     def add_book(self, book):
#         self.books.append(book)
#
#     def __iter__(self):
#         return LibraryIterator(
#             [j for i in self.books for j in i.pages])  # тут определите, что будете передавать итератору
#
#
# class LibraryIterator:
#
#     def __init__(self, pages):
#         self.pages = pages
#         self.index = 0
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if self.index >= len(self.pages):
#             raise StopIteration
#         self.index += 1
#         return self.pages[self.index - 1]
#
#
# # Пример использования
# book1 = Book("Book 1", ["Page 1", "Page 2", "Page 3", "Page 4"])
# book2 = Book("Book 2", ["Page A", "Page B", "Page C"])
# book3 = Book("Book 3", ["Chapter 1", "Chapter 2"])
#
# library = Library()
# library.add_book(book1)
# library.add_book(book2)
# library.add_book(book3)
#
# # Используем вложенный итератор для обхода страниц в библиотеке
# for page in library:
#     print(page)

#
# from random import randint
#
#
# class Dice:
#     def __init__(self, value):
#         self.value = value
#
#     def __str__(self):
#         return f"Dice={self.value}"
#
#
# class Game:
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         return Dice(randint(1, 100)), Dice(randint(1, 100))
#
#
# for d1, d2 in Game():
#     print(d1, d2)
#     if d1.value == 100 and d2.value == 100:
#         print('GameOver')
#         break


# class InfinityIterator:
#
#     def __init__(self, n=0):
#         self.n = n
#         self.d = 10
#         self.temp = 0
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         self.temp = self.n
#         self.n += self.d
#         return self.temp
#
#
# for i in InfinityIterator(7):
#     print(i)


# class Point:
#     def __init__(self, x):
#         self.x = x
#
#     @property
#     def x(self):
#         return self._x
#
#     @x.setter
#     def x(self, value):
#         self._x = int(value)
#
# a = Point(3)
# print(a.x)
# a.x = 1
# print(a.x)


from datetime import datetime

# Обычно, когда к дескриптору осуществляется доступ из класса, возвращают экземпляр дескриптора,
# а при доступе из экземпляра — нужное конкретное значение, в нашем случае - текущее время:

# class Time:
#     def __get__(self, instance, owner_class):
#         if instance is None:
#             return self
#         return datetime.now()
#
#
# class Logger:
#     current_time = Time()
#
#
# print(Logger.current_time)
# log = Logger()
# print(log.current_time)


# from datetime import datetime
#
# class Logger:
#
#     @property
#     def current_time(self):
#         return datetime.now()
#
# print(Logger.current_time)
# log = Logger()
# print(log.current_time)


# class StringValidation:
#
#     def __init__(self, length):
#         self.length = length
#
#     def __set_name__(self, owner_class, attribute_name):
#         self.attribute_name = attribute_name
#
#     def __set__(self, instance, value):
#         if not isinstance(value, str):
#             raise ValueError(f'В атрибут {self.attribute_name} можно сохранять только строки.')
#         if len(value) < self.length:
#             raise ValueError(f'Длина атрибута {self.attribute_name} должна быть не меньше {self.length} символов')
#         instance.__dict__[self.attribute_name] = value
#
#     def __get__(self, instance, owner_class):
#         if instance is None:
#             return self
#         return instance.__dict__.get(self.attribute_name, None)


# class MaxLengthAttribute:
#
#     def __get__(self, instance, owner):
#         if instance is None:
#             return self
#         if len(instance.__dict__) == 0:
#             return None
#         result = sorted(instance.__dict__.keys(), key=lambda x: (len(x), x), reverse=True)
#         # в качестве ключа сортировки использовал key=lambda x: (len(x), x) здесь сначала идет сортировка по длине,
#         # а если длина равна то сортировка происходит по алфавиту,
#         # ну и третьим параметром reverse=True, т.к. нам нужен самый длинный атрибут.
#         return result[0]
#
# class JustClass:
#     max_atr = MaxLengthAttribute()
# #
# #
# obj = JustClass()
# obj.mock = 15
# obj.city = "Saint Peterburg"
# obj.name = "Vasiliy"
# obj.door = 'wood'
#
# print(obj.max_atr)

# d = {'name': 1, 'm': 2, 'main': 3}
# a = sorted(d, key=lambda x: len(x), reverse=True)
# print(a)

#
# class ColourComponent:
#
#     def __init__(self, start, end):
#         self.start = start
#         self.end = end
#
#     def __set_name__(self, owner_class, attribute_name):
#         self.attribute_name = attribute_name
#
#     def __get__(self, instance, owner):
#         if instance is None:
#             return self
#         return int(instance.__dict__['hex'][self.start:self.end], 16)
#
#
# class Colour:
#     r = ColourComponent(1, 3)
#     g = ColourComponent(3, 5)
#     b = ColourComponent(5, 7)
#
#     def __init__(self, hex):
#         self.hex = hex
#
#
# colour = Colour("#abcded")
# print(colour.r)
# print(colour.g)
# print(colour.b)

#
#
# class Descriptor:
#     def __init__(self, *args):
#         self._values = args
#
#     def __get__(self, instance, owner):
#         if self._values:
#             return len(self._values)
#         return 'Empty'
#
#     def __set__(self, instance, value):
#         pass
#
#
# class Student:
#     marks = Descriptor(4, 5, 4, 5, 5, 5)
#
#
# misha = Student()
# misha.marks = 2
# print(misha.__dict__)
# print(misha.marks)


#
#
# class CustomProperty:
#     def __init__(self, fget=None, fset=None):
#         self.fget = fget
#         self.fset = fset
#
#     def __set_name__(self, owner_class, prop_name):
#         self.prop_name = prop_name
#
#     def __get__(self, instance, owner_class):
#         print('__get__ called...')
#         if instance is None:
#             return self
#         if self.fget is None:
#             raise AttributeError(f'{self.prop_name} is not readable.')
#         return self.fget(instance)
#
#     def __set__(self, instance, value):
#         print('__set__ called...')
#         if self.fset is None:
#             raise AttributeError(f'{self.prop_name} is not writable.')
#         self.fset(instance, value)
#
#
# class Person:
#     def get_name(self):
#         return self._name
#
#     def set_name(self, value):
#         self._name = value
#
#     name = CustomProperty(fget=get_name, fset=set_name)
#
# p = Person()
# print(p.__dict__)
# p.name = 'Artem'
# print(p.name)
# print(p.__dict__)
#
# # пробуем затемнить дескриптор
# p.__dict__['name'] = 'Egor'
# print(p.name)


# Дескипторы
# class StringValidation:
#     def __init__(self, min_length):
#         self.min_length = min_length
#
#     def __set_name__(self, owner_class, attribute_name):
#         self.attribute_name = attribute_name
#
#     def __set__(self, instance, value):
#         if not isinstance(value, str):
#             raise ValueError(f'В атрибут {self.attribute_name} можно сохранять только строки.')
#         if len(value) < self.min_length:
#             raise ValueError(f'Длина атрибута {self.attribute_name} должна '
#                              f'быть не меньше {self.min_length} символов')
#         instance.__dict__[self.attribute_name] = value
#
#     def __get__(self, instance, owner_class):
#         if instance is None:
#             return self
#         else:
#             print(f'calling __get__ for {self.attribute_name}')
#             return instance.__dict__.get(self.attribute_name, None)
#
# class Person:
#     name = StringValidation(5)
#     last_name = StringValidation(7)
#
#
# p = Person()
# p.name = 'Michail'
# p.last_name = 'Lermontov'
# print(p.name, p.last_name)
# try:
#     p.name = 'M.'
# except ValueError as ex:
#     print(ex)
# print(p.name, p.last_name)


# # Dataclasses
# from dataclasses import is_dataclass, dataclass
#
#
# # Создайте класс данных Point и два экземпляра
#
# @dataclass
# class Point:
#     x: int
#     y: int
#
#
# point1 = Point(5, 7)
# point2 = Point(-10, 12)
#
# print(point1, point2, sep='\n')
#
# # Ниже располагается код для проверки
#
# assert is_dataclass(Point), 'Point не dataclass'
# assert isinstance(point1, Point)
# assert isinstance(point2, Point)
# assert point1.x == 5
# assert point1.y == 7
# assert point2.x == -10
# assert point2.y == 12
# print('GREAT')

#
# from dataclasses import dataclass
# from typing import Optional
#
#
# @dataclass
# class Person:
#     city: str
#     first_name: str = 'Ivan'
#     last_name: str = 'Ivanov'
#     age: Optional[int] = None
#
#
#
# tim = Person(city='Ivanovo')
# print(tim.first_name)


# from dataclasses import dataclass
#
#
# @dataclass
# class Location:
#     name: str
#     longitude: float = 0
#     latitude: float = 11.5
#
#
# stonehenge = Location(name='Stonehenge', longitude=51, latitude=1.5)

#
# from dataclasses import dataclass, field
#
#
# @dataclass
# class Person:
#     first_name: str
#     last_name: str
#     hobbies: set = field(default_factory=set)

#
# from dataclasses import dataclass, field
#
#
# @dataclass
# class Article:
#     title: str = field(compare=False)
#     author: str = field(compare=False)
#     likes: int = field(init=False, default=0)
#
#
# a = Article('Как озвучивать фильмы', 'Дмитрий Пучков', 20)
# print(a.likes)


# a = {1,2,3}
# print(type(a))


#
# def a(*args, **kwargs):
#     return f'args = {args} kwargs = {kwargs}'
#
# print(a(1,2,3,4,a=1,b=2,c=3))

#

# Пример реализации Singleton
# class Logger:
#     __inst = None
#
#     def __new__(cls):
#         if not cls.__inst:
#             cls.__inst = super(Logger, cls).__new__(cls)
#             cls.__inst.log_level = 'INFO'
#         return cls.__inst
#
#     def set_level(self, level):
#         if not Logger.__inst:
#             raise ValueError('The instance has not created')
#         self.log_level = level
#
#     @staticmethod
#     def get_logger():
#         if not Logger.__inst:
#             Logger.__new__(Logger)
#         return Logger.__inst
#
#
# logger_1 = Logger.get_logger()
# print(logger_1.log_level)  # Выведет "INFO"
# Logger.set_level("DEBUG")
# print(logger_1.log_level)  # Выведет "DEBUG"
#
# logger_2 = Logger.get_logger()
# print(logger_2.log_level)  # Выведет "DEBUG"
# print(logger_2 is logger_1)



#ФИЧИ ОТ ПРОДАЖНИКОВ - 3
# from dataclasses import dataclass, field
# from typing import List, Any
#
#
# @dataclass
# class Product:
#     name: str
#     price: float = field(repr=False)
#
#
# @dataclass
# class Cart:
#     products: List = field(default_factory=list)
#     discount: float = field(init=False, default=None)
#     promo: Any = field(init=False, default=None)
#     promo_value: float = field(init=False, default=None)
#
#     def add_product(self, product, count=None):
#         if count:
#             self.products.extend([product] * count)
#         else:
#             self.products.append(product)
#
#     def get_total(self):
#         if self.discount:
#             self.promo = None
#             total = sum([product.price for product in self.products])
#             return total - (total * self.discount)
#
#         elif self.promo:
#             self.discount = None
#             total = 0
#
#             # Применяем промокод ко всем товарам, если goods_list пустой
#             if not self.promo[0].goods_list:
#                 # Промокод применяется ко всем товарам
#                 total = sum([product.price for product in self.products])
#                 return total * (1 - self.promo_value / 100)
#
#             # Применяем промокод только к определенным товарам
#             for product in self.products:
#                 if product in self.promo[0].goods_list:
#                     # Рассчитываем скидочную цену только для этого расчета
#                     discounted_price = product.price * (1 - self.promo_value / 100)
#                     total += discounted_price
#                 else:
#                     total += product.price
#             return total
#
#         else:
#             return sum([product.price for product in self.products])
#
#     def apply_discount(self, discount: int):
#         if not (isinstance(discount, int) and 1 <= discount <= 100):
#             raise ValueError('Неправильное значение скидки')
#         self.discount = discount / 100
#
#     def apply_promo(self, code):
#         if code in [promo.code_promo for promo in ACTIVE_PROMO]:
#             temp = [promo.discount_value for promo in ACTIVE_PROMO if promo.code_promo == code]
#             self.promo_value = temp[0]
#             self.promo = [promo for promo in ACTIVE_PROMO if promo.code_promo == code]
#             print(f'Промокод {code} успешно применился')
#         else:
#             self.promo = None
#             self.promo_value = 0
#             print(f'Промокода {code} не существует')
#
#
# @dataclass
# class Promo:
#     code_promo: str
#     discount_value: float
#     goods_list: list = field(default_factory=list)
#
#     def is_valid(self, value):
#         if not (isinstance(value, int) and 1 <= value <= 100):
#             self.discount_value = 0
#         self.discount_value = value


# book = Product('Книга', 100.0)
# usb = Product('Флешка', 50.0)
# pen = Product('Ручка', 10.0)
#
# ACTIVE_PROMO = [
#     Promo('new', 20, [pen]),
#     Promo('all_goods', 30),
#     Promo('only_book', 40, [book]),
# ]
#
# cart = Cart()
# cart.add_product(book, 10)
# cart.add_product(pen)
# print(cart.get_total())
#
# # Применение промокода в 40% на книгу
# cart.apply_promo('only_book')
# print(cart.get_total())




