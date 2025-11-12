"""Binary Tree Maximum Path Sum problem implementation."""
from typing import Optional


class TreeNode:
    """Binary tree node."""

    def __init__(self, val: int = 0, left: Optional["TreeNode"] = None, right: Optional["TreeNode"] = None) -> None:
        self.val = val
        self.left = left
        self.right = right


def max_path_sum(root: Optional[TreeNode]) -> int:
    """Return maximum path sum using post-order traversal."""
    max_sum = float("-inf")

    def gain(node: Optional[TreeNode]) -> int:
        nonlocal max_sum
        if not node:
            return 0
        left_gain = max(gain(node.left), 0)
        right_gain = max(gain(node.right), 0)
        max_sum = max(max_sum, node.val + left_gain + right_gain)
        return node.val + max(left_gain, right_gain)

    gain(root)
    return max_sum


if __name__ == "__main__":
    tree = TreeNode(-10, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
    assert max_path_sum(tree) == 42
