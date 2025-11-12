"""Meeting Rooms (Leetcode Premium) problem implementation."""
from typing import List


def can_attend_meetings(intervals: List[List[int]]) -> bool:
    """Check if a person can attend all meetings (no overlaps)."""
    intervals.sort()
    for i in range(1, len(intervals)):
        if intervals[i][0] < intervals[i - 1][1]:
            return False
    return True


if __name__ == "__main__":
    assert can_attend_meetings([[0, 30], [5, 10], [15, 20]]) is False
