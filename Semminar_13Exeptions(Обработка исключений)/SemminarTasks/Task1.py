# Создайте функцию, которая запрашивает числовые данные от пользователя до тех пор,
# пока он не введёт целое или вещественное число.
# Обрабатывайте не числовые данные как исключения.
#
# def task1() -> float | int:
#     while True:
#         num = input("Введите целое или вещественное число: ")
#         try:
#             num = int(num) if num.isdigit() else float(num)
#         except ValueError:
#             print(f"{num} не число!")
#         else:
#             return num
#
#
# if __name__ == '__main__':
#     print(task1())