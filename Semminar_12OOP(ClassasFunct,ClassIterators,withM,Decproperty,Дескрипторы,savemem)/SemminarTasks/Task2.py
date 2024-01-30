 # Доработаем задачу 1.
# # Создайте менеджер контекста, который при выходе сохраняет значения в JSON файл.
#
# import json
# from collections import OrderedDict
#
# class Factorial:
#     __JSON_FILE_NAME = "factorials.json"
#
#     def __init__(self, k):
#         self.__fact = self.__load_json()
#         self.k = k
#
#     def __call__(self, number: int):
#         str_number = str(number)
#         if str_number in self.__fact:
#             return self.__fact[str_number]
#         result, key = 1, 0
#         max_pair = self.__get_max(number)
#         if max_pair:
#             key, result = max_pair
#         for i in range(key + 1, number + 1):
#             result *= i
#         self.__fact[str_number] = result
#         if len(self.__fact) > self.k:
#             self.__fact.popitem(last=False)
#         return result
#
#     # def __get_max(self, number: int) -> tuple | None:
#     # max_pair = None
#
#     def __get_max(self, number: int) -> tuple | None:
#         max_pair = None
#
#         for key, value in self.__fact.items():
#             int_key = int(key)
#             if int_key < number and (max_pair is None or int_key > max_pair[0]):
#                 max_pair = (int(key), value)
#             return max_pair
#
#     def get_factorials(self):
#         return self.__fact
#
#     def __load_json(self):
#         try:
#             with open(self.__JSON_FILE_NAME, encoding='utf-8') as f:
#                 return OrderedDict(json.load(f))
#         except FileNotFoundError as e:
#             return OrderedDict()
#
#     def __enter__(self):
#         pass
#     # return self
#
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         with open(self.__JSON_FILE_NAME, "w", encoding='utf-8') as f:
#             json.dump(self.__fact, f, indent=2, ensure_ascii=False)
#
#
# if __name__ == '__main__':
#     f = Factorial(3)
#     with f:
#         print(f(2), f(4), f(3), f(5), f(6), f(7))
#         print(f.get_factorials())