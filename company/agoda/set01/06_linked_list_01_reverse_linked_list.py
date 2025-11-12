"""Reverse Linked List problem implementation."""
from typing import Optional


class ListNode:
    """Singly linked list node."""

    def __init__(self, val: int, next: Optional["ListNode"] = None) -> None:
        self.val = val
        self.next = next


def reverse_list(head: Optional[ListNode]) -> Optional[ListNode]:
    """Iteratively reverse a singly linked list."""
    prev = None
    current = head
    while current:
        nxt = current.next
        current.next = prev
        prev = current
        current = nxt
    return prev


if __name__ == "__main__":
    head = ListNode(1, ListNode(2, ListNode(3)))
    reversed_head = reverse_list(head)
    assert [reversed_head.val, reversed_head.next.val, reversed_head.next.next.val] == [3, 2, 1]
