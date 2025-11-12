"""Validate Binary Search Tree problem implementation."""
from typing import Optional


class TreeNode:
    """Binary tree node."""

    def __init__(self, val: int = 0, left: Optional["TreeNode"] = None, right: Optional["TreeNode"] = None) -> None:
        self.val = val
        self.left = left
        self.right = right


def is_valid_bst(root: Optional[TreeNode]) -> bool:
    """Validate BST using recursion with bounds."""
    def helper(node: Optional[TreeNode], low: float, high: float) -> bool:
        if not node:
            return True
        if not (low < node.val < high):
            return False
        return helper(node.left, low, node.val) and helper(node.right, node.val, high)

    return helper(root, float("-inf"), float("inf"))


if __name__ == "__main__":
    tree = TreeNode(2, TreeNode(1), TreeNode(3))
    assert is_valid_bst(tree) is True
