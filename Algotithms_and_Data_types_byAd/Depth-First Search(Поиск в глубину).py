# DFS(Поиск в глубину) - Алгоритм поиска в графе, проходит в глубину от начальной точки
# пока не обнаружит узел у которого нет дочерних узлов.
# Реализуется  при помощи рекурсии(стек вызовов) или стека+цикл

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


def dfs_preorder(root: TreeNode):
    if root is None:  # Условие выхода из рекурсии
        return
    print(root.val, end=" ")
    dfs_preorder(root.left)
    dfs_preorder(root.right)


print(f"DFS PREORDER - {dfs_preorder(root)}")

def dfs_inorder(root: TreeNode):
    if root is None:  # Условие выхода из рекурсии
        return
    dfs_inorder(root.left)
    print(root.val, end=" ")
    dfs_inorder(root.right)


print(f"DFS INORDER - {dfs_inorder(root)}")


def dfs_postorder(root: TreeNode):
    if root is None:  # Условие выхода из рекурсии
        return
    dfs_postorder(root.left)
    dfs_postorder(root.right)
    print(root.val, end=" ")


print(f"DFS POSTORDER - {dfs_postorder(root)}")


# Эти фрагменты кода описывают три классических способа рекурсивного обхода бинарного дерева (DFS — поиск в глубину),
# которые различаются порядком обработки узлов: корня, левого и правого поддеревьев.

       #  A
       # B C
      # D E F G

# Прямой обход (Preorder)
# Сначала добавляется значение корня, затем обход левого поддерева, потом правого.
# Получается последовательность: корень → левое → правое.
# Используется для копирования дерева или сериализации.
def preorder(root):
    return [root.val] + preorder(root.left) + preorder(root.right) if root else []

# Симметричный обход (Inorder)
# Сначала обход левого поддерева, потом корень, затем правое.
# левое -> корень -> правое
# Для бинарного дерева поиска (BST) даёт узлы в отсортированном порядке.
# Применяется для вывода элементов в порядке возрастания.
def inorder(root):
    return inorder(root.left) + [root.val] + inorder(root.right) if root else []

# Обратный обход (Postorder)
# Сначала левое и правое поддеревья, корень — в конце.
# Последовательность: левое → правое → корень.
# Идеален для удаления дерева (сначала листья) или вычисления выражений.
def postorder(root):
    return postorder(root.left) + postorder(root.right) + [root.val] if root else []

print()
print(f"Preorder dfs {preorder(root)}")
print()
print(f"Inorder dfs {inorder(root)}")
print()
print(f"Postorder dfs {postorder(root)}")



# LeetCode 257. Binary Tree Paths
# Given the root of a binary tree, return all root-to-leaf paths in any order.
# A leaf is a node with no children.
#
# Input: root = [1, 2, 3, null, 5]
# Output: ["1->2->5", "1->3"]


# Definition for a binary tree node.
#
# from typing import List
#
#
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
#
#
# class Solution:
#     def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
#         result = []
#
#         def dfs(root, res, tmp=""):
#             tmp += f"{str(root.val)} "
#             if not (root.left or root.right):
#                 res.append("->".join(tmp.split(" "))[:-2])
#                 tmp = ""
#                 return
#             if root.left:
#                 dfs(root.left, res, tmp)
#             if root.right:
#                 dfs(root.right, res, tmp)
#
#         dfs(root, result)
#         return result
