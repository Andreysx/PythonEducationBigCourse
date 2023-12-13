# Создайте вручную кортеж содержащий элементы разных типов.
# Получите из него словарь списков,
# где ключ - тип элемента, а значение - список элементов данного типа.

my_typle = (1, 2, 2.5, 2.3, [23, 56], [2, 73], True, False, {23, 35}, {23, 6}, "Hello_world", "321")
my_dict = {}
for item in my_typle:
    my_dict.setdefault(type(item), []).append(item)
[print(f"{key}: {value}") for key, value in my_dict.items()]
