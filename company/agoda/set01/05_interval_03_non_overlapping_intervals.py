"""Non-overlapping Intervals problem implementation."""
from typing import List


def erase_overlap_intervals(intervals: List[List[int]]) -> int:
    """Greedy strategy to remove minimum intervals for non-overlap."""
    if not intervals:
        return 0
    intervals.sort(key=lambda x: x[1])
    count = 0
    end = intervals[0][1]
    for start, finish in intervals[1:]:
        if start < end:
            count += 1
        else:
            end = finish
    return count


if __name__ == "__main__":
    assert erase_overlap_intervals([[1, 2], [2, 3], [3, 4], [1, 3]]) == 1
