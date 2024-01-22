# Создайте класс окружность.
# Класс должен принимать радиус окружности при создании
# экземпляра.
# У класса должно быть два метода, возвращающие длину
# окружности и её площадь.
# from math import pi
#
#
# class Circle:
#     def __init__(self, radius):
#         self.radius = radius
#
#     def circle_length(self):
#         return self.radius * pi
#
#     def circle_area(self):
#         return pi * self.radius ** 2
#
# if __name__ == '__main__':
#     a = Circle(5)
#     print(a.circle_length())
#     print(a.circle_area())

# Circle = type('Circle', (object, ), {'pi': 3.14,'__init__': lambda self,
# radius: setattr(self, 'radius', radius),
# 'get_circumference': lambda self: 2 * self.pi * self.radius,
# 'get_circle_area': lambda self: self.pi * self.radius ** 2})

# Создайте класс прямоугольник.
# Класс должен принимать длину и ширину при создании
# экземпляра.
# У класса должно быть два метода, возвращающие периметр
# и площадь.
# Если при создании экземпляра передаётся только одна
# сторона, считаем что у нас квадрат.

# class Rectangle:
#     def __init__(self, a, b=None):
#         self.a = a
#         if b:
#             self.b = b
#         else:
#             self.b = a
#
#     def perimeter(self):
#      return 2 * self.a + 2 * self.b
#
#     def area(self):
#         return self.a * self.b
#
#
# if __name__ == '__main__':
#     rect_1 = Rectangle(2, 4)
#     rect_2 = Rectangle(2)
#     print(rect_1.perimeter(), rect_1.area(), rect_2.perimeter(), rect_2.area())
#
#
#
# OR
#
# class Rectangle:
#     def __init__(self, length: int | float, width: int | float = None):
#         self.length = length
#         self.width = width if width else length
#
#     def get_area(self):
#         return self.length * self.width
#
#     def get_perimeter(self):
#         return 2 * (self.width + self.length)


# Напишите класс для хранения информации о человеке: ФИО, возраст и т.п. на ваш выбор.
# У класса должны быть методы birthday для увеличения возраста на год, full_name для вывода полного ФИО и т.п. на ваш выбор.
# Убедитесь, что свойство возраст недоступно для прямого изменения, но есть возможность получить текущий возраст.

# class Person:
#     def __init__(self, name, surname, age):
#         self.name = name
#         self.surname = surname
#         self.__age = age
#
#     def birthday(self):
#         self.__age += 1
#
#     def full_name(self):
#         return (f"{self.name} {self.surname}")
#
#     def age_info(self):
#         return self.__age
#
#
# if __name__ == "__main__":
# person_01 = Person("Jhon", "Smit", 30)
# print(person_01.age_info())
# # print(person_01._age)
#
# person_01.birthday()
# print(person_01.age_info())
# print(person_01.full_name())


#
# Создайте класс Сотрудник.
# Воспользуйтесь классом человека из прошлого задания.
# У сотрудника должен быть шестизначный идентификационный номер
# и уровень доступа (остаток от суммы цифр id делённой на семь).

# class Employee(Human): - на основе подобного класса из прошлого задания
#     # id_iter = itertools.count(1_000_000_000_000_000)
#     class_id = 1_000_000_000_000_000
#
#     def __init__(self, first_name: str, last_name: str, age: int):
#     super().__init__(first_name, last_name, age)
#         # self.id = next(self.id_iter)
#         self.id = self.class_id
#         Employee.class_id += 1
#
#     def get_access_level(self):
#         return sum(map(int, str(self.id))) % 7
#
#     def __str__(self):
#         return f"{self.last_name} {self.first_name} - {self.age} лет. Уровень доступа {self.get_access_level()}"

# sdfsf






