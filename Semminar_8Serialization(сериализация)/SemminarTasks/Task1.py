# Вспоминаем задачу 3 из прошлого семинара.
# Мы сформировали текстовый файл с псевдо именами и произведением чисел.
# Напишите функцию, которая создаёт из созданного ранее файла новый с данными в формате JSON.
# Имена пишите с большой буквы. Каждую пару сохраняйте с новой строки.

import json

def create_json_from_file(file_read: str, file_write: str):
    with (
        open(file_read, encoding='utf-8') as f_read,
        open(file_write, "w", encoding='utf-8') as f_write
    ):
        result = [{"name": name.capitalize(), "number": int(number) if number.isdigit() else float(number)}
            for name, number in (line.rstrip().split() for line in f_read)]
    # print(*result, sep="\n")
    json.dump(result, f_write, indent=2, ensure_ascii=False)

