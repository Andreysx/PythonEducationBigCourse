# Методы startswith и endswith
# Метод startswith проверяет начинается ли строка с заданной подстроки. Метод
# возвращает истину или ложь. Метод endswith проверяет окончание строки
# переданной в качестве аргумента подстрокой.
# text = 'Однажды в студёную зимнюю пору'
# print(text.startswith('Однажды'))
# print(text.endswith('зимнюю', 0, -5))
# Оба метода помимо подстроки могут принимать параметры start и stop. В этом
# случае проверка начала либо конца будет проводиться в указанном диапазоне.


# def func():
#     temp_dict = {}
#     for item in globals():
#         if not item.startswith('__'):
#             if item.endswith('s') and len(item) > 1:
#                 temp_dict[item[:-1]] = globals()[item]
#                 temp_dict[item] = None
#     globals().update(temp_dict) # or locals
#
#
# func()
# print([item for item in globals() if not item[0].startswith('__')])
#
# ##Лучше не использовать глоб переменные и лучше все изолировать(модули)