from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        """Kadane's algorithm tracking current and global maximum sums."""
        current = best = nums[0]
        for num in nums[1:]:
            current = max(num, current + num)
            best = max(best, current)
        return best
