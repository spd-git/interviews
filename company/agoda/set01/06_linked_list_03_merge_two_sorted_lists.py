"""Merge Two Sorted Lists problem implementation."""
from typing import Optional


class ListNode:
    """Singly linked list node."""

    def __init__(self, val: int, next: Optional["ListNode"] = None) -> None:
        self.val = val
        self.next = next


def merge_two_lists(list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
    """Merge two sorted linked lists into one sorted list."""
    dummy = tail = ListNode(0)
    while list1 and list2:
        if list1.val < list2.val:
            tail.next = list1
            list1 = list1.next
        else:
            tail.next = list2
            list2 = list2.next
        tail = tail.next
    tail.next = list1 or list2
    return dummy.next


if __name__ == "__main__":
    a = ListNode(1, ListNode(2, ListNode(4)))
    b = ListNode(1, ListNode(3, ListNode(4)))
    merged = merge_two_lists(a, b)
    assert [merged.val, merged.next.val, merged.next.next.val, merged.next.next.next.val, merged.next.next.next.next.val, merged.next.next.next.next.next.val] == [1, 1, 2, 3, 4, 4]
