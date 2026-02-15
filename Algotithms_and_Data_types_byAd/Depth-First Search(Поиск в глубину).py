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


def dfs(root: TreeNode):
    if root is None:  # Условие выхода из рекурсии
        return
    print(root.val, end=" ")
    dfs(root.left)
    dfs(root.right)


dfs(root)

# LeetCode 257. Binary Tree Paths
# Given the root of a binary tree, return all root-to-leaf paths in any order.
# A leaf is a node with no children.
#
# Input: root = [1, 2, 3, null, 5]
# Output: ["1->2->5", "1->3"]


# Definition for a binary tree node.

from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        result = []

        def dfs(root, res, tmp=""):
            tmp += f"{str(root.val)} "
            if not (root.left or root.right):
                res.append("->".join(tmp.split(" "))[:-2])
                tmp = ""
                return
            if root.left:
                dfs(root.left, res, tmp)
            if root.right:
                dfs(root.right, res, tmp)

        dfs(root, result)
        return result
