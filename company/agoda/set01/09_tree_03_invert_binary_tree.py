"""Invert/Flip Binary Tree problem implementation."""
from typing import Optional


class TreeNode:
    """Binary tree node."""

    def __init__(self, val: int = 0, left: Optional["TreeNode"] = None, right: Optional["TreeNode"] = None) -> None:
        self.val = val
        self.left = left
        self.right = right


def invert_tree(root: Optional[TreeNode]) -> Optional[TreeNode]:
    """Recursively invert binary tree."""
    if root:
        root.left, root.right = invert_tree(root.right), invert_tree(root.left)
    return root


if __name__ == "__main__":
    tree = TreeNode(4, TreeNode(2, TreeNode(1), TreeNode(3)), TreeNode(7, TreeNode(6), TreeNode(9)))
    inverted = invert_tree(tree)
    assert inverted.left.val == 7 and inverted.right.val == 2
