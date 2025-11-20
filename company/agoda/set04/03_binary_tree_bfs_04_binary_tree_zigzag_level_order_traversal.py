from __future__ import annotations

from typing import List, Optional
from collections import deque


class TreeNode:
    def __init__(self, val: int = 0, left: Optional["TreeNode"] = None, right: Optional["TreeNode"] = None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        results: List[List[int]] = []
        queue = deque([root])
        left_to_right = True
        while queue:
            level_size = len(queue)
            level: List[int] = []
            for _ in range(level_size):
                node = queue.popleft()
                level.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            if not left_to_right:
                level.reverse()
            results.append(level)
            left_to_right = not left_to_right
        return results
