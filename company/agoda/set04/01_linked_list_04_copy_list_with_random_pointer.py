from __future__ import annotations

from typing import Dict, Optional


class Node:
    def __init__(self, x: int, next: Optional["Node"] = None, random: Optional["Node"] = None):
        self.val = x
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: Optional[Node]) -> Optional[Node]:
        """Creates a deep copy of a list with random pointers using a hashmap."""
        if not head:
            return None

        old_to_new: Dict[Node, Node] = {}
        current = head
        while current:
            old_to_new[current] = Node(current.val)
            current = current.next

        current = head
        while current:
            copy = old_to_new[current]
            copy.next = old_to_new.get(current.next)
            copy.random = old_to_new.get(current.random)
            current = current.next

        return old_to_new[head]
