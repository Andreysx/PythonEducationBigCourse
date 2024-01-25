# Создайте класс МояСтрока
# где будут доступны все возможности str
# и дополнительно хранится имя автора строки и время создания (time.time)

import time


class MyString(str):
    """Create class MyString with (str) possibilities"""

    def __new__(cls, value, name, *args, **kwargs):
        inctance = super().__new__(cls,value)
        inctance.name = name
        inctance.time = time.time()
        return inctance


if __name__ == '__main__':
    string_1 = MyString("qwerty", name="Andrey")
    print(string_1, string_1.name, string_1.time)
    print(string_1.upper(), string_1.name, string_1.time)

