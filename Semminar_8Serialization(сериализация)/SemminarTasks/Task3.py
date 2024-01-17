# # Напишите функцию, которая сохраняет созданный в прошлом задании(2) файл в формате CSV.
#
# import json
# import csv
#
#
# def task3(json_file, csv_file):
#     with (
#         open(json_file, encoding='utf-8') as json_file,
#         open(csv_file, 'w', newline='', encoding='utf-8') as csv_file
#     ):
#
#         dictionary: dict = json.load(json_file)
#         csv_writer = csv.DictWriter(csv_file, fieldnames=["id", "name", "level"], quoting=csv.QUOTE_NONNUMERIC)
#         csv_writer.writeheader()
#         for level in dictionary:
#             for id_, name in dictionary[level].items():
#                 csv_writer.writerow({"id": id_, "name": name, "level": level})
#
#
# task3("task2.json","task3.csv")