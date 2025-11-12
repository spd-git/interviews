"""Subtree of Another Tree problem implementation."""
from typing import Optional


class TreeNode:
    """Binary tree node."""

    def __init__(self, val: int = 0, left: Optional["TreeNode"] = None, right: Optional["TreeNode"] = None) -> None:
        self.val = val
        self.left = left
        self.right = right


def is_same_tree(s: Optional[TreeNode], t: Optional[TreeNode]) -> bool:
    if not s and not t:
        return True
    if not s or not t or s.val != t.val:
        return False
    return is_same_tree(s.left, t.left) and is_same_tree(s.right, t.right)


def is_subtree(root: Optional[TreeNode], sub_root: Optional[TreeNode]) -> bool:
    """Check if sub_root is a subtree of root."""
    if not sub_root:
        return True
    if not root:
        return False
    if is_same_tree(root, sub_root):
        return True
    return is_subtree(root.left, sub_root) or is_subtree(root.right, sub_root)


if __name__ == "__main__":
    tree = TreeNode(3, TreeNode(4, TreeNode(1), TreeNode(2)), TreeNode(5))
    sub = TreeNode(4, TreeNode(1), TreeNode(2))
    assert is_subtree(tree, sub) is True
