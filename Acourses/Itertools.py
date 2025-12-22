# from itertools import cycle, repeat, count
# from collections import deque
#
# #
# #
# def infinity_generate(iterable, offset=0):
#     sequence = deque(iterable)
#     sequence.rotate(-offset)
#     print(sequence)
#     return cycle(sequence)
# #
# count = 0
# for i in infinity_generate('ABCDEF', 1):
#     print(i)
#     count += 1
#     if count > 10:
#         break


# d = deque([1, 2, 3, 4, 5])
# print(d.rotate(1))


# import itertools
#
# # Создаем бесконечную последовательность
# # четных чисел начиная с 1
# odd_numbers = itertools.count(4, 2)
#
# # Печатаем все четные числа, которые меньше 35
# for number in odd_numbers:
#     if number <= 35:
#         print(number)
#     else:
#         break


# import itertools
#
# bools = [True, False]
# ints = [7, 8, 10]
#
# for value in itertools.product(bools, ints, repeat=3):
#     print(value)
#
# import itertools
#
# suits = ["\u2663", "\u2665", "\u2666", "\u2660"]
# ranks = ['2', '3', '4', '5', '6', '7', '8',
#          '9', '10', 'J', 'Q', 'K', 'A']
#
# combinations = itertools.product(ranks, suits)
#
# for r, s in combinations:
#     print(f"{r} of {s}")

# from itertools import product


# def get_binary(N):
#     for seq in product('01', repeat=N):
#         print(''.join(seq))
#
#
# get_binary(3)

# def get_binary_advanced(n, k):
#     for seq in product('01', repeat=n):
#         if seq.count('1') == k:
#             print(''.join(seq))
#
#
# # get_binary_advanced(3, 2)
# get_binary_advanced(4, 2)

#
# import itertools
#
#
# def time_periods_8_17():
#     hours = range(8, 17)
#     minutes = range(60)
#     seconds = range(60)
#     time_periods = itertools.product(hours, minutes, seconds)
#
#     for h, m, s in time_periods:
#         print(f"{h:02}:{m:02}:{s:02}")
#
# time_periods_8_17()

#
# from dataclasses import dataclass
# import itertools
#
#
# @dataclass
# class Human:
#     name: str
#     age: int
#
#
# @dataclass
# class Man(Human):
#     gender: str = 'M'
#
#
# @dataclass
# class Woman(Human):
#     gender: str = 'W'
#
#
# def check_match(men: list, women: list):
#     combinations = itertools.product(men, women)
#     for m, w in combinations:
#         w_age_min = m.age // 2 + 7
#         w_age_max = (m.age - 7) * 2
#         if w_age_min <= w.age <= w_age_max:
#             print(f'Пользователю {m.name} подходит {w.name}')
#
#
# mans = [Man(name='Федосий', age=40), Man(name='Фирс', age=69)]
#
# women = [Woman(name='Екатерина', age=46), Woman(name='Ангелина', age=48),
#          Woman(name='Акулина', age=33), Woman(name='Любовь', age=20),
#          Woman(name='Синклитикия', age=29)]
#
# check_match(mans, women)


#
# import itertools
#
# def perm(n):
#     perm_iterator = itertools.permutations(range(1, n + 1))
#     return perm_iterator
#
#
# for el in perm(3):
#     print(''.join(map(str, el)))

# from itertools import permutations
#
# for i in permutations(range(1, int(input()) + 1)):
#     print(*i, sep='')


import itertools
from string import ascii_uppercase

# n = int(input())
# letters = ascii_uppercase[:n]
# for el in itertools.permutations(letters):
#     print(*el, sep=' ')
#


# def permutations(n, k):
#     letters = ascii_uppercase[:n]
#     count = 0
#     for el in itertools.permutations(letters):
#         count += 1
#         if count == k:
#             print(*el, sep=' ')
#             break
#
# n = int(input())
# k = int(input())
#
# permutations(n, k)

#
# n = 10
# res = 1
# for i in range(1, n+1):
#     res *= i
# print(res)

# from pathlib import Path
#
# current_path = Path.cwd()
#
# print(current_path)
#
# home_path = Path.home()
#
# print(home_path)

#
# Вот несколько способов распаковать вложенный список в одномерный:
# from itertools import chain
#
# nested = [[1, 2], [3, 4], [5, 6]]
# flat = list(chain.from_iterable(nested))
# print(flat)  # [1, 2, 3, 4, 5, 6]

