# Создайте класс-функцию, который считает факториал числа при вызове экземпляра.
# Экземпляр должен запоминать последние k значений.
# Параметр k передаётся при создании экземпляра.
# Добавьте метод для просмотра ранее вызываемых чисел и их факториалов.

# from math import factorial
#
# class Fact:
#     def __init__(self, k):
#         self.k = k
#         self.history = []
#
#     def __call__(self, num):
#         self.history.append((num, factorial(num)))
#         if len(self.history) > self.k:
#             self.history.pop(0)
#         return self.history[-1][1]
#
#     def get_history(self):
#         return self.history
#
#
# if __name__ == '__main__':
#     f = Fact(5)
#     print(f(5), f(4), f(3), f(1), f(5), f(8), f(10), f.get_history(), sep="\n")

# Доработаем задачу 1.
# Создайте менеджер контекста, который при выходе сохраняет значения в JSON файл.


