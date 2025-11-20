from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        """XOR of all numbers leaves the unique element."""
        result = 0
        for num in nums:
            result ^= num
        return result
