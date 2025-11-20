"""Two Sum problem implementation."""
from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        Return indices of the two numbers such that they add up to target.

        Uses a hash map to store previously seen values for O(n) time complexity.
        Returns [] if no such pair exists.
        """
        lookup = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in lookup:
                return [lookup[complement], i]
            lookup[num] = i
        return []

if __name__ == "__main__":
    assert Solution().twoSum([2, 7, 11, 15], 9) == [0, 1]
    assert Solution().twoSum([3,2,4], 6) == [1, 2]
    assert Solution().twoSum([3,3], 6) == [0, 1]
