# Search algorithms:
# Simple search O(n)
def simple_search(array: list, item: int) -> int:
    for i, el in enumerate(array):
        if el == item:
            return i
    return -1


# l = [1, 3, 4, 5, 6, 7, 8]
# print(simple_search(l, 5))

# Binary search
# Работает только с отсортированными массивами
# O(log n)
def binary_search(array: list, item: int) -> int:
    low = 0
    high = len(array) - 1
    while low <= high:
        mid = (low + high) // 2
        guess = array[mid]
        if guess == item:
            return mid
        if guess > item:
            high = mid - 1
        else:
            low = mid + 1
    return -1


# print(binary_search(l, 6))


# BFS(graph, binary tree)
# Работает с графами O(V+E)
# Позволяет найти путь из точки A в точку B
# Если он существует находит кратчайший путь
graph = {"Андрей": ["Никита", "Максим", "Иван"],
         "Никита": ["Дмитрий", "Олег", "Иван"],
         "Максим": [],
         "Иван": [],
         "Дмитрий": [],
         "Олег": ["Никита", "Максим", "Игорь"],
         "Игорь": ["Антон"],
         "Антон": []}


def name_end(s: str):
    if s.endswith("tt"):
        return True
    return False


from collections import deque


def bfs_search(name):
    search_queue = deque()
    search_queue += graph[name]
    searched = []
    while search_queue:
        person = search_queue.popleft()

        if person not in searched:
            if name_end(person):
                return "Success"
            else:
                searched.append(person)
                search_queue += graph[person]
    return "Failure"


# print(bfs_search("Андрей"))

# Реализация бинарного дерева
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


root = TreeNode("A")
root.left = TreeNode("B")
root.right = TreeNode("C")
root.left.left = TreeNode("D")
root.left.right = TreeNode("E")
root.right.left = TreeNode("F")
root.right.right = TreeNode("G")


# Поискв ширину по бинарному дереву
def bfs(root: TreeNode):
    s_q = deque([root])
    while s_q:
        for _ in range(len(s_q)):  # Обрабатываем один уровень дерева за раз
            node = s_q.popleft()
            if node:
                print(node.val, end=" ")
                s_q += [node.left]
                s_q += [node.right]


print("BFS")
bfs(root)


# DFS(binary tree, preorder(корень - левое - правое), inorder(левое -корень -правое), postorder(левое-правое-корень))
# Три способа обхода бинарного дерева различаются порядком обработки узлов
class TreeNode_2:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


root_2 = TreeNode_2("A")
root_2.left = TreeNode_2("B")
root_2.right = TreeNode_2("C")
root_2.left.left = TreeNode_2("D")
root_2.left.right = TreeNode_2("E")
root_2.right.left = TreeNode_2("F")
root_2.right.right = TreeNode_2("G")


# Прямой обход
# Используется для копирования дерева или сериализации.
def dfs_preorder(root: TreeNode_2):
    if not root:
        return
    print(root.val, end=" ")
    dfs_preorder(root.left)
    dfs_preorder(root.right)


print()
print("PREORDER DFS")
dfs_preorder(root_2)


# Симметричный обход (Inorder)
# Применяется для вывода элементов в порядке возрастания.
def dfs_inorder(root: TreeNode_2):
    if not root:
        return
    dfs_inorder(root.left)
    print(root.val, end=" ")
    dfs_inorder(root.right)


print()
print("INORDER DFS")
dfs_inorder(root_2)


# Обратный обход (Postorder)
# Идеален для удаления дерева (сначала листья) или вычисления выражений.
def dfs_postorder(root: TreeNode_2):
    if not root:
        return
    dfs_postorder(root.left)
    dfs_postorder(root.right)
    print(root.val, end=" ")


print()
print("POSTORDER DFS")
dfs_postorder(root_2)


# ✅ Когда выбирать BFS (очередь)
# 1. Нужен кратчайший путь в невзвешенном графе
# BFS находит путь с минимальным числом рёбер. DFS — нет (найдёт любой, не обязательно короткий).
#
# 2. Граф «бесконечный» или очень глубокий, но не слишком широкий
# Например, поиск выхода из лабиринта, когда неизвестно, насколько глубоко решение. BFS не уйдёт в бесконечную глубину.
#
# 3. Все рёбра имеют одинаковый вес (или вес не учитывается)
#
# 4. Требуется обход «по слоям»
# Например, поиск всех друзей на расстоянии 2 в соцсети.
#
# 5. Память не критична (или граф не слишком широкий)
# BFS хранит весь текущий уровень — может потреблять O(ширина) памяти.
#
# ✅ Когда выбирать DFS (стек или рекурсия)
# 1. Нужно проверить существование пути (не важно, какого)
# DFS быстрее найдёт любой путь, если не нужен кратчайший.
#
# 2. Граф очень широкий, но не слишком глубокий
# BFS при широком графе «взорвётся» по памяти. DFS использует O(глубина).
#
# 3. Требуется топологическая сортировка, поиск компонент сильной связности, проверка циклов
# Это классические задачи для DFS.
#
# 4. Память ограничена
# DFS потребляет меньше памяти, если граф глубокий, но не слишком разветвлённый.
#
# 5. Работа с деревьями (особенно бинарными)
# Например, прямой, обратный, симметричный обход — естественно реализуются через DFS.
# #
# BFS → кратчайший путь, но больше памяти
#
# DFS → меньше памяти, но не ищет кратчайший путь

# Sorting  algorithms:
# Bubble sort o(n2)
def bubble_sort(array: list) -> list:
    for i in range(len(array)):
        for j in range(len(array) - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]

    return array


print()
s_b = [6, 5, 7, 4, 8, 3, 9, 2, 1]

print(f"Bubble sorting {bubble_sort(s_b)}")


# Selection sort
def selection_sort(array: list) -> list:
    for i in range(len(array)):
        min_i = i
        for j in range(i + 1, len(array)):
            if array[min_i] > array[j]:
                min_i = j
        array[i], array[min_i] = array[min_i], array[i]
    return array


s_s = [6, 5, 7, 4, 8, 3, 9, 2, 1]

print(f"Selection sorting {selection_sort(s_s)}")


# Insertion sort
def insertion_sort(array: list) -> list:
    for i in range(1, len(array)):
        for j in range(i, 0, -1):
            if array[j - 1] > array[j]:
                array[j], array[j - 1] = array[j - 1], array[j]

    return array


s_i = [6, 5, 7, 4, 8, 3, 9, 2, 1]

print(f"Insertion sorting {insertion_sort(s_i)}")


# Quick sort
# O(n log n) - Опорный элемент случайный
# O(n2) - Опорный элемент первый и список уже отсортирован
#
def quick_sort(array: list) -> list:
    if len(array) < 2:
        return array
    else:
        pivot = array[len(array) // 2]
        less = [i for i in array if i < pivot]
        more = [i for i in array if i > pivot]
        return quick_sort(less) + [pivot] + quick_sort(more)


s_q = [6, 5, 7, 4, 8, 3, 9, 2, 1]
print(f"Quick sorting {quick_sort(s_q)}")


# Merge sort
# O(n log n) - Средний случай
def merge_lists(first: list, second: list) -> list:
    i, j = 0, 0
    new_array = []
    while i < len(first) and j < len(second):
        if first[i] < second[j]:
            new_array.append(first[i])
            i += 1
        else:
            new_array.append(second[j])
            j += 1

    new_array.extend(first[i:])
    new_array.extend(second[j:])

    return new_array


def split(array: list):
    n = len(array) // 2
    a_1 = array[:n]
    a_2 = array[n:]

    if len(a_1) > 1:
        a_1 = split(a_1)
    if len(a_2) > 1:
        a_2 = split(a_2)

    return merge_lists(a_1, a_2)


s_m = [6, 5, 7, 4, 8, 3, 9, 2, 1]

print(f"Merge sorting {split(s_m)}")


#
# Other:
# Sliding window
# Задачи типа  - Наибольшая подстрока без повторений
def sliding_window(seq: str) -> int:
    maxsize = 0
    left = 0
    uniq = set()
    for right in range(len(seq)):
        while seq[right] in uniq:
            uniq.remove(seq[left])
            left += 1
        maxsize = max(maxsize, right - left + 1)
        uniq.add(seq[right])
    return maxsize


b = 'abcda'
print(sliding_window(b))


# Two pointers

def is_palindrome(seq: str) -> bool:
    i, j = 0, len(seq) - 1
    while i <= j:
        if seq[i] != seq[j]:
            return False
        i += 1
        j -= 1
    return True


word = "abcrba"


# print(is_palindrome(word))


# Merge lists alg
# def merge_lists(first: list, second: list) -> list:
#     i, j = 0, 0
#     new_array = []
#     while i < len(first) and j < len(second):
#         if first[i] < second[j]:
#             new_array.append(first[i])
#             i += 1
#         else:
#             new_array.append(second[j])
#             j += 1
#
#     new_array.extend(first[i:])
#     new_array.extend(second[j:])
#
#     return new_array


# Последовательные символыМощность строки — это максимальная длина непустой подстроки, содержащей только один уникальный символ.

# Требуется вернуть мощность строки s.
# def max_power( s: str) -> int:
#     max_size = 1
#     current = 1
#
#     for i in range(1,len(s)):
#         if s[i] == s[i - 1]:
#             current += 1
#         else:
#             current = 1
#         max_size = max(max_size, current)
# return max_size


# 1. Two Sum
# class Solution:
#     def two_sum(self, nums: list[int], target: int) -> list[int]:
#         # nums_2 = nums[:]
#         # for i in range(len(nums)):
#         #     for j in range(len(nums_2)):
#         #         if i == j:
#         #             continue
#         #         if nums[i] + nums_2[j] == target:
#         #             return [i, j]
#
#         d = dict()
#         for i, num in enumerate(nums):
#             res = target - num
#             if res in d:
#                 return [d[res], i]
#             d[num] = i


# Переместить нули/283. Move Zeroes
# Input: nums = [0,1,0,3,12]
# Output: [1,3,12,0,0]

# class Solution(object):
#     def moveZeroes(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: None Do not return anything, modify nums in-place instead.
#         """
#         i, j = 0, 0
#         if len(nums) <= 1:
#             return nums
#         while i < len(nums):
#             if nums[i] != 0:
#                 nums[j], nums[i] = nums[i], nums[j]
#                 j += 1
#                 i += 1
#             else:
#                 i += 1
#
#         return nums


# Пропущенное число/268. Missing Number
def missing_number(nums: list[int]) -> int:
    set_1 = set(nums)
    set_2 = set(i for i in range(0, len(nums) + 1))
    res = (set_2 - set_1)
    return res.pop()

    # Или
    # n = len(nums)
    # total = n * (n + 1) // 2
    # return total - sum(nums)


# Перевернуть строку
# class Solution:
#     def reverse_string(self, s: list[str]) -> None:
#         i, j = 0, len(s) - 1
#         while i <= j:
#             s[i], s[j] = s[j], s[i]
#             i += 1
#             j -= 1


# Наибольшая подстрока без повторений
# class Solution:
#     def length_of_longest_substring(self, s: str) -> int:
#         max_size = 0
#         left = 0
#         uniq_symbols = set()
#         for right in range(len(s)):
#             while s[right] in uniq_symbols:
#                 uniq_symbols.remove(s[left])
#                 left += 1
#             max_size = max(max_size, right - left + 1)
#             uniq_symbols.add(s[right])
#         return max_size


# Палиндром
# class Solution:
#     def is_palindrome(self, s: str) -> bool:
#         s_1 = ''.join([i for i in s if i.isalpha() or i.isdigit()]).lower()
#         if not s_1:
#             return True
#         return True if s_1 == s_1[::-1] else False

# Пересечение двух массивов
# class Solution:
#     def intersection(self, nums1: list[int], nums2: list[int]) -> list[int]:
#         nums1_s = set(nums1)
#         nums2_s = set(nums2)
#         return list(nums1_s.intersection(nums2_s))

# Пересечение двух массивов 2
# class Solution:
#     def intersect(self, nums1: list[int], nums2: list[int]) -> list[int]:
#         new_array = []
#         for i in nums1:
#             if i in nums2:
#                 new_array.append(i)
#                 nums2.remove(i)
#         return new_array


# Последовательные символы
# class Solution:
#     def max_power(self, s: str) -> int:
#         max_size = 1
#         current = 1
#
#         for i in range(1, len(s)):
#             if s[i] == s[i - 1]:
#                 current += 1
#             else:
#                 current = 1
#             max_size = max(max_size, current)
#         return max_size


# Максимальное количество последовательных единиц
# def find_max_consecutive_ones(nums: list[int]) -> int:
#     max_count = 0
#     current = 0
#     for i in range(0, len(nums)):
#         if nums[i] == 1:
#             current += 1
#         else:
#             current = 0
#         max_count = max(max_count, current)
#
#     return max_count
#
#
# nums = [1,0,1,1,0,1]
#
# print(find_max_consecutive_ones(nums))


def generate_matrix(n: int, m: int) -> list[list[int]]:
    # g = [i for i in range(1, n * m + 1)][::-1]
    #
    # matrix = []
    #
    # for i in range(n):
    #     row = []
    #     for j in range(m):
    #         value = g.pop()
    #         row.append(value)
    #     matrix.append(row)
    matrix = [[i * m + j + 1 for j in range(m)] for i in range(n)]

    # Вывод матрицы
    #     for row in matrix:
    #         print(' '.join(map(str, row)))
    # n = 2
    # m = 3


    # generate_matrix(n, m)




# Успеваемость студентов
# def passed_students(students: dict[str, list[str]], value: int) -> list[str]:
#     result = set()
#     for student in students:
#         scores = students[student]
#         for s in scores:
#             s = s.split('/')
#             print(s)
#             if (int(s[0]) * 100) // int(s[1]) >= value:
#                 result.add(student)
#                 continue
#             else:
#                 break
#
#     return list(result)
#
#
# students = {
#     "Иван": ["5/5", "10/10", "20/20"],
#     "Мария": ["4/5", "9/10", "18/20"],
#     "Алексей": ["5/5", "10/10", "19/20"],
#     "Ольга": ["3/5", "7/10", "14/20"],
#     "Дмитрий": ["5/5", "10/10", "20/20"],
# }
#
# value = 90
#
# print(passed_students(students, value))


# Инвертировать бинарное дерево

# Определение узла двоичного дерева.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# from collections import deque
# class Solution:
#     def invert_tree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
#         if not root:
#             return
#         queue = deque([root])
#         while queue:
#             for _ in range(len(queue)):
#                 node = queue.popleft()
#                 node.left, node.right = node.right, node.left
#                 if node.left:
#                     queue += [node.left]
#                 if node.right:
#                     queue += [node.right]
#         return root