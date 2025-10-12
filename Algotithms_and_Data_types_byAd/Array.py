# Сравнение списка (list python(dynamic array))с массивом из модуля array
import array
import sys

python_list = [1, 2, 3, 4, 5]  # Хранит 5 объектов int
int_array = array.array('i', [1, 2, 3, 4, 5])  # Хранит 5 значений int

print(f"list размер: {sys.getsizeof(python_list)} байт")
print(f"array размер: {sys.getsizeof(int_array)} байт")