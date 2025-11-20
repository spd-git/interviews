from __future__ import annotations

from typing import Optional


class ListNode:
    def __init__(self, val: int = 0, next: Optional["ListNode"] = None):
        self.val = val
        self.next = next


class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        """Reverses nodes between left and right positions (1-indexed)."""
        if left == right or not head:
            return head

        dummy = ListNode(0, head)
        prev = dummy
        for _ in range(left - 1):
            prev = prev.next

        # Reverse sublist
        reverse_prev = None
        current = prev.next
        for _ in range(right - left + 1):
            nxt = current.next
            current.next = reverse_prev
            reverse_prev = current
            current = nxt

        tail = prev.next
        prev.next = reverse_prev
        tail.next = current
        return dummy.next
