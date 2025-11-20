from __future__ import annotations

from typing import Optional


class Node:
    def __init__(self, val: int = 0, left: Optional["Node"] = None, right: Optional["Node"] = None, next: Optional["Node"] = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    def connect(self, root: Optional[Node]) -> Optional[Node]:
        """Uses level traversal with previously established next pointers."""
        current = root
        while current:
            dummy = tail = Node(0)
            while current:
                if current.left:
                    tail.next = current.left
                    tail = tail.next
                if current.right:
                    tail.next = current.right
                    tail = tail.next
                current = current.next
            current = dummy.next
        return root
