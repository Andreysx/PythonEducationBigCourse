# Задание №2
# ✔ Напишите функцию, которая генерирует
# псевдоимена.
# ✔ Имя должно начинаться с заглавной буквы,
# состоять из 4-7 букв, среди которых
# обязательно должны быть гласные.
# ✔ Полученные имена сохраните в файл.

from random import choice,randint
from string import ascii_lowercase
## ascii_lowercase - фактически алфавит из модуля string
import re
##модуль регулярных выражений
#
#
# VOWELS = "sdiyks"
# MIN_LEN_NAME = 4
# MAX_LEN_NAME = 7
#
# def generate_names(file_name: str, amount: int):
#     with open(file_name, 'a', encoding='utf-8') as f:
#         while amount:
#             name = ''
#             for _ in range(randint(MIN_LEN_NAME, MAX_LEN_NAME)):
#                 name += choice(ascii_lowercase)
#             for ch in VOWELS:
#                 if ch in name:
#                     f.write(f"{name.capitalize()}\n")
#                     amount -= 1
#                     break
#             # if re.search(f"[{VOWELS}]", name):
#             #     f.write((f"{name.capitalize()}\n"))
#             #     amount -= 1 - решение через регулярные выражения
#
#
# if __name__ == '__main__':
#     generate_names("test_file_02.txt", 8)