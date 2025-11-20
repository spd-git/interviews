from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        """DP storing rob and skip values for each house."""
        rob_prev = skip_prev = 0
        for amount in nums:
            new_rob = skip_prev + amount
            skip_prev = max(skip_prev, rob_prev)
            rob_prev = new_rob
        return max(rob_prev, skip_prev)
