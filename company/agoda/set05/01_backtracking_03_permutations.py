from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        """Return all permutations using backtracking with in-place swapping."""
        result: List[List[int]] = []

        def backtrack(first: int) -> None:
            if first == len(nums):
                result.append(nums.copy())
                return
            for i in range(first, len(nums)):
                nums[first], nums[i] = nums[i], nums[first]
                backtrack(first + 1)
                nums[first], nums[i] = nums[i], nums[first]

        backtrack(0)
        return result
