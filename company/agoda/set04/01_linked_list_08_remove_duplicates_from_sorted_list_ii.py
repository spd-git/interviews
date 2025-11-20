from __future__ import annotations

from typing import Optional


class ListNode:
    def __init__(self, val: int = 0, next: Optional["ListNode"] = None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """Removes all nodes that have duplicate numbers leaving only distinct values."""
        dummy = ListNode(0, head)
        prev = dummy
        current = head

        while current:
            if current.next and current.val == current.next.val:
                duplicate_val = current.val
                while current and current.val == duplicate_val:
                    current = current.next
                prev.next = current
            else:
                prev = prev.next
                current = current.next
        return dummy.next
