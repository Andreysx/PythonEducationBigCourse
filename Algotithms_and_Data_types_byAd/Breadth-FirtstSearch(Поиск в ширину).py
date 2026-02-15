# # Поиск в ширину работает только с графами.
# Граф состоит из узлов и ребер(абстрактная структура данных).
# Отношения между узлами могут действовать только в одну сторону(направленные).
# Направленный граф - разновидность графа - Дерево(абстрактная структура данных)
# Либо отношения действовуют в обе стороны(ненаправленные, каждый узел является соседом по отношению к другому)
# Графы реализуются на базе хеш-таблиц.


# Реализация направленного графа на базе хеш-таблицы(dict)
# Хэш-таблицы позволяют смоделировать отношения между объектами

graph = dict()
graph["you"] = ["alice", "bob", "claire"]
graph["bob"] = ["anuj", "peggy"]
graph["alice"] = ["peggy"]
graph["claire"] = ["thom", "jonny"]
graph["anuj"] = []
graph["peggy"] = []
graph["thom"] = []
graph["jonny"] = []
print(graph)

#
# Полный алгоритм поиска в ширину(работает с deque двусторонней очередью(двусвязным списком) Python).
# Сложность алгоритма O(V+E) V - количество вершин Е - количество ребер.
# Алгоритм проверяет сначала связи первого уровня, затем связи второго уровня, затем третьего и тд.
# Поиск в ширину распространяется от начальной точки!
# Поиск в ширину позволяет определять существует ли путь из A в B
# Если путь существует, поиск в ширину определяет кратчайший путь
# BFS работает с любыми типами графов
# Направленными, ненаправленными.
# Циклическими и ациклическими.
# Связными и несвязными.
# Разреженными и плотными.
# Взвешенные графы: BFS не подходит для поиска кратчайшего пути во взвешенных графах.
# Если у ребер разная длина (стоимость), BFS все равно будет считать, что переход по любому ребру стоит "1".
# Это приведет к тому, что найденный путь может оказаться не самым коротким по сумме весов.
# Для взвешенных графов используют алгоритмы Дейкстры или A* (если веса положительные) или Беллмана-Форда (если есть отрицательные веса).

from collections import deque


def person_is_seller(name):  # простая функция для поиска узла(нужного узла) с оканчивающимся именем на м
    return name[-1] == 'm'


# Алгоритм поиска в ширину

def search(name):
    search_queue = deque()  # Создание пустой очереди queue(FIFO First in First out)
    search_queue += graph[name]  # Все соседи добавляются в очередь из списка
    searched = []  # Массив для отслеживания уже проверенных узлов(ДЛЯ ПРЕДОТВРАЩЕНИЯ ЗАЦИКЛИВАНИЯ МЕЖДУ ДВУМЯ УЗЛАМИ)
    while search_queue:  # Пока очередь не пуста
        person = search_queue.popleft()  # Из очереди извлекается первый элемент
        if person not in searched:  # Узел проверяется только в том случае если он не проверялся ранее(для работы с циклическими ненаправленными графами)
            if person_is_seller(person):  # Проверяем узел на правдивость функции для проверки
                print(f'Found {person}')  # Да это то что искали
                return True
            else:
                search_queue += graph[person]  # Добавляются все соседи проверяемого узла
                searched.append(person)  # Узел помечается как уже проверенный
    return False  # Если выполнение дошло до этой строки, значит в графе нет искомого элемента


search('you')

# Пример с реализацией графа классом

from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


root = TreeNode(val="A")
root.left = TreeNode(val="B")
root.right = TreeNode(val="C")
root.left.left = TreeNode(val="D")
root.left.right = TreeNode(val="E")
root.right.left = TreeNode(val="F")
root.right.right = TreeNode(val="G")


def bfs(root: TreeNode):
    q = deque()
    q += [root]
    while q:
        for _ in range(len(q)):
            node = q.popleft()
            if node is not None:
                print(node.val, end=" ")
                q += [node.left]
                q += [node.right]


bfs(root)

# Строчка for _ in range(len(q)): — это элегантный способ сказать:
#
# ("Обработай все узлы, которые сейчас есть в очереди (текущий уровень), и"
#  " не обращай внимания на новые узлы (следующий уровень), которые мы добавим во время этой обработки")
#
# Это классический паттерн для уровневого обхода дерева (level-order traversal).


# LeetCode 222. Count Complete Tree Nodes
# Given the root of a complete binary tree, return the number of the nodes in the tree.
#
# Input: root = [1,2,3,4,5,6]
# Output: 6


# Definition for a binary tree node.
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        search_queue = deque([root])
        count = 0
        while search_queue:
            for _ in range(len(search_queue)):
                node = search_queue.popleft()
                if node:
                    count += 1
                    search_queue += [node.left]
                    search_queue += [node.right]
        return count
