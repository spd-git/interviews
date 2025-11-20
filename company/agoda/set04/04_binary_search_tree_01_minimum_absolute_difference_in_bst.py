from __future__ import annotations

from typing import Optional


class TreeNode:
    def __init__(self, val: int = 0, left: Optional["TreeNode"] = None, right: Optional["TreeNode"] = None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        self.prev_val = None
        self.min_diff = float("inf")

        def inorder(node: Optional[TreeNode]) -> None:
            if not node:
                return
            inorder(node.left)
            if self.prev_val is not None:
                self.min_diff = min(self.min_diff, node.val - self.prev_val)
            self.prev_val = node.val
            inorder(node.right)

        inorder(root)
        return int(self.min_diff)
