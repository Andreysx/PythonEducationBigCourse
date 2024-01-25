# Дорабатываем класс прямоугольник из прошлого семинара.
# Добавьте возможность сложения и вычитания.
# При этом должен создаваться новый экземпляр прямоугольника.
# Складываем и вычитаем периметры, а не длинну и ширину.
# При вычитании не допускайте отрицательных значений.
#
# Доработайте прошлую задачу.
# Добавьте сравнение прямоугольников по площади.
# Должны работать все шесть операций сравнения
# from functools import total_ordering
# The class must define one of __lt__(), __le__(), __gt__(), or __ge__(). In addition, the class should supply an __eq__() method.
#
#
# @total_ordering
class Rectangle:
    def __init__(self, width, height=None):
        self.width = width
        self.height = height if height else width

    def perimeter(self):
        return 2 * (self.width + self.height)

    def area(self):
        return self.width * self.height

    def __add__(self, other):
        if isinstance(other, Rectangle):
            per = self.perimeter() + other.perimeter()
            min_side = min(self.width, self.height, other.width, other.height)
            second_side = per / 2 - min_side
            return Rectangle(min_side, second_side)
        raise TypeError("Не поддерживается сложение с этим типом")

    def __sub__(self, other):
        if isinstance(other, Rectangle):
            per = abs(self.perimeter() - other.perimeter())
            min_side = min(self.width, self.height, other.width, other.height)
            second_side = per / 2 - min_side
            return Rectangle(min_side, second_side)
        raise TypeError("Не поддерживается вычитание с этим типом")

    def __str__(self):
        return f"{self.width = }, {self.height = }, {self.perimeter() = }, {self.area() = }"

    def __eq__(self, other):
        if isinstance(other, Rectangle):
            return self.area() == other.area()
        raise TypeError("Не поддерживается сравнение с этим типом")

    def __lt__(self, other):
        if isinstance(other, Rectangle):
            return self.area() < other.area()
        raise TypeError("Не поддерживается сравнение с этим типом")

    def __le__(self, other):
        if isinstance(other, Rectangle):
            return self.__lt__(other) or self.__eq__(other)
        raise TypeError("Не поддерживается сравнение с этим типом")


if __name__ == '__main__':
    r1 = Rectangle(2, 3)
    r2 = Rectangle(3, 5)
    r3 = r1 - r2
    print(r1, r2, r3, sep='\n')
    print(f"{r1 > r2 = }")
    print(f"{r1 < r2 = }")
    print(f"{r1 == r2 = }")
    print(f"r1 != r2 = {r1 != r2}")
    print(f"{r1 <= r2 = }")
    print(f"{r1 >= r2 = }")