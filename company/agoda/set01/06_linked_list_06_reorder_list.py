"""Reorder List problem implementation."""
from typing import Optional


class ListNode:
    """Singly linked list node."""

    def __init__(self, val: int, next: Optional["ListNode"] = None) -> None:
        self.val = val
        self.next = next


def reorder_list(head: Optional[ListNode]) -> None:
    """Reorder list L0→L1→…→Ln into L0→Ln→L1→Ln-1→… in-place."""
    if not head or not head.next:
        return

    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    prev = None
    current = slow.next
    slow.next = None
    while current:
        nxt = current.next
        current.next = prev
        prev = current
        current = nxt

    first, second = head, prev
    while second:
        tmp1, tmp2 = first.next, second.next
        first.next = second
        second.next = tmp1
        first, second = tmp1, tmp2


if __name__ == "__main__":
    head = ListNode(1, ListNode(2, ListNode(3, ListNode(4))))
    reorder_list(head)
    assert [head.val, head.next.val, head.next.next.val, head.next.next.next.val] == [1, 4, 2, 3]
