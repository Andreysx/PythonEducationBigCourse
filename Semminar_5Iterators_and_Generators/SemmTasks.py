# Задача 1 Пользователь вводит строку из четырёх или более целых чисел, разделённых символом “/”.
# Сформируйте словарь, где:
# ● второе и третье число являются ключами
# ● первое число является значением для первого ключа
# ● четвертое и все возможные последующие числа хранятся в кортеже как значения второго ключа

# First Solution
# def task1(numbers_str: str) -> dict:
# v1, k1, k2, *v2 = map(int, numbers_str.split('/'))
# return {k1: v1, k2: tuple(v2)}
#
# data = input()
# print(task1(data))

# Second Solution

# data = input().split("/")
# res = {}
# res.update({data[1]: data[0]})
# res.update({data[2]: tuple(data[3:])})
#
# print(res)

# Задача 2 Самостоятельно сохраните в переменной строку текста.
# Создайте из строки словарь, где ключ - буква, а значение - код буквы.
# Напишите преобразование в одну строку.

# # dict comprehension
# res = {char: ord(char) for char in input()}
# # print(res)
# # Задача 3 Продолжаем развивать задачу 2.
# # Возьмите словарь, который вы получили. Сохраните его итераторатор.
# # Далее выведите первые 5 пар ключ-значение, обращаясь к итератору, а не к словарю.
#
# dict_iter = iter(res.items())
# print(next(dict_iter))
# print(next(dict_iter))
# print(next(dict_iter))
# print(next(dict_iter))
# print(next(dict_iter))
# print(next(dict_iter))
# OR
# string = 'asdfghhjk'
# result = {c: ord(c) for c in string}
# print(result)
# result_it = iter(result.items())
# for _ in range(5):
#     print(next(result_it))

#  Задача 4 Создайте генератор чётных чисел от нуля до 100.
# Из последовательности исключите числа, сумма цифр которых равна 8.
# Решение в одну строку.

# Используем генераторное выражение с распаковкой
# data = (i for i in range(0, 100 + 1, 2) if sum(int(j) for j in str(i)) != 8)
# print(*data)
#
# Задача 5  Напишите программу, которая выводит на экран числа от 1 до 100.
# При этом вместо чисел, кратных трем, программа должна выводить слово «Fizz»,
# а вместо чисел, кратных пяти — слово «Buzz».
# Если число кратно и 3, и 5, то программа должна выводить слово «FizzBuzz».
# *Превратите решение в генераторное выражение.

# Используем тернарный оператор
# data = ("FizzBuzz" if i % 15 == 0 else "Fizz" if i % 3 == 0 else "Buzz" if i % 5 == 0 else i for i in range(100+1))
# print(*data)
#
# Other solution

# def task5():
#     return ((i, 'Fizz', 'Buzz', 'FizzBuzz')[(not i % 3) + 2 * (not i % 5)] for i in range(1, 101))
# i % 3 == 0
# True = 1
# False = 0

# Задача 6 Выведите в консоль таблицу умножения от 2х2 до 9х10 как на школьной тетрадке.
# Таблицу создайте в виде однострочного генератора, где каждый элемент генератора - отдельный пример таблицы умножения.
# Для вывода результата используйте “принт” без перехода на новую строку.


# print(f"{i} * {j} = {i * j} {[for i in range(2, 10)]}")
# Решение с вложенными циклами
# for i in range(2, 10, 4):
#     for j in range(2, 10):
#         for k in range(4):
#             print(f"{i + k} * {j} = {(k + i) * j}", end="\t")
#         print()
#     print()

# Рещение от преподавателя
# Решение без генратора(однострочника)
# table_str = ""
# for i in range(2, 10, 4):
#     for j in range(2, 11):
#         for k in range(i, i + 4):
#             if k != i + 4 - 1:
#                 table_str += f'{k:>2} x {j:>2} = {k * j:>2}\t'
#             else:
#                 if j != 10:
#                     table_str += f'{k:>2} x {j:>2} = {k * j:>2}\n'
#                 else:
#                     table_str += f'{k:>2} x {j:>2} = {k * j:>2}\n\n'
#
# print(table_str, end='')
#
# Решение с помощью генератора
# data = (
#     f"{k:>2} x {j:>2} = {k * j:>2}\t"
#     if k != i + 4 - 1
#     else f"{k:>2} x {j:>2} = {k * j:>2}\n"
#     if j != 10
#     else f"{k:>2} x {j:>2} = {k * j:>2}\n\n"
#     for i in range(2, 10, 4)
#     for j in range(2, 11)
#     for k in range(i, i + 4)
# )
#
# print(*data, end="")

# Решение через строковый метод join
# print(
#     '\n\n'.join(
#         '\n'.join(
#             '\t'.join(f"{i + k} * {j} = {(k + i) * j}"
#                       for k in range(4)) for j in range(2, 10)) for i in
#             range(2, 10, 4)))

# Задача 7 Создайте функцию-генератор. Функция генерирует N простых чисел, начиная с числа 2.# Для проверки числа на простоту используйте правило: “число является простым, если делится нацело только на единицу и на себя”.


# def is_prime(number: int) -> bool:
#     for i in range(2, number // 2 + 1):
#         if not number % i:
#             return False
#     return True
#
# def task7(n, start= 2):
#     while n:
#         if is_prime(start):
#             yield start
#             n -= 1
#             start += 1
#
# print(*task7(10), sep ="\n")