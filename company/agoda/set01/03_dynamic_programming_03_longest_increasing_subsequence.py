"""Longest Increasing Subsequence problem implementation."""
from bisect import bisect_left
from typing import List


def length_of_lis(nums: List[int]) -> int:
    """Patience sorting strategy to compute LIS in O(n log n)."""
    tails: List[int] = []
    for num in nums:
        index = bisect_left(tails, num)
        if index == len(tails):
            tails.append(num)
        else:
            tails[index] = num
    return len(tails)


if __name__ == "__main__":
    assert length_of_lis([10, 9, 2, 5, 3, 7, 101, 18]) == 4
