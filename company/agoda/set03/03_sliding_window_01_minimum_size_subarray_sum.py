"""LeetCode 209. Minimum Size Subarray Sum."""

from typing import List


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:  # noqa: N802
        left = 0
        current = 0
        best = float("inf")

        for right, val in enumerate(nums):
            current += val
            while current >= target:
                best = min(best, right - left + 1)
                current -= nums[left]
                left += 1

        return 0 if best == float("inf") else best
