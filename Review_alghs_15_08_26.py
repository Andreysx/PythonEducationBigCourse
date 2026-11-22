# Data structures:
# Array, Dinamic array Произвольный доступ непрерывный блок памяти с заданным размером
# чтение  O(1)
# запись  O(N)
# удаление O(N)

# Linked list Последовательный доступ
# чтение  O(N)
# запись  O(1)
# удаление O(1)

# Hash table
# чтение  O(1)
# запись  O(1)
# удаление O(1)

# Graph
# Граф — это совокупность вершин (узлов) и ребер (связей между ними), которые описывают отношения между объектами. Позволяют моделировать связи между объектами
# Ориентированные(направленные - со стрелками - связь только в направлении стрелок(ребер))
# Неориентированные (ненаправленные - без стрелок - связь в обе стороны)(при обходе неориентированных графов необходимо хранить информацию о посещенных вершинах для избежания зацикливания)
# Взвешенный граф - ребра имеют веса (Дейкстра для графов где веса положительны)
# Невзвешенный граф - граф без весов)
# Ациклический граф DAG - В ориентированном графе нет циклов. Это самый важный тип для программирования (DAG — Directed Acyclic Graph)
# Циклический граф - граф с циклами, при обходе нужно отслеживать уже проверенные узлы.

# Tree
# Деревья - Граф без циклов и с единственным путем между вершинами(нет ребер указывающих в обратном направлении)

# Binary tree Бинарное дерево - это иерархическая структура данных, где каждый узел имеет не более двух потомков: левого и правого.
# Binary search tree

# STACK LIFO
# QUEUE FIFO


# O - асимтотическая нотация
# Описывает худший случай выполнения, дает гарантии что хуже не будет и мы можем опираться на это
# Скорость алгоритмов измеряется не в секундах, а в темпе роста количества операций
# По сути формула описывает насколько быстро возрастает время выполнения алгоритма с увеличением объема входных данных

# O(1) - Константное(постоянное)
# O(log n) - Логарифмическое
# O(n) - Линейное
# O(n log n) - Линейно-логарифмическое
# O(n2) - Квадратичное
# O(n3) - Кубическое
# O(n * m) - Экспонециальное


# ALGORITHMS:
#Алгоритм это набор инструкций для выполнения некоторой задачи
# SEARCH ALGORITHMS:
# Simple search O(n)
# Ищет позицию элемента в  массиве неважно отсортированный или нет
# По сути полный перебор -> bruteforce
def simple_search(array: list, item: int) -> int:
    for i, el in enumerate(array):
        if el == item:
            return i
    return -1


# Binary search O(log n)
# Чтобы сложность алгоритма увеличилась на 1, размер входных данных должен вырасти вдвое
# Бинарый поиск - ищет позицию элемента в массиве
# Только по отсортированному массиву
# На каждый итерации рассматриваемый диапазон поиска уменьшается вдвое
def binary_search(array: list, item: int) -> int:
    low = 0
    high = len(array) - 1
    while low <= high:
        mid = (low + high) // 2
        guess = array[mid]
        if guess == item:
            return mid
        elif guess > item:
            high = mid - 1
        else:
            low = mid + 1
    return -1


#
# binary_s_list = [1,2,3,4,5,6,7,8]
# print(binary_search(binary_s_list, 5))


# BFS Briedth-first search/Поиск или обход в ширину O(V + E)
# Поиск/обход в ширину O(V + E)
# Работает с графами
# Позволяет определить есть путь  между вершинами  из A в B
# Если он есть - то находит кратчайший путь между двумя вершинами графа
# Поиск/обход начинается с начальной точки
# Обходит по уровням связей Сначала 1ур -> 2ур -> 3ур и тд
# Использует очередь FIFO (deque в python)
# Использовать если граф очень глубокий или его глубина неизвестна и при этом он не слишком широкий, чтобы не просесть по памяти

from collections import deque

graph = dict()


def simple_func(*args, **kwargs):
    pass


def search(root):
    search_queue = deque()
    search_queue += graph[root]
    searched = []
    while search_queue:
        node = search_queue.popleft()
        if node not in searched:
            if simple_func(node):
                return True
            else:
                search_queue += graph[node]
                searched += [node]
    return False


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


root = TreeNode('A')
root.left = TreeNode('B')
root.right = TreeNode('C')
root.left.left = TreeNode('D')
root.left.right = TreeNode('E')
root.right.left = TreeNode('F')
root.right.right = TreeNode('G')


def bfs(root: TreeNode):
    s_q = deque()
    s_q += [root]
    while s_q:
        for _ in range(len(s_q)):
            node = s_q.popleft()
            if node:
                print(node.val, end=' ')
                s_q += [node.left]
                s_q += [node.right]


# bfs(root)


# Depth-first search / Поиск или обход в глубину O(V + E)
# DFS(Depth-first search)
# Поиск/Обход в глубину O(V + E)
# Идет в глубь настолько насколько это возможно прежде чем возвращаться назад
# Работает с графами
# Находит путь между вершинами A И B, но не обязательно кратчайший
# Работает рекурсивно,использует стэк STACK
# Лучше использовать если граф слишком широкий, но не слишком глубокий
#
# Популярен при обходе бинарных деревьев
# Есть разные способы обхода, которые различаются порядком обработки узлов


# Preorder(Прямой обход) корень -> левое -> правое
# Используется для копирования или сериализации дерева

def preorder_dfs(root: TreeNode):
    if not root:
        return
    print(root.val, end=' ')
    preorder_dfs(root.left)
    preorder_dfs(root.right)


# preorder_dfs(root)


# Inorder (Симметричный обход) левое -> корень -> правое
# Используется для вывода по возрастанию

def inorder_dfs(root: TreeNode):
    if not root:
        return
    inorder_dfs(root.left)
    print(root.val, end=' ')
    inorder_dfs(root.right)


# inorder_dfs(root)

# Postorder (Обратный обход) левое -> правое -> корень
# Используется для удаления дерева - сначала листья

def postorder(root: TreeNode):
    if not root:
        return
    postorder(root.left)
    postorder(root.right)
    print(root.val, end=' ')


# postorder(root)


# Sorting algorithms:
# Медленные алгоритмы
# Bubble sorting O(n2)
from random import randint


def bubble_sort(array: list):
    for i in range(len(array)):
        for j in range(len(array) - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]


# b_s = [randint(-10, 10) for i in range(10)]
# print(b_s)
# bubble_sort(b_s)
# print(b_s)

# Selection sort O(n2)
def selection_sort(array: list):
    for i in range(len(array)):
        min_i = i
        for j in range(i + 1, len(array)):
            if array[j] < array[min_i]:
                min_i = j
        array[i], array[min_i] = array[min_i], array[i]


#
# s_s = [randint(-10, 10) for i in range(10)]
# print(s_s)
# selection_sort(s_s)
# print(s_s)

# Insertion sorting
def insertion_sort(array: list):
    for i in range(1, len(array)):
        for j in range(i, 0, -1):
            if array[j] < array[j - 1]:
                array[j], array[j - 1] = array[j - 1], array[j]



# i_s = [randint(-10, 10) for i in range(10)]
# print(i_s)
# insertion_sort(i_s)
# print(i_s)

# Главное различие между медленными алгоритамми сортировки и быстрыми  — количество сравнений и обменов
# Меньше лишних обменов
# Пузырёк
# Постоянно меняет соседние элементы:
# Требуется очень много обменов.
# QuickSort
# Делает намного меньше перестановок и быстрее разбивает массив на большие упорядоченные куски.

# Быстрые алгоритмы

# Quick sort Быстрая сортировка
# Работает рекурсивно(разделяй и властвуй) Определить максимально простейший случай из всех возможных и придумать ка свести задачу к нему
# Сильно зависит от выбора опорного элемента!!!
# O(n log n) - Опорный - случайный элемент - Средний случай
# O(n2)  - Опорный - первый элемент и входной массив уже отсортирован - большой стек вызовов и много раз рассматриваем одни и те же элементы - Худший случай
# Оптимизация - выбор медианы выбираем медиану из трех: первый, центральный, последний (уменьшает шанс плохого разбиения)

def quick_sort(array: list) -> list:
    if len(array) < 2:
        return array

    # Optimization with median

    first, second, last = array[0], array[len(array) // 2], array[-1]
    pivot = sorted([first, second, last])[1]
    less = [i for i in array if i < pivot]
    equal = [i for i in array if i == pivot]
    more = [i for i in array if i > pivot]

    # pivot = array[len(array) // 2]
    # less = [i for i in array if i < pivot]
    # equal = [i for i in array if i == pivot]
    # more = [i for i in array if i > pivot]

    return quick_sort(less) + equal + quick_sort(more)

# q_s = [randint(-10, 10) for i in range(10)]
# print(q_s)
# print(quick_sort(q_s))
# print(q_s)


# Merge sorting Сортировка слиянием
# Merge sort O(n log n)
# Более стабильный алгоритм, но требует дополнительных накладных расходов по пямяти
#  Лучший, средний, худший случаи - всегда O(n log n)
# В общем случае работает медленнее чем быстрая сортировка
# Merge sort - это надежный, стабильный алгоритм с гарантированной производительностью, но платой за это является дополнительная память.


def merge(first: list, second: list) -> list:
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

    return merge(a_1, a_2)


#
# m_s = [randint(-10, 10) for i in range(10)]
# print(m_s)
# print(split(m_s))
# # print(m_s)


# Other algorithms:

# Sliding window
# Найти длину самую длинную уникальную подстроку в строке
def sliding_window(seq: str) -> int:
    max_size = 0
    left = 0
    uniq_symb = set()
    for right in range(len(seq)):
        while seq[right] in uniq_symb:
            uniq_symb.remove(seq[left])
            left += 1
        max_size = max(max_size, right - left + 1)
        uniq_symb.add(seq[right])
    return max_size

s = 'asdstr'
print(sliding_window(s))


# Two pointers
def is_palindrome(word: str):
    i, j = 0, len(word) - 1
    while i <= j:
        if word[i] != word[j]:
            return False
        i += 1
        j -= 1
    return True