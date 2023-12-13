# Пользователь вводит строку текста.
# Подсчитайте сколько раз встречается каждая буква в строке без использования метода count и с ним.
# Результат сохраните в словаре, где ключ - символ, а значение - частота встречи символа в строке.
# Обратите внимание на порядок ключей.
# Объясните почему они совпадают или не совпадают в ваших решениях.

from collections import Counter

text = input().replace(' ', '')

my_dict = {}

for c in text:
    my_dict[c] = my_dict.get(c, 0) + 1
print(my_dict)

new_my_dict = {}

for el in set(text):
    new_my_dict[el] = text.count(el)
print(new_my_dict)

print(Counter(text))
