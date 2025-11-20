"""Merge K Sorted Lists problem implementation."""
import heapq
from typing import List, Optional, Tuple


class ListNode:
    """Singly linked list node."""

    def __init__(self, val: int = 0, next: Optional["ListNode"] = None) -> None:
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


class Solution:

    def is_empty(self, heap):
        for node in heap:
            if node:
                return False
        return True

    def swap(self, arr, i, j):
        arr[i], arr[j] = arr[j], arr[i]

    def heapify(self, heap):
        pass

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        for node in lists:
            heap.append(node)
        new_head = None

        while not self.is_empty(heap):


        return new_head
        # return ListNode(1, ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(4, ListNode(5, ListNode(6))))))))


def array_to_list_node(arr):
    last_element = None
    for element in reversed(arr):
        last_element = ListNode(element, last_element)
    return last_element


def list_node_to_arr(list_node):
    values = []
    while list_node:
        values.append(list_node.val)
        list_node = list_node.next
    return values


if __name__ == "__main__":
    assert list_node_to_arr(Solution().mergeKLists([
        array_to_list_node(     [1,4,5]     ),
        array_to_list_node(     [1,3,4]     ),
        array_to_list_node(     [2,6]       )
    ])) == [1, 1, 2, 3, 4, 4, 5, 6]
