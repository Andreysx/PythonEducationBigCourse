# Дорабатываем задачу 1.
# Превратите внешнюю функцию в декоратор.
# Он должен проверять входят ли переданные в
# функцию-угадайку числа в диапазоны [1, 100] и [1, 10].
# Если не входят, вызывать функцию со случайными числами из диапазонов.

from random import randint
from typing import Callable


def decorator(func):
    def inner(guess, amount_of_tries):
        if guess < 1 or guess > 100:
            guess = randint(1, 100)
        if amount_of_tries < 1 or amount_of_tries > 10:
            amount_of_tries = randint(1, 10)

        return func(guess, amount_of_tries)

    return inner


@decorator
def good_num(num1, num2):
    for i in range(num2):
        temp = int(input("Введите ваш вариант: "))
        if temp == num1:
            print("Вы победили: ")
            print("Попытка #", i + 1)

    print(f"Загаданое число = {num1}")

    return f"Попытки закончились. Загаданое число = {num1}"


num1 = int(input("Введите от 1 до 100: "))
num2 = int(input("Введите кол-во попыток от 1 до 10: "))

good_num(num1, num2)