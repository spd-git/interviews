from __future__ import annotations

from typing import Optional


class TreeNode:
    def __init__(self, val: int = 0, left: Optional["TreeNode"] = None, right: Optional["TreeNode"] = None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """Flattens the tree in-place using reverse preorder traversal."""
        self.prev: Optional[TreeNode] = None

        def helper(node: Optional[TreeNode]) -> None:
            if not node:
                return
            helper(node.right)
            helper(node.left)
            node.right = self.prev
            node.left = None
            self.prev = node

        helper(root)
