# Вспоминаем задачу из семинара 8 про сериализацию данных,
# где в бесконечном цикле запрашивали имя, личный идентификатор и уровень доступа (от 1 до 7) сохраняя информацию в JSON файл.
# Напишите класс пользователя, который хранит эти данные в свойствах экземпляра.
# Отдельно напишите функцию, которая считывает информацию из JSON файла и формирует множество пользователей.

import json

FILE_NAME = "users.json"


class User:
    users = {}

    def __init__(self, name, id_, level):
        self.name = name
        self.id = id_
        self.level = level

    def __str__(self):
        return f"Имя: {self.name}, id: {self.id}, level: {self.level}"


def get_users(file_name: str) -> set:
    with open(file_name, encoding='utf-8') as f:
        result = set()
        try:
            file_dict = json.load(f)
        except json.decoder.JSONDecodeError:
            file_dict = {}
        for lvl, dict_ in file_dict.items():
            for id_, name in dict_.items():
                result.add(User(name, id_, lvl))
    return result


if __name__ == '__main__':
    print(*get_users(FILE_NAME), sep="\n")