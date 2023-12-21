# Напишите функцию, которая принимает строку текста.
# Сформируйте список с уникальными кодами Unicode
# каждого символа введённой строки отсортированный по убыванию.

# def task2(text):
#     return sorted([ord(char) for char in text], reverse=True)
#
# task2()

# Функция получает на вход строку из двух чисел через пробел.
# Сформируйте словарь, где ключом будет символ из Unicode, а значением - целое число.
# Диапазон пар ключ-значение от наименьшего из введённых пользователем чисел до наибольшего включительно

# def create_unicode_dict(in_str):
#
#     numbers = [int(num) for num in in_str.split()]
#     num_min, num_max = min(numbers), max(numbers)
#     unicode_dict = {chr(code): code for code in range(num_min, num_max + 1)}
#     return unicode_dict
#
#
# input_nums = input("Enter two numbers with space: ")
#
# print(create_unicode_dict(input_nums))


# Функция получает на вход список чисел.
# Отсортируйте его элементы in place без использования встроенных в язык сортировок.
# Как вариант напишите сортировку пузырьком.
# Её описание есть в википедии.

# def sorting(array: list):
#     for i in range(len(array) - 1):
#         for j in range(len(array) - 1 - i):
#             if array[j] > array[j + 1]:
#                 array[j], array[j + 1] = array[j + 1], array[j]
#     return array
#
# print(sorting([1, 3, 4, 124, 1, 4]))
# # input_numbers = list(input("Введите произвольный набор чисел через пробел: "))
# # print(sorting(input_numbers))
#

# Функция принимает на вход три списка одинаковой длины:
# имена str,
# ставка int, п
# ремия str с указанием процентов вида “10.25%”.
# Вернуть словарь с именем в качестве ключа и суммой премии в качестве значения.
# Сумма рассчитывается как ставка умноженная на процент премии


# def bonuses(names: list[str], salaries: list[int], percents: list[str]) -> dict[str: int|float]:
#     result = {}
#     for name, salary, percent in zip(names, salaries, percents):
#         result[name] = salary * float(percent[:-1]) * 0.01
#     return result
#
# print(bonuses(['Василий', 'Виктор'], [10_000, 25_000], ['10.25%', '15.2%']))

# Функция получает на вход список чисел и два индекса. Вернуть сумму чисел между между переданными индексами.
# Если индекс выходит за пределы списка, сумма считается до конца и/или начала списка.
# Если нижняя граница меньше нуля, суммируем от начала.
# Если верхняя граница больше длины списка, до конца.

# def find_sum(num_arr: list[int], start_index: int, end_index: int) -> int:
#     # if start_index < 0:
#         # start_index = 0
#     # if end_index > len(num_arr):
#         # end_index = len(num_arr)
#     return sum(num_arr[start_index: end_index + 1])
#
#
# my_arr = [3, 5, 2]
# print(find_sum(my_arr, 2,1))

# Функция получает на вход словарь с названием компании
# в качестве ключа и списком с доходами и расходами (3-10 чисел) в качестве значения.
# Вычислите итоговую прибыль или убыток каждой компании.
# Если все компании прибыльные, верните истину, а если хотя бы одна убыточная - ложь.

# def task7(companies: dict[str: tuple[list[int], list[int]]]) -> bool:
#     return all(sum(income) - sum(expenses) > 0 for income, expenses in companies.values())
#
# companies = {"Sber": ([2, 4, 2, 6, 1, 5], [1, 5, 1, 3, 5]),
#              "VTB": ([2, 4, 2, 5, 2, 1, 5], [2, 3, 1, 7, 6]),
#              "GAZPROM": ([2, 5, 1, 6, 2, 3], [2, 5, 1, 3, 7])}
#
# print(task7(companies))

# Создайте несколько переменных заканчивающихся и не оканчивающихся на “s”.
# Напишите функцию, которая при запуске заменяет содержимое переменных оканчивающихся на s
# (кроме переменной из одной буквы s) на None.
# Значения не удаляются, а помещаются в одноимённые переменные без s на конце.
