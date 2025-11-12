"""Merge K Sorted Lists problem implementation."""
import heapq
from typing import List, Optional, Tuple


class ListNode:
    """Singly linked list node."""

    def __init__(self, val: int, next: Optional["ListNode"] = None) -> None:
        self.val = val
        self.next = next


def merge_k_lists(lists: List[Optional[ListNode]]) -> Optional[ListNode]:
    """Merge k sorted linked lists using a min-heap."""
    heap: List[Tuple[int, int, ListNode]] = []
    for idx, node in enumerate(lists):
        if node:
            heapq.heappush(heap, (node.val, idx, node))

    dummy = tail = ListNode(0)
    while heap:
        _, idx, node = heapq.heappop(heap)
        tail.next = node
        tail = tail.next
        if node.next:
            heapq.heappush(heap, (node.next.val, idx, node.next))
    return dummy.next


if __name__ == "__main__":
    a = ListNode(1, ListNode(4, ListNode(5)))
    b = ListNode(1, ListNode(3, ListNode(4)))
    c = ListNode(2, ListNode(6))
    merged = merge_k_lists([a, b, c])
    values = []
    while merged:
        values.append(merged.val)
        merged = merged.next
    assert values == [1, 1, 2, 3, 4, 4, 5, 6]
