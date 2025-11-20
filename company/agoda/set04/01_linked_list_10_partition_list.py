from __future__ import annotations

from typing import Optional


class ListNode:
    def __init__(self, val: int = 0, next: Optional["ListNode"] = None):
        self.val = val
        self.next = next


class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        """Partitions list preserving order with nodes < x before others."""
        less_dummy = less_tail = ListNode(0)
        greater_dummy = greater_tail = ListNode(0)

        current = head
        while current:
            if current.val < x:
                less_tail.next = current
                less_tail = less_tail.next
            else:
                greater_tail.next = current
                greater_tail = greater_tail.next
            current = current.next

        greater_tail.next = None
        less_tail.next = greater_dummy.next
        return less_dummy.next
