# Доработайте класс прямоугольник из прошлых семинаров.
# Добавьте возможность изменять длину и ширину прямоугольника
# и встройте контроль недопустимых значений (отрицательных).
# Используйте декораторы свойств.

# В __init__ можно делать много поправок
# По сути геттер и сеттер вызывается прям в констукторе класса__init__


class Rectangle:
    def __init__(self, a, b=None):
        self.a = a
        if b:
            self.b = b
        else:
            self.b = a

    def perimeter(self):
        return 2 * self._a + 2 * self._b

    def area(self):
        return self._a * self._b

    def __add__(self, other):
        new_p = self.perimeter() + other.perimeter()
        return Rectangle(new_p / 4)

    def __sub__(self, other):
        new_p = self.perimeter() - other.perimeter()
        if new_p < 0:
            raise ValueError('Получился отрицательный периметр')
        else:
            return Rectangle(new_p / 4)

    def __gt__(self, other):
        return self.area() > other.area()

    def __eq__(self, other):
        return self.area() == other.area()

    def __ge__(self, other):
        return self.area() >= other.area()

    @property # getter
    def a(self):
        return self._a

    @a.setter # setter
    def a(self, value):
        if value < 0:
            raise ValueError('Длина не может быть отрицательной')
        self._a = value

    @property # getter
    def b(self):
        return self._b

    @b.setter # setter
    def b(self, value):
        if value < 0:
            raise ValueError('Длина не может быть отрицательной')
        self._b = value


if __name__ == '__main__':
    r = Rectangle(2, 5)
    r.a = 5
    r.b = 6
    print(r.a, r.b)
    # r.a = -5