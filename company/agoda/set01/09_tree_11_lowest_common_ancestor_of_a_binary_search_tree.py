"""Lowest Common Ancestor of a BST problem implementation."""
from typing import Optional


class TreeNode:
    """Binary tree node."""

    def __init__(self, val: int = 0, left: Optional["TreeNode"] = None, right: Optional["TreeNode"] = None) -> None:
        self.val = val
        self.left = left
        self.right = right


def lowest_common_ancestor(root: Optional[TreeNode], p: TreeNode, q: TreeNode) -> Optional[TreeNode]:
    """Iteratively find LCA leveraging BST properties."""
    current = root
    while current:
        if p.val < current.val and q.val < current.val:
            current = current.left
        elif p.val > current.val and q.val > current.val:
            current = current.right
        else:
            return current
    return None


if __name__ == "__main__":
    tree = TreeNode(6,
                    TreeNode(2, TreeNode(0), TreeNode(4, TreeNode(3), TreeNode(5))),
                    TreeNode(8, TreeNode(7), TreeNode(9)))
    p = tree.left
    q = tree.left.right
    assert lowest_common_ancestor(tree, p, q).val == 2
