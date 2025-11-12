"""Construct Binary Tree from Preorder and Inorder Traversal implementation."""
from typing import Dict, List, Optional


class TreeNode:
    """Binary tree node."""

    def __init__(self, val: int = 0, left: Optional["TreeNode"] = None, right: Optional["TreeNode"] = None) -> None:
        self.val = val
        self.left = left
        self.right = right


def build_tree(preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
    """Build tree using recursion and hashmap for inorder indices."""
    index_map: Dict[int, int] = {value: idx for idx, value in enumerate(inorder)}

    def helper(pre_left: int, pre_right: int, in_left: int, in_right: int) -> Optional[TreeNode]:
        if pre_left > pre_right or in_left > in_right:
            return None
        root_val = preorder[pre_left]
        root = TreeNode(root_val)
        in_index = index_map[root_val]
        left_size = in_index - in_left
        root.left = helper(pre_left + 1, pre_left + left_size, in_left, in_index - 1)
        root.right = helper(pre_left + left_size + 1, pre_right, in_index + 1, in_right)
        return root

    return helper(0, len(preorder) - 1, 0, len(inorder) - 1)


if __name__ == "__main__":
    preorder = [3, 9, 20, 15, 7]
    inorder = [9, 3, 15, 20, 7]
    tree = build_tree(preorder, inorder)
    assert tree.val == 3 and tree.right.val == 20
