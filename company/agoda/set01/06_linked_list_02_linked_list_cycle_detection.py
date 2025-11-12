"""Detect Cycle in a Linked List problem implementation."""
from typing import Optional


class ListNode:
    """Singly linked list node."""

    def __init__(self, val: int, next: Optional["ListNode"] = None) -> None:
        self.val = val
        self.next = next


def has_cycle(head: Optional[ListNode]) -> bool:
    """Use Floyd's Tortoise and Hare algorithm to detect a cycle."""
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow is fast:
            return True
    return False


if __name__ == "__main__":
    node1 = ListNode(3)
    node2 = ListNode(2)
    node3 = ListNode(0)
    node4 = ListNode(-4)
    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node2
    assert has_cycle(node1) is True
