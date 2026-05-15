# Структуры данных:
# Array, Dinamic array(элементы хранятся подряд в памяти;
# при добавлении места может не хватить → выделяется новый, больший блок памяти;
# старые элементы копируются;
# список хранит не сами объекты, а ссылки (PyObject*) на них.)
# Linked list
# Hash-table
# Graph
# Tree
# Binary Tree
# Binary Tree SEARCH
# Queue
# Stack

# O(нотация) - Определяет худший случай выполнения
# Скорость алгоритмов измеряется не в секундах, а в темпе роста количества операций
# По сути формула описывает насколько быстро возрастает время выполнения алгоритма с увеличением размера входных данных
# O(1)
# O(log n)
# O(n)
# O(n log n)
# O(n2)
# O(n3)
# O(n*m)

# Алгоритмы поиска:
# Простой поиск - O(n) - линейное время.
# Ищет позицию элемента в массиве
def simple_search(array: list, item: int) -> int:
    for i, el in enumerate(array):
        if el == item:
            return i
    return -1


# Бинарый поиск - ищет позицию элемента в массиве
# Только по отсортированному массиву
# Сложность O(log n)
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


# b_s = [1, 2, 3, 4, 5, 6, 7, 8]
# print(f"Binary search result: {binary_search(b_s, 6)} ")


# BFS Поиск/обход в ширину O(V + E)
# Алгоритм работает с графами(невзвешенными)
# Позволяет определить есть путь из A в B
# Если путь есть то находит кратчайший путь
# Поиск/обход начинается с начальной точки
#  Обходит по уровням связей - испольует очередь FIFO
# Подходит если граф слишком глубокий, но при это не слишком широкий
#
from collections import deque

graph = dict()


def simple_func(*args):
    pass


def search(graph_node):
    search_queue = deque()
    search_queue += graph[graph_node]
    searched = []
    while search_queue:
        node = search_queue.popleft()
        if node not in searched:
            if simple_func(node):
                return True
            else:
                searched.append(node)
                search_queue += graph[node]

    return False


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


def bfs(root: TreeNode):
    s_q = deque()
    s_q += [root]
    while s_q:
        for _ in range(len(s_q)):
            node = s_q.popleft()
            if node:
                print(node.val, end=" ")
                s_q += [node.left]
                s_q += [node.right]


print()
print("BFS")
bfs(root)


#
# DFS - Обход в глубину O(V + E)
# Находит путь от A к B, но не обязательно кратчайший
# Работает рекурсивно использует стек
# Идет в глубь настолько насколько это возможно
# Популярен при обходе бинарных деревьев
# Использовать если граф слишком широки но не слишком глубокий

# Прямой обход(PREORDER)(к-л-п)
# Удобен для копирования и серриализации дерева
def dfs_preorder(root: TreeNode):
    if not root:
        return
    print(root.val, end=" ")
    dfs_preorder(root.left)
    dfs_preorder(root.right)


print()
print("DFS PREORDER")
dfs_preorder(root)


#
# Симметричный обход (INORDER) (л-к-п)
# Используется дял вывода элементов в порядке возрастания
def dfs_inorder(root: TreeNode):
    if not root:
        return
    dfs_inorder(root.left)
    print(root.val, end=" ")
    dfs_inorder(root.right)


print()
print("DFS INORDER")
dfs_inorder(root)


# Обратный обход(POSTORDER)(л-п-к)
# Используется для удаления дерева - сначала листья или вычисления
def postorder_dfs(root: TreeNode):
    if not root:
        return
    postorder_dfs(root.left)
    postorder_dfs(root.right)
    print(root.val, end=" ")


print()
print("DFS POSTORDER")
postorder_dfs(root)


# Алгоритм Дейкстры работает с ациклическими графами DAG с положительными весами(Вычисляет кратчайший путь во взвешенном графе)
# Алгоритм Беллмана-Форда работат с ациклическими графами с любыми весами

# Алгоритмы сортировки
# Bubble sorting O(n2)
def bubble_sort(array: list):
    for i in range(len(array)):
        for j in range(len(array) - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]


print()
b_s = [65, 7, 2, 3, 4, 9, 1, 45, -3, -2]
bubble_sort(b_s)
print("Bubble sort", b_s)


# Selection sorting
def selection_sort(array: list):
    for i in range(len(array)):
        min_i = i
        for j in range(i + 1, len(array)):
            if array[j] < array[min_i]:
                min_i = j
        array[min_i], array[i] = array[i], array[min_i]


print()
s_s = [65, 7, 2, 3, 4, 9, 1, 45, -3, -2]
selection_sort(s_s)
print("Seletion sort", s_s)


# Inserion sort
def insertion_sort(array: list):
    for i in range(1, len(array)):
        for j in range(i, 0, -1):
            if array[j] < array[j - 1]:
                array[j], array[j - 1] = array[j - 1], array[j]


print()
i_s = [65, 7, 2, 3, 4, 9, 1, 45, -3, -2]
insertion_sort(i_s)
print("Insertion sort", i_s)


# Quick sort Быстрая сортировка
# Работает рекурсивно(разделяй и властвуй)
# Сильно зависит от выбора опорного элемента
# O(n log n) - Опорный - случайный элемент - Средний случай
# O(n2)  - Опорный - первый элемент и входной массив уже отсортирован - большой стек вызовов - Худший случай
# Оптимизация - выбор медианы выбираем медиану из трех: первый, центральный, последний (уменьшает шанс плохого разбиения)


def quick_sort(array: list):
    if len(array) < 2:
        return array
    else:
        pivot = array[len(array) // 2]
        less = [i for i in array if i < pivot]
        equal = [i for i in array if i == pivot]
        more = [i for i in array if i > pivot]
        return quick_sort(less) + equal + quick_sort(more)

    # Оптимизация с медианой
    # else:
    #     start = array[0]
    #     center = array[len(array) // 2]
    #     end = array[-1]
    #     pivot = sorted([start, center, end])[1]
    #
    #     less = [i for i in array if i < pivot]
    #     equal = [i for i in array if i == pivot]
    #     more = [i for i in array if i > pivot]
    #     return quick_sort(less) + equal + quick_sort(more)


print()
q_s = [65, 7, 2, 3, 4, 9, 1, 45, -3, -2]
print("Quick sort", quick_sort(q_s))


# Merge sorting
# Merge sort O(n log n)
# Более стабильный алгоритм, но требует дополнительных накладных расходов
#  Лучший, средний, худший случаи - всегда O(n log n)
# В общем случае работает медленнее чем быстрая сортировка
# Merge sort - это надежный, стабильный алгоритм с гарантированной производительностью, но платой за это является дополнительная память.

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
    n = len(array) // 2  # середина массива
    a_1 = array[:n]
    a_2 = array[n:]

    if len(a_1) > 1:
        a_1 = split(a_1)
    if len(a_2) > 1:
        a_2 = split(a_2)

    return merge_lists(a_1, a_2)


# def merge_sort(arr):
#     if len(arr) <= 1:
#         return arr
#
#     mid = len(arr) // 2
#     left = merge_sort(arr[:mid])
#     right = merge_sort(arr[mid:])
#
#     return merge_lists(left, right)


print()
m_s = [65, 7, 2, 3, 4, 9, 1, 45, -3, -2]
print("Merge sort", split(m_s))


# Other ones:

# Two pointers
def is_palindrome(word: str):
    i, j = 0, len(word) - 1
    while i <= j:
        if word[i] != word[j]:
            return False
        i += 1
        j -= 1
    return True


# w = 'abbsba'
# print(is_palindrome(w))\


# Максимальная длина уникальной подстроки в строке(Наибольшая подстрока без повторений)
def sliding_window(seq: str):
    max_size = 0
    left = 0
    uniq_s = set()
    for right in range(len(seq)):
        while seq[right] in uniq_s:
            uniq_s.remove(seq[left])
            left += 1
        max_size = max(max_size, right - left + 1)
        uniq_s.add(seq[right])
    return max_size


s = "pwwkew"
print(f"Sliding window {sliding_window(s)}")

# Merge algh
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
#     new_array.extend(first[i:])
#     new_array.extend(second[j:])
#
#     return new_array
