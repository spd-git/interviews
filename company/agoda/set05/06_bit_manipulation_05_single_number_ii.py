from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        """Track bits appearing once and twice using finite-state bitmasking."""
        ones = twos = 0
        for num in nums:
            ones = (ones ^ num) & ~twos
            twos = (twos ^ num) & ~ones
        return ones
