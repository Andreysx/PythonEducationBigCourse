import argparse

parser = argparse.ArgumentParser(description='Мой парсер')
parser.add_argument('path', help='Путь к файлу')

args = parser.parse_args()  # сохраняем результат метода parse_args

print(type(args))  # Посмотрим на тип значения
print(args)  # Посмотрим на само значение

file_path = args.path  # Получаем значение атрибута path
print(file_path)