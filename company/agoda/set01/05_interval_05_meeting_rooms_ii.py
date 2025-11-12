"""Meeting Rooms II (Leetcode Premium) problem implementation."""
import heapq
from typing import List


def min_meeting_rooms(intervals: List[List[int]]) -> int:
    """Use min-heap to track meeting end times."""
    if not intervals:
        return 0
    intervals.sort(key=lambda x: x[0])
    heap: List[int] = []
    for start, end in intervals:
        if heap and heap[0] <= start:
            heapq.heapreplace(heap, end)
        else:
            heapq.heappush(heap, end)
    return len(heap)


if __name__ == "__main__":
    assert min_meeting_rooms([[0, 30], [5, 10], [15, 20]]) == 2
