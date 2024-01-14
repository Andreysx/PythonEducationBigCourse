 # Задание №1
# ✔ Напишите функцию, которая заполняет файл
# (добавляет в конец) случайными парами чисел.
# ✔ Первое число int, второе - float разделены вертикальной чертой.
# ✔ Минимальное число - -1000, максимальное - +1000.
# ✔ Количество строк и имя файла передаются как аргументы функции.
#
# from random import randint,uniform # в лекции 6 про модуль random написано
#
# MAX = 1000
# MIN = -1000
#
# def file_func(num: int, file_name: str):
#     with open(file_name,"a", encoding="utf-8" ) as file1:
#         for i in range(num):
#             file1.write(f'{randint(MIN, MAX)} | {round(randint(MIN, MAX), 2)} \n')
#
#
# if __name__ == '__main__':
#     file_func(5, "test_file_01.txt")
#
#
# #





