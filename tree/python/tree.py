"""
description: binary tree implementation in python

author: Taimore Khan
"""

from typing import Optional, List
from queue import Queue

class Node:
    def __init__(self, val: int, left=None, right=None) -> None:
        self.val = val
        self.left = left
        self.right = right



class Tree:
    def __init__(self):
        self.visits = []

    def dfs_recurs_preord(self, node:Optional[Node]) -> Optional[List]:
        if node:
            self.visits.append(node.val)
            self.visits.append(self.dfs_recurs_preord(node.left))
            self.visits.append(self.dfs_recurs_preord(node.right))

    def dfs_recurs_inord(self, node:Optional[Node]) -> None:
        if node:
            self.visits.append(self.dfs_recurs_inord(node.left))
            self.visits.append(node.val)
            self.visits.append(self.dfs_recurs_inord(node.right))


    def dfs_recurs_postord(self, node:Optional[Node]) -> None:
        if node:
            self.visits.append(self.dfs_recurs_postord(node.left))
            self.visits.append(self.dfs_recurs_postord(node.right))
            self.visits.append(node.val)

    def dfs_iterative_preord(self, node:Optional[Node]) -> None:
        stack = [node]
        while stack:
            n = stack.pop()
            if n:
                self.visits.append(n.val)
                stack.append(n.right)
                stack.append(n.left)
