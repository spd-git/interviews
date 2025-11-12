"""Kth Smallest Element in a BST problem implementation."""
from typing import Optional


class TreeNode:
    """Binary tree node."""

    def __init__(self, val: int = 0, left: Optional["TreeNode"] = None, right: Optional["TreeNode"] = None) -> None:
        self.val = val
        self.left = left
        self.right = right


def kth_smallest(root: Optional[TreeNode], k: int) -> int:
    """In-order traversal to find kth smallest element."""
    stack = []
    current = root
    while True:
        while current:
            stack.append(current)
            current = current.left
        current = stack.pop()
        k -= 1
        if k == 0:
            return current.val
        current = current.right


if __name__ == "__main__":
    tree = TreeNode(3, TreeNode(1, right=TreeNode(2)), TreeNode(4))
    assert kth_smallest(tree, 1) == 1
