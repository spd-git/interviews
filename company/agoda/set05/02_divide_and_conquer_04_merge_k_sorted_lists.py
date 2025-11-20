from typing import List, Optional
import heapq


class ListNode:
    def __init__(self, val: int = 0, next: Optional['ListNode'] = None):
        self.val = val
        self.next = next

    def __lt__(self, other: 'ListNode'):
        return self.val < other.val


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        """Use a min-heap to repeatedly pull the smallest node."""
        heap: List[ListNode] = []
        for node in lists:
            if node:
                heapq.heappush(heap, node)
        dummy = ListNode(0)
        tail = dummy
        while heap:
            node = heapq.heappop(heap)
            tail.next = node
            tail = tail.next
            if node.next:
                heapq.heappush(heap, node.next)
        return dummy.next
