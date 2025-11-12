"""Longest Consecutive Sequence problem implementation."""
from typing import Iterable


def longest_consecutive(nums: Iterable[int]) -> int:
    """Use a set to find longest consecutive sequence in O(n)."""
    num_set = set(nums)
    best = 0
    for num in num_set:
        if num - 1 not in num_set:
            current = num
            streak = 1
            while current + 1 in num_set:
                current += 1
                streak += 1
            best = max(best, streak)
    return best


if __name__ == "__main__":
    assert longest_consecutive([100, 4, 200, 1, 3, 2]) == 4
