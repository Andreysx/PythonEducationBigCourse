# Задание №4
# ✔ Создайте функцию, которая создаёт файлы с указанным расширением.
# Функция принимает следующие параметры:
# ✔ расширение
# ✔ минимальная длина случайно сгенерированного имени, по умолчанию 6
# ✔ максимальная длина случайно сгенерированного имени, по умолчанию 30
# ✔ минимальное число случайных байт, записанных в файл, по умолчанию 256
# ✔ максимальное число случайных байт, записанных в файл, по умолчанию 4096
# ✔ количество файлов, по умолчанию 42
# ✔ Имя файла и его размер должны быть в рамках переданного диапазона.
from string import ascii_lowercase
from random import choice,randint
from pathlib import Path

FOLDER_NAME = "task4_files"
AMOUNT_OF_FILES = 42
def _generate_name(min_len_name, max_len_name, extension):
    name = ''
    for _ in range(randint(min_len_name, max_len_name)):
        name += choice(ascii_lowercase)
    return f"{name}.{extension}"


def generate_files(extencion: str, min_len_name=6, max_len_name=30, min_byte=256, max_byte=4096, files_amount=42):
    folder = Path(Path().cwd() / FOLDER_NAME)
    folder.mkdir(exist_ok=True)
    for _ in range(AMOUNT_OF_FILES):
        file = Path(folder / _generate_name(min_len_name, max_len_name, extencion))
        if not file.exists():
            with open(file, 'wb') as file:
                file.write((bytes(randint(min_byte,max_byte))))