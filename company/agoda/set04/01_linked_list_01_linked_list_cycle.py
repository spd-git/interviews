from __future__ import annotations

from typing import Optional


class ListNode:
    def __init__(self, x: int):
        self.val = x
        self.next: Optional["ListNode"] = None


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        """Detects if a linked list has a cycle using Floyd's algorithm."""
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow is fast:
                return True
        return False
