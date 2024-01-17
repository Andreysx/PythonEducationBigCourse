# Напишите функцию, которая в бесконечном цикле запрашивает имя, личный идентификатор и уровень доступа (от 1 до 7).
# После каждого ввода добавляйте новую информацию в JSON файл.
# Пользователи группируются по уровню доступа.
# Идентификатор пользователя выступает ключём для имени.
# Убедитесь, что все идентификаторы уникальны независимо от уровня доступа.
# При перезапуске функции уже записанные в файл данные должны сохраняться.

import os
import json


def __create_json(file_name: str, dict_: dict):
    with open(file_name, 'w', encoding='utf-8') as f:
        json.dump(dict_, f, indent=2, ensure_ascii=False)


def __update_json(file_name: str, name: str, id_: str, level: str):
    with open(file_name, encoding='utf-8') as f:
        try:
            file_dict = json.load(f)
        except json.decoder.JSONDecodeError:
            file_dict = {}
    ids = []
    for lvl in file_dict:
        for idd in file_dict[lvl]:
            ids.append(idd)
    if id_ in ids:
        raise ValueError(f"Такой id {id_} уже существует")
    file_dict[level] = file_dict.get(level, {}) | {id_: name} ## | В данном случае склейка словарей
    # print(file_dict, type(file_dict))
    __create_json(file_name, file_dict)


def task2(file_name):
    while True:
        name = input("Введите имя: ") or "Илья" ## В случае пустого ввода пользователем вернется Илья
        id_ = input("Введите личный идентификатор: ") or "10"
        level = input("Введите уровень доступа (от 1 до 7): ") or "5"
        if not os.path.exists(file_name):
            __create_json(file_name, {level: {id_: name}})
        else:
            try:
                __update_json(file_name, name, id_, level)
            except ValueError as e:
                print(e)

        exit_choice = input('Для завершения введите "exit", для продолжения нажмите Enter: ')
        if exit_choice.lower() == 'exit':
            break





task2("task2.json")