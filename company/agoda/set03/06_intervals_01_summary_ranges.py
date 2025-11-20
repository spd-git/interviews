"""LeetCode 228. Summary Ranges."""

from typing import List


class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:  # noqa: N802
        if not nums:
            return []

        ranges = []
        start = prev = nums[0]
        for num in nums[1:]:
            if num == prev + 1:
                prev = num
                continue
            ranges.append(f"{start}->{prev}" if start != prev else str(start))
            start = prev = num
        ranges.append(f"{start}->{prev}" if start != prev else str(start))
        return ranges
