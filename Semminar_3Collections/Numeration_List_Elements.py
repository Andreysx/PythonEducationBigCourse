# Создайте вручную список с повторяющимися целыми числами.
# Сформируйте список с порядковыми номерами нечётных элементов исходного списка.
# Нумерация начинается с единицы.

my_list = [1, 2, 3, 4, 1, 2, 3, 1, 2, 3, 1, 2, 3]

# result = [i + 1 for i in range(len(data)) if data[i] % 2] - не использовать range(len - ресурсоемко
res_list = [i[0] for i in enumerate(my_list, 1) if i[1] % 2 != 0]

print(res_list)
