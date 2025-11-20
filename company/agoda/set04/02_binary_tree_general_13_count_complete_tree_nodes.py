from __future__ import annotations

from typing import Optional


class TreeNode:
    def __init__(self, val: int = 0, left: Optional["TreeNode"] = None, right: Optional["TreeNode"] = None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        def tree_height(node: Optional[TreeNode]) -> int:
            height = 0
            while node:
                height += 1
                node = node.left
            return height

        if not root:
            return 0

        left_height = tree_height(root.left)
        right_height = tree_height(root.right)
        if left_height == right_height:
            return (1 << left_height) + self.countNodes(root.right)
        return (1 << right_height) + self.countNodes(root.left)
