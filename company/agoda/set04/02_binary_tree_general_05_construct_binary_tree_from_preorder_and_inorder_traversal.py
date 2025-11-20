from __future__ import annotations

from typing import Dict, List, Optional


class TreeNode:
    def __init__(self, val: int = 0, left: Optional["TreeNode"] = None, right: Optional["TreeNode"] = None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        index_map: Dict[int, int] = {value: i for i, value in enumerate(inorder)}
        self.pre_index = 0

        def array_to_tree(left: int, right: int) -> Optional[TreeNode]:
            if left > right:
                return None
            root_val = preorder[self.pre_index]
            self.pre_index += 1
            root = TreeNode(root_val)
            root.left = array_to_tree(left, index_map[root_val] - 1)
            root.right = array_to_tree(index_map[root_val] + 1, right)
            return root

        return array_to_tree(0, len(inorder) - 1)
