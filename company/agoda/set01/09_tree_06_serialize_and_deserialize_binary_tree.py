"""Serialize and Deserialize Binary Tree problem implementation."""
from collections import deque
from typing import Optional


class TreeNode:
    """Binary tree node."""

    def __init__(self, val: int = 0, left: Optional["TreeNode"] = None, right: Optional["TreeNode"] = None) -> None:
        self.val = val
        self.left = left
        self.right = right


class Codec:
    """Codec for serializing and deserializing binary trees."""

    def serialize(self, root: Optional[TreeNode]) -> str:
        if not root:
            return "#"
        queue = deque([root])
        values = []
        while queue:
            node = queue.popleft()
            if node:
                values.append(str(node.val))
                queue.append(node.left)
                queue.append(node.right)
            else:
                values.append("#")
        return ",".join(values)

    def deserialize(self, data: str) -> Optional[TreeNode]:
        if data == "#":
            return None
        values = data.split(",")
        root = TreeNode(int(values[0]))
        queue = deque([root])
        index = 1
        while queue:
            node = queue.popleft()
            if values[index] != "#":
                node.left = TreeNode(int(values[index]))
                queue.append(node.left)
            index += 1
            if values[index] != "#":
                node.right = TreeNode(int(values[index]))
                queue.append(node.right)
            index += 1
        return root


if __name__ == "__main__":
    codec = Codec()
    tree = TreeNode(1, TreeNode(2), TreeNode(3, TreeNode(4), TreeNode(5)))
    data = codec.serialize(tree)
    restored = codec.deserialize(data)
    assert restored.right.left.val == 4
