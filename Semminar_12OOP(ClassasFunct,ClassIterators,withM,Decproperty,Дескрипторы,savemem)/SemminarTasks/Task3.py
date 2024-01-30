# # Создайте класс-генератор.
# # Экземпляр класса должен генерировать факториал числа в диапазоне от start до stop с шагом step.
# # Если переданы два параметра, считаем step=1.
# # Если передан один параметр, также считаем start=1
#
# from math import factorial
#
#
# class Fact:
#     def __init__(self, num, *args):
#         if not args:
#             self.start = 1
#             self.stop = num
#             self.step = 1
#         elif len(args) == 1:
#             self.start = num
#             self.stop = args[0]
#             self.step = 1
#         else:
#             self.start = num
#             self.stop = args[0]
#             self.step = args[1]
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if self.start > self.stop and self.step > 0:
#             raise StopIteration
#         elif self.start < self.stop and self.step < 0:
#             raise StopIteration
#         else:
#             f = factorial(self.start)
#             self.start += self.step
#         return f
#
#
# if __name__ == '__main__':
#     f = Fact(10, 2, -2)
#     for i in f:
#         print(i)