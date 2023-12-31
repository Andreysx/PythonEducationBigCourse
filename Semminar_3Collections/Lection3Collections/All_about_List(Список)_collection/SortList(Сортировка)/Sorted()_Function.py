# Сортировка списков
# Одна из частых операций при работе со списками их сортировка. Python позволяет
# отсортировать список на месте, inplace, т.е. не создавая копию. А можно создать
# копию отсортированного списка как отдельный объект.
# 🔥 Важно! При сортировке элементы списка должны быть одного типа.
# Иначе Python может не понять как сравнивать между собой элементы разных
# типов и вызовет ошибку.
my_list = ['H', 'e', 'l', 'l', 'o', 1, 3, 5, 7]
my_list.sort() # TypeError: '<' not supported between instances of 'int' and 'str'
res = sorted(my_list) # TypeError: '<' not supported between instances of 'int' and 'str'
# Функция sorted()
# Функция sorted принимает на вход любую коллекцию по которой можно
# итерироваться и возвращает отсортированный список.
# 🔥 Важно! Функция sorted может принимать не только списки, но и другие
# последовательности: строки, множества, кортежи, словари и т.п.. При этом
# функция всегда возвращает список.
my_list = [4, 8, 2, 9, 1, 7, 2]
sort_list = sorted(my_list)
print(my_list, sort_list, sep='\n')
rev_list = sorted(my_list, reverse=True)
print(my_list, rev_list, sep='\n')
# Переданная в функцию коллекция остаётся неизменной после результата работы
# функции. Если в функцию передать дополнительный аргумент reverse=True,
# сортировка происходит по убыванию.
# Внутри функции используется алгоритм сортировки Timsort — гибридная
# устойчивая сортировка с временной асимптотикой O(n log n). Дополнительно
# тратится O(n) памяти на создание нового отсортированного списка.
