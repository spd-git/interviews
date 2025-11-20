from __future__ import annotations

from typing import Dict, List, Optional


class TreeNode:
    def __init__(self, val: int = 0, left: Optional["TreeNode"] = None, right: Optional["TreeNode"] = None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        index_map: Dict[int, int] = {value: i for i, value in enumerate(inorder)}
        self.post_index = len(postorder) - 1

        def helper(left: int, right: int) -> Optional[TreeNode]:
            if left > right:
                return None
            root_val = postorder[self.post_index]
            self.post_index -= 1
            root = TreeNode(root_val)
            inorder_index = index_map[root_val]
            root.right = helper(inorder_index + 1, right)
            root.left = helper(left, inorder_index - 1)
            return root

        return helper(0, len(inorder) - 1)
