#
#
# from collections import Counter
#
#
# def calculate_sales(*sales_dicts) -> Counter:
#     result = Counter()
#     for i in range(len(sales_dicts)):
#         result += sales_dicts[i]
#     return result
# # def calculate_sales(*sales_dicts) -> Counter:
# #     return reduce(lambda a, b: a + b, map(Counter, sales_dicts))
#
#
# # Пример использования функции
# sales_1 = {'John': 10, 'Mary': 5, 'Bob': 3, 'Alice': 7}
# sales_2 = {'John': 5, 'Mary': 8, 'Bob': 6, 'Alice': 2}
# sales_3 = {'John': 3, 'Mary': 4, 'Bob': 2, 'Alice': 9}
# sales_4 = {'John': 8, 'Alice': 5, 'Henry': 10}
#
# assert calculate_sales(sales_1, sales_2, sales_3) == Counter({'John': 18, 'Alice': 18, 'Mary': 17, 'Bob': 11})
# assert calculate_sales(sales_1, sales_2) == Counter({'John': 15, 'Mary': 13, 'Bob': 9, 'Alice': 9})
# assert calculate_sales(sales_3, sales_2) == Counter({'Mary': 12, 'Alice': 11, 'John': 8, 'Bob': 8})
# assert calculate_sales(sales_4, sales_2, sales_1) == Counter({'John': 23, 'Alice': 14, 'Mary': 13, 'Henry': 10, 'Bob': 9})


# from collections import Counter
#
#
# def count_min_goals(statistics):
#     player_goals = Counter()
#
#     for year_data in statistics.values():
#         for player, goals in year_data.items():
#             if player not in player_goals:
#                 player_goals[player] = goals
#             else:
#                 if goals < player_goals[player]:
#                     player_goals[player] = goals
#
#     return player_goals
#
#
# statistics = {
#     2020: {'Messi': 20, 'Neymar': 30, 'Ronaldo': 25},
#     2021: {'Neymar': 23, 'Griezmann': 47, 'Messi': 29},
#     2022: {'Griezmann': 35, 'Messi': 34, 'Ronaldo': 34}
# }
#
# a = count_min_goals(statistics)
# a.
#
# print(count_min_goals(statistics))
# # assert count_min_goals(statistics) == Counter({'Griezmann': 35, 'Ronaldo': 25, 'Neymar': 23, 'Messi': 20})
# #
# # statistics = {
# #     2015: {'Benzema': 32, 'Griezmann': 43, 'Messi': 52, 'Neymar': 39, 'Ronaldo': 51},
# #     2016: {'Benzema': 26, 'Griezmann': 37, 'Messi': 36, 'Neymar': 35, 'Ronaldo': 42},
# #     2017: {'Benzema': 27, 'Griezmann': 51, 'Messi': 42, 'Neymar': 49, 'Ronaldo': 30},
# #     2018: {'Benzema': 32, 'Griezmann': 41, 'Messi': 45, 'Neymar': 30, 'Ronaldo': 43},
# #     2019: {'Benzema': 29, 'Griezmann': 39, 'Messi': 51, 'Neymar': 31, 'Ronaldo': 48},
# #     2020: {'Benzema': 33, 'Griezmann': 41, 'Messi': 36, 'Neymar': 30, 'Ronaldo': 25},
# #     2021: {'Benzema': 54, 'Griezmann': 47, 'Messi': 29, 'Neymar': 36, 'Ronaldo': 21},
# #     2022: {'Benzema': 29, 'Griezmann': 35, 'Messi': 34, 'Neymar': 36, 'Ronaldo': 34}
# # }
# # assert count_min_goals(statistics) == Counter(
# #     {'Griezmann': 35, 'Neymar': 30, 'Messi': 29, 'Benzema': 26, 'Ronaldo': 21})

#
# from collections import Counter
#
#
# def find_three_most_common(lst: list) -> list:
#     result = [item[0] for item in Counter(lst).most_common(3)]
#     while len(result) != 3:
#         result.append(None)
#     return result[::-1]
#
#
# assert find_three_most_common([1, 2, 2, 3, 3, 3, 4, 4, 4, 4]) == [2, 3, 4]
# assert find_three_most_common([1, 1, 1, 1, 1]) == [None, None, 1]
# assert find_three_most_common([1, 1, 1, 2, 2]) == [None, 2, 1]
# assert find_three_most_common([1, 1, 2, 2, 2]) == [None, 1, 2]
# assert find_three_most_common([]) == [None, None, None]

#
#
# from collections import Counter
#
#
# def find_difference_with_counter(lst1: list, lst2: list) -> list:
#     result = Counter(lst1) - Counter(lst2)
#     result = sorted(list(result.elements()))
#
#     return result
#
#
# assert find_difference_with_counter([1, 2, 2, 3, 4, 4, 5],
#                                     [2, 3, 3, 4, 5, 6]) == [1, 2, 4]
#
# print(find_difference_with_counter([5, 4, 5, 1, 2, 7, 3],
#                                     [2, 3, 3, 4, 5, 6]))
# assert find_difference_with_counter([5, 4, 5, 1, 2, 7, 3],
#                                     [2, 3, 3, 4, 5, 6]) == [1, 5, 7]
#
# assert find_difference_with_counter([1, 1, 2, 3, 3, 4, 4, 5, 6, 7],
#                                     [1, 1, 2, 4, 5, 6]) == [3, 3, 4, 7]
#
# assert find_difference_with_counter([1, 1, 1, 1],
#                                     [1, 1, ]) == [1, 1]
#
# assert find_difference_with_counter([1, 1, ],
#                                     [1, 1, 1, 1]) == []
#
#
# from collections import Counter
# from typing import Optional
#
#
# def find_most_common_element(lst: list[int]) -> Optional[int]:
#     return Counter(lst).most_common(1)[0][0] if lst else None
#     # result = Counter(lst).most_common(1)
#     # # if result:
#     # #     return result[0][0]
#     # # else:
#     # #     return None
#
#
# print(find_most_common_element([1, 2, 2, 3, 3, 3, 4, 4, 4, 4]))
# assert find_most_common_element([1, 2, 2, 3, 3, 3, 4, 4, 4, 4]) == 4
#
# assert find_most_common_element([3, 8, 7, 3, 3, 5, 3, 5, 1, 3, 3]) == 3
# assert find_most_common_element([1, 2, 3]) == 1
# assert find_most_common_element([5]) == 5
# assert find_most_common_element([]) is None

#
# from collections import Counter
# from typing import Optional
#
#
# def find_majority_element(nums: list) -> Optional[int]:
#     length = len(nums)
#     c = Counter(nums).most_common()
#     for item in c:
#         if item[1] >= length / 2:
#             return item[0]
#         else:
#             return None
#
#
# print(find_majority_element([3, 8, 7, 3, 3, 5, 3, 5, 1, 3, 3]))
# assert find_majority_element([3, 8, 7, 3, 3, 5, 3, 5, 1, 3, 3]) == 3
#
# # Тест 2: Элемент большинства присутствует
# assert find_majority_element([6, 8, 4, 6, 8, 6, 6]) == 6
#
# # Тест 3: Элемент большинства отсутствует
# assert find_majority_element([1, 2, 3]) is None
#
# # Тест 4: Пустой список
# assert find_majority_element([]) is None
#
# # Тест 5: Список с одним элементом
# assert find_majority_element([7]) == 7
#
# # Тест 6: Список с двумя элементами
# assert find_majority_element([7, 7]) == 7
#
# # Тест 7: Список с тремя элементами (элемент большинства отсутствует)
# assert find_majority_element([7, 8, 9]) is None


# from collections import deque
# from typing import NamedTuple
#
# class Commands(NamedTuple):
#     action: str
#     side: str
#     value: int = 1
#
# d_c = deque(map(int, input().split()))
# count_command = int(input())
#
# commands = []
# for _ in range(count_command):
#     parts = input().split()
#     if len(parts) == 3:
#         action, side, value = parts[0], parts[1], int(parts[2])
#     else:
#         action, side = parts[0], parts[1]
#         value = 1
#     commands.append(Commands(action, side, value))
#
# for command in commands:
#     match command:
#         case Commands(action='A', side='L', value=value):
#             d_c.appendleft(value)
#         case Commands(action='A', side='R', value=value):
#             d_c.append(value)
#         case Commands(action='D', side='L', value=_):
#             d_c.popleft()
#         case Commands(action='D', side='R', value=_):
#             d_c.pop()
#         case Commands(action='R', side='R', value=value):
#             d_c.rotate(value)
#         case Commands(action='R', side='L', value=value):
#             d_c.rotate(-value)
#
# print(d_c)

# Или
# from collections import deque
#
# deq = deque(map(int, input().split()))
# for _ in range(int(input())):
#     match input().split():
#         case ["A", "R", num]:
#             deq.append(int(num))
#         case ["A", "L", num]:
#             deq.appendleft(int(num))
#         case ["D", "R"]:
#             deq.pop()
#         case ["D", "L"]:
#             deq.popleft()
#         case ["R", "R"]:
#             deq.rotate()
#         case ["R", "L"]:
#             deq.rotate(-1)
#
# print(deq)


# print(d_c, count_command, commands, sep='\n')


# from collections import deque
#
# deq = deque(map(int, input().split()))
#
# player_A, player_B = 0, 0
#
# while deq:
#     player_A += deq.popleft()
#     if deq:
#         player_B += deq.pop()
#
# print('FIRST' if player_A > player_B else 'SECOND' if player_B > player_A else 'DRAW')
# # if player_A > player_B:
# #     print('FIRST')
# # elif player_B > player_A:
# #     print('SECOND')
# # else:
# #     print('DRAW')


# def is_palindrome(s: str) -> bool:
#     d_s = deque(s.lower().replace(' ','').replace(',',''))
#     flag = True
#     while len(d_s) >= 3:
#         if d_s[0] == d_s[-1]:
#             flag = True
#         else:
#             flag = False
#         d_s.pop()
#         d_s.popleft()
#     return flag

# queue = deque(filter(str.isalpha, s.lower()))
#     while len(queue) > 1:
#         if queue.popleft() != queue.pop():
#             return False
#     return True


# from collections import deque
#
#
# class TextEditor:
#
#     def __init__(self):
#         self.text_editor = ''
#         self.add_story = deque()
#         self.cancel_story = deque()
#
#     def add_text(self, text):
#         self.text_editor += text
#         self.add_story.append(text)
#
#     def undo(self):
#         if self.add_story:
#             last_el = self.add_story.pop()
#             self.cancel_story.append(last_el)
#             self.text_editor = self.text_editor.replace(last_el, '')
#
#     def redo(self):
#         if self.cancel_story:
#             last_el = self.cancel_story.pop()
#             self.text_editor += last_el
#             self.add_story.append(last_el)
#
#     def get_text(self):
#         return self.text_editor
#
#
# editor = TextEditor()
# editor.add_text("Hello, ")
# assert editor.get_text() == "Hello, "
#
# editor.add_text("World!")
# print(editor.add_story)
# assert editor.get_text() == "Hello, World!"
#
# editor.add_text(" How are you!")
# print(editor.add_story)
# assert editor.get_text() == "Hello, World! How are you!"
#
# editor.undo()
# print(editor.add_story)
# print(editor.get_text())
# assert editor.get_text() == "Hello, World!"
#
# editor.redo()
# print(editor.cancel_story)
# print(editor.get_text())
# assert editor.get_text() == "Hello, World! How are you!"
#
# editor.undo()
# assert editor.get_text() == "Hello, World!"
# #
# editor.undo()
# assert editor.get_text() == "Hello, "


from collections import deque
import array

d = deque(maxlen=5)
d.extend([1,2,3,4,5])
print(d)
print(d[4])



#Именованный кортеж
from collections import namedtuple
from typing import NamedTuple

Person = namedtuple('Person', 'name age')

p = Person('Andrey', 26)


class Person_2(NamedTuple):
    age: int
    name: str


p_2 = Person_2(26, 'Andrey')


print(p, p.name, p.age)
print(p_2, p.name, p.age)