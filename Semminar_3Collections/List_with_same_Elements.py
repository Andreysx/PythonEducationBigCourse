# Создайте вручную список с повторяющимися элементами.
# Удалите из него все элементы, которые встречаются дважды.

my_list = [1, 2, 3, 4, 5, 3, 5, 6, 8, 2]
# 1 тернарные операторы
editted_list = [num for num in my_list if my_list.count(num) != 2]
print(editted_list)
# 2 функция filter
editted_list_v2 = list(filter(lambda x: my_list.count(x) != 2, my_list))
print(editted_list_v2)
# 3
for num in set(my_list):
    if my_list.count(num) == 2:
        my_list.remove(num)
        my_list.remove(num)
print(my_list)