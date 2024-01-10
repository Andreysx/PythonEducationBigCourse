# Создайте модуль с функцией внутри. Функция принимает на вход три целых числа: нижнюю и верхнюю границу и количество попыток.
# Внутри генерируется случайное число в указанных границах и пользователь должен угадать его за заданное число попыток.
# Функция выводит подсказки “больше” и “меньше”. Если число угадано, возвращается истина, а если попытки исчерпаны - ложь.
# Улучшаем задачу 2. Добавьте возможность запуска функции “угадайки” из модуля в командной строке терминала.
# Строка должна принимать от 1 до 3 аргументов: параметры вызова функции.
# Для преобразования строковых аргументов командной строки в числовые параметры используйте генераторное выражение.

from random import randint
from sys import argv


def guess_number(max_value: int, min_value: int = 0, amount_of_tries: int = 3) -> bool:
    print(f"Угадайте число в диапазоне {min_value}..{max_value} c {amount_of_tries} попыток")
    number = randint(min_value, max_value)
    for i in range(1, amount_of_tries + 1):
        try_number = int(input(f"Попытка №{i}: \nВведите число: "))
        if number == try_number:
            return True
        print("Меньше" if try_number > number else "Больше")
    return False


if __name__ == '__main__':
    numbers = map(int, argv[1:])
    # print(argv, numbers)
    print(guess_number(*numbers))