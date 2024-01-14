# Задание №3
# ✔ Напишите функцию, которая открывает на чтение созданные
# в прошлых задачах файлы с числами и именами.
# ✔ Перемножьте пары чисел. В новый файл сохраните
# имя и произведение:
# ✔ если результат умножения отрицательный, сохраните имя
# записанное строчными буквами и произведение по модулю
# ✔ если результат умножения положительный, сохраните имя
# прописными буквами и произведение округлённое до целого.
# ✔ В результирующем файле должно быть столько же строк,
# сколько в более длинном файле.
# ✔ При достижении конца более короткого файла,
# возвращайтесь в его начало.

# def generate_numbers_names(file_numbers, file_names, file_numbers_and_names):
#     with (
#         open (file_numbers, encoding= 'utf-8') as f_numbers,
#         open (file_names, encoding='utf-8') as f_names,
#         open (file_numbers_and_names, "w", encoding= 'utf-8') as f_names_numbers
#     ):
#         numbers = [tuple(num.rstrip().split('|')) for num in f_numbers]
#         names = [name.rstrip() for name in f_names]
#         size_numbers, size_names = len(numbers), len(names)
#         size = size_numbers if size_numbers > size_names else size_names
#         for i in range(size):
#             name = names[i % size_names]
#             a, b = map(float, numbers[i % size_numbers])
#             if (number := a * b) < 0:
#                 f_names_numbers.write(f" {name.lower()} {abs(number): .2f}\n")
#             else:
#                 f_names_numbers. write(f" {name.upper()} {round(number)}\n")
#
#
# if __name__ == '__main__':
#     generate_numbers_names("test_file_01.txt", "test_file_01.txt", "test_file_03.txt")