# ● Чтение в словарь
# Помимо сохранения таблицы в список можно использовать для хранения словарь.
# Ключи словаря — названия столбцов, значения — очередная строка файла CSV.
# Прочитаем файл biostats_tab.csv из примера выше, но не в список, а в словарь.
# Воспользуемся классом DictReader.
#
# import csv
# with open('biostats_tab.csv', 'r', newline='') as f:
#     csv_file = csv.DictReader(f, fieldnames=["name", "sex","age", "height", "weight", "office"],
#         restkey="new", restval="MainOffice", dialect='excel-tab', quoting=csv.QUOTE_NONNUMERIC)
#     for line in csv_file:
#         print(f'{line = }')
#         print(f'{line["name"] = }\t{line["age"] = }')
#
# Если передать список строк в параметр fieldnames, они будут использоваться для
# ключей словаря, а не первая строка файла. В нашем примере передан “лишний”
# ключ count. Т.к. в таблице нет шестого столбца, ему было присвоено значение из
# параметра restval.
#
# import csv
# with open('biostats_tab.csv', 'r', newline='') as f:
#     csv_file = csv.DictReader(f, fieldnames=["name", "sex","age", ], restkey="new", restval="Main Office",
#                               dialect='excel-tab',quoting=csv.QUOTE_NONNUMERIC)
#     for line in csv_file:
#         print(f'{line = }')
#         print(f'{line["name"] = }\t{line["age"] = }')
#
# Если количество ключей оказывается меньше, чем столбцов, недостающий ключ
# берётся из параметра restkey. При этом все столбцы без ключа сохраняются как
# элементы списка в restkey ключ.
# ● Запись из словаря
# Для записи содержимого словаря в CSV используют класс DictWriter. Его параметры
# схожи с рассмотренными выше параметрами DictReader.
#
# import csv
# from typing import Iterator
# with (
#     open('biostats_tab.csv', 'r', newline='') as f_read,
#     open('biostats_new.csv', 'w', newline='', encoding='utf-8') as f_write
# ):
#     csv_read: Iterator[dict] = csv.DictReader(f_read,
#     fieldnames=["name", "sex", "age", "height", "weight", "office"],restval="MainOffice",
#                                               dialect='excel-tab', quoting=csv.QUOTE_NONNUMERIC)
#     csv_write = csv.DictWriter(f_write, fieldnames=["id", "name","office", "sex", "age", "height", "weight"],
#                                dialect='excel-tab',quoting=csv.QUOTE_ALL)
#     csv_write.writeheader()
#     all_data = []
#     for i, dict_row in enumerate(csv_read):
#         if i != 0:
#             dict_row['id'] = i
#             dict_row['age'] += 1
#             all_data.append(dict_row)
#     csv_write.writerows(all_data)
#
# Класс DictWriter получил список полей для записи, где добавлено новое поле id. В
# качестве диалекта выбран excel с табуляцией. В параметре quoting указали, что все
# значения стоит заключать в кавычки.
# Новый для нас метод writeheader сохранил первую строку с заголовками в том
# порядке, в котором мы их перечислили в параметре fieldnames. Далее мы работаем
# с элементами словаря и формируем список словарей для одноразовой записи в
# файл.
# 🔥 Важно! Обратите внимание на импорт объекта Iterator из модуля typing.
# При написании кода IDE подсвечивала возможные ошибки, так как не
# понимала что за объект csv_read. Запись csv_read: Iterator[dict] = … сообщает,
# что мы используем объект итератор, который возвращает словари. После
# уточнения типа IDE исключила подсветку “ошибок”.