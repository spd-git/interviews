from __future__ import annotations

from typing import Optional


class ListNode:
    def __init__(self, val: int = 0, next: Optional["ListNode"] = None):
        self.val = val
        self.next = next


class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        """Rotates the list to the right by k places."""
        if not head or not head.next or k == 0:
            return head

        # Compute length and connect tail to head
        length = 1
        tail = head
        while tail.next:
            tail = tail.next
            length += 1
        tail.next = head

        k = k % length
        steps_to_new_tail = length - k - 1
        new_tail = head
        for _ in range(steps_to_new_tail):
            new_tail = new_tail.next
        new_head = new_tail.next
        new_tail.next = None
        return new_head
