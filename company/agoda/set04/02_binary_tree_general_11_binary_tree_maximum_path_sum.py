from __future__ import annotations

from typing import Optional


class TreeNode:
    def __init__(self, val: int = 0, left: Optional["TreeNode"] = None, right: Optional["TreeNode"] = None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.max_sum = float("-inf")

        def gain(node: Optional[TreeNode]) -> int:
            if not node:
                return 0
            left_gain = max(gain(node.left), 0)
            right_gain = max(gain(node.right), 0)
            current_path = node.val + left_gain + right_gain
            self.max_sum = max(self.max_sum, current_path)
            return node.val + max(left_gain, right_gain)

        gain(root)
        return int(self.max_sum)
