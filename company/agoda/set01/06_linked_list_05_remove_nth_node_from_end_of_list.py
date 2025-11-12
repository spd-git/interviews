"""Remove Nth Node From End of List problem implementation."""
from typing import Optional


class ListNode:
    """Singly linked list node."""

    def __init__(self, val: int, next: Optional["ListNode"] = None) -> None:
        self.val = val
        self.next = next


def remove_nth_from_end(head: Optional[ListNode], n: int) -> Optional[ListNode]:
    """Two-pointer approach to remove nth node from end."""
    dummy = ListNode(0, head)
    fast = slow = dummy
    for _ in range(n):
        fast = fast.next
    while fast and fast.next:
        fast = fast.next
        slow = slow.next
    if slow.next:
        slow.next = slow.next.next
    return dummy.next


if __name__ == "__main__":
    head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    new_head = remove_nth_from_end(head, 2)
    assert [new_head.val, new_head.next.val, new_head.next.next.val, new_head.next.next.next.val] == [1, 2, 3, 5]
