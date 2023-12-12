# Множества set и frozenset
# Ещё одна коллекция из коробки — множества. Множество — набор уникальных
# неиндексированных элементов. В Python есть два вида множеств: set —
# изменяемое множество, frozenset — неизменяемое множество. Неизменяемое
# множество позволяет вычислять хеш и может использоваться там, где разрешён
# 33
# лишь хешированный тип данных, например в качестве ключа словаря.
# my_set = {1, 2, 3, 4, 2, 5, 6, 7}
# print(my_set)
# my_f_set = frozenset((1, 2, 3, 4, 2, 5, 6, 7,))
# print(my_f_set)
# not_set = {1, 2, 3, 4, 2, 5, 6, 7, ['a', 'b']} # TypeError: unhashable type: 'list'
# Обратите внимание, что двойка передавалась в множества дважды, но хранится в
# единственном экземпляре, как один из уникальных элементов
# 🔥 Важно! Элементом множества могут быть только неизменяемые типы
# данных.
