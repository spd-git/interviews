from typing import List
import bisect


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        """Patience sorting approach using tails array and binary search."""
        tails: List[int] = []
        for num in nums:
            idx = bisect.bisect_left(tails, num)
            if idx == len(tails):
                tails.append(num)
            else:
                tails[idx] = num
        return len(tails)
