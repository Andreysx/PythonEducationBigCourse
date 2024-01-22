# Задача 3 Напишите декоратор, который сохраняет в json файл параметры декорируемой функции
# и результат, который она возвращает.
# При повторном вызове файл должен расширяться, а не перезаписываться.
# ● Каждый ключевой параметр сохраните как отдельный ключ json словаря.
# ● Для декорирования напишите функцию, которая может принимать как позиционные, так и ключевые аргументы.
# ● Имя файла должно совпадать с именем декорируемой функции.

import json


def read_from_file(file_name):
    with open(file_name, encoding='utf-8') as f:
        return json.load(f)


def save_to_file(diction: dict, file_name):
    with open(file_name, 'w', encoding='utf-8') as f:
        json.dump({f"{k}": v for k, v in diction.items()}, f, ensure_ascii=False, indent=2)


def decorator(func):
    result = {}

    def inner(a: int, b: int, *args, **kwargs):
        nonlocal result
        result = read_from_file(func.__name__ + ".json")
        if (a, b) not in result:
            result[(a, b)] = func(a, b)
            save_to_file(result | kwargs | {"args": args}, func.__name__ + ".json")
        return result

    return inner


@decorator
def task3(a: int, b: int, *args, **kwargs):
    return a + b


if __name__ == '__main__':
    while True:
        a = int(input("Введите первое число: "))
        b = int(input("Введите второе число: "))
        print(task3(a, b, 2, 3, 10, z=5, l="23"))