# Прочитайте созданный в прошлом задании csv файл без использования csv.DictReader.
# Дополните id до 10 цифр незначащими нулями.
# В именах первую букву сделайте прописной.
# Добавьте поле хеш на основе имени и идентификатора.
# Получившиеся записи сохраните в json файл, где каждая строка csv файла представлена как отдельный json словарь.
# Имя исходного и конечного файлов передавайте как аргументы функции.

import csv
import json


def task4(cvs_file, json_file):
    with open(cvs_file, newline='', encoding='utf-8') as f:
        csv_reader = csv.reader(f)
        result = []
        for i, line in enumerate(csv_reader):
            if i:
                id_ = line[0].zfill(10)
                name = line[1].capitalize()
                hash_ = hash(line[1] + line[0])
                level = line[2]
                dict_ = {"id" : id_, "name": name, "level": level, "hash": hash_}
                result.append(dict_)

    with open(json_file, 'w', encoding='utf-8') as f:
        json.dump(result, f, indent=2, ensure_ascii=False)

task4("task3.csv", "task4.json")