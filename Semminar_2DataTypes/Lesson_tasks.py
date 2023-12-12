# from sys import getsizeof
# import decimal
# from math import pi, sqrt


# def task1():
# a, b, c, d, e, f, g = "Hello world", 2, 2.5, [], (), {}, set()
# for item in (a, b, c, d, e, f, g):
# print(item, type(item))
# a = 1
# b = "dsfgsf"
# c = 3.13
# print(type(a))
# print(type(b))
# print(type(c))
# print(id(a))
# print(id(b))
# print(id(c))

# Создайте в переменной data список значений разных типов перечислив их через запятую внутри квадратных скобок.
# Для каждого элемента в цикле выведите:
# ● порядковый номер начиная с единицы
# ● значение
# ● адрес в памяти
# ● размер в памяти
# ● хэш объекта
# ● результат проверки на целое число только если он положительный
# ● результат проверки на строку только если он положительный
# *Добавьте в список повторяющиеся элементы и сравните на результаты.

# def task2():
#     data = [1, "hello" , 2.5, 1]
#     result = []
#     for i, item in enumerate(data, start = 1):
#         print(i, item, id(item), getsizeof(item), hash(item), isinstance(item, str), item in result)
#         result.append(item)
#
# task2()


# Напишите программу, которая получает целое число и возвращает его двоичное,
# восьмеричное строковое представление.
# Функции bin и oct используйте для проверки своего результата.
# *Дополнительно
# ● Попробуйте избежать дублирования кода в преобразованиях к разным системам счисления
# ● Избегайте магических чисел
# ● Добавьте аннотацию типов где это возможно

# def task3():
#     DEAFULTNUMBER = "237"
#     BIN, OCT = 2, 8
#     number: int = int(input("Введите число ") or DEAFULTNUMBER)
#     print(bin(number), oct(number))
#     print(trans(number, BIN), trans(number, OCT))
#
# def trans(num: int, n: int) -> int:
#     result = []
#     while num:
#         result.append(num % n)
#         num //= n
#     return sum(result[i] * 10 ** i for i in range(len(result)))
# # result = [str(item) for item in result[::-1]]
# # return "".join(result)
# task3()

# Напишите программу, которая вычисляет площадь круга и длину окружности по введённому диаметру.
# Диаметр не превышает 1000 у.е.
# Точность вычислений должна составлять не менее 42 знаков после запятой.

# def task4():
#     decimal.getcontext().prec = 42
#     diameter = decimal.Decimal(input("Введите диаметр: "))
#     PI = decimal.Decimal(pi)
#     print("Длина окружности равна", PI * diameter)
#     print("Площадь окружности равна", PI * (diameter / 2) ** 2)
#
# task4()

# Напишите программу, которая решает квадратные уравнения даже если дискриминант отрицательный.
# Используйте комплексные числа для извлечения квадратного корня.

# def task5():
#     a, b, c = int(input("Введите а: ")), int(input("Введите b: ")), int(input("Введите с: "))
#     d = b ** 2 - 4 * a * c
#     if d > 0:
#         print((-1 * b - sqrt(d)) / (2 * a))
#         print((-1 * b + sqrt(d)) / (2 * a))
#     elif d == 0:
#         print(-1 * (b / (2 * a)))
#     else:
#         d = complex(d, 0)
#         print("Complex sqrt", (-1 * b - d ** 0.5) / (2 * a))
#         print("Complex sqrt", (-1 * b + d ** 0.5) / (2 * a))
#
# task5()



