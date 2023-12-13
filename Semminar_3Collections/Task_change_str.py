# Пользователь вводит данные. Сделайте проверку данных и преобразуйте если возможно в один из вариантов ниже:
# ● целое положительное число
# ● вещественное положительное или отрицательное число
# ● строку в нижнем регистре, если в строке есть хотя бы одна заглавная буква
# ● строку в верхнем регистре в остальных случаях

def is_float(text):
    if text and text[0] == '-':
        text = text[1:]
    if text[1:].replace(",", ".").count('.') == 1:
        for ch in text.replace(".", ""):
            if not ch.isdigit():
                return False
        return True
    return False


def is_on_upper(text):
    for letter in text:
        if letter.isupper():
            return True
    return False


def task2():
    my_input = input("Введите текст: \n")
    if my_input.isdigit() and int(my_input) > 0:
        print("целое положительное число")
    elif (my_input.isdigit() and int(my_input) < 0) \
             or (is_float(my_input) and float(my_input) < 0):
            print("отрицательное число")
    elif is_float(my_input):
        print("вещественное положительное")
    elif is_on_upper(my_input):
        print("строку в нижнем регистре, если в строке есть хотя бы одна заглавная буква")
    else:
        print("строку в верхнем регистре в остальных случаях")


task2()




# ИЛИ
# проверка на совпадение с шаблоном, это решение с регулярными выражениями
# import re
#
# n = input()
#
# if re.fullmatch(r'\d+', n):
#     n = int(n)
#     print(type(n), n)
# elif re.fullmatch(r'-?\d+\.\d+', n):
#     n = float(n)
#     print(type(n), n)
# elif re.search(r'[A-Zа-я]', n):
#     n = n.lower()
#     print(type(n), n)
# else:
#     n = n.lower()
#     print(type(n), n)
