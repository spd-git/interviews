from typing import List


class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        """Kadane on normal and inverted array to handle wrap-around."""
        total = sum(nums)
        max_end = min_end = 0
        max_sum = -10**9
        min_sum = 10**9
        for num in nums:
            max_end = max(num, max_end + num)
            max_sum = max(max_sum, max_end)
            min_end = min(num, min_end + num)
            min_sum = min(min_sum, min_end)
        if max_sum < 0:
            return max_sum
        return max(max_sum, total - min_sum)
