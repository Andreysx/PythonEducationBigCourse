# Три друга взяли вещи в поход. Сформируйте словарь, где ключ - имя друга, а значение - кортеж вещей.
# Ответьте на вопросы:
# ● какие вещи взяли все три друга
# ● какие вещи уникальны, есть только у одного друга
# ● какие вещи есть у всех друзей кроме одного и имя того, у кого данная вещь отсутствует
# Для решения используйте операции с множествами. Код должен расширяться на любое большее количество друзей.
from functools import reduce

# import tour as tour


def every_one_have(tour: dict) -> set:
    return reduce(lambda a, b: set(a) & set(b), tour.values())

def only_one_have(tour: dict) -> dict:
    result = {}
    for name, items in tour.items():
        temp_set = set(items)
        for key, value in tour.items():
            if key != name:
                temp_set -= set(value)
            if temp_set:
                result[name] = temp_set
    return result


def every_one_have_except_one(tour: dict) -> dict:
    all_items = reduce(lambda a, b: set(a) | set(b), tour.values())
    result = {}
    for item in all_items:
        count, full_name = 0, ''
        for name, items in tour.items():
            if item not in items:
                count += 1
            if count > 1:
                break
        full_name = name
        if count == 1:
            result[item] = full_name
    return result


def task8():
    tour = {"Иван": ("Палатка", "Спальный мешок", "Термос", "Спички", "Еда"),
        "Дмитрий": ("Палатка", "Спальный мешок", "Нож", "Еда"),
        "Василий": ("Спальный мешок", "Еда", "Аптечка", "Посуда")}
    print("У всех есть", ', '.join(every_one_have(tour)))
# for name, items in only_one_have(tour).items():
#     print(f"Только у {name} есть {', '.join(items)}")
#
#     for item, name in every_one_have_except_one(tour).items():
#     print(f"У всех есть {item}, кроме {name}")