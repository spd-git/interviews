"""LeetCode 45. Jump Game II using greedy BFS layer tracking."""

from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        steps = 0
        current_end = 0
        farthest = 0

        for i in range(len(nums) - 1):
            farthest = max(farthest, i + nums[i])
            if i == current_end:
                steps += 1
                current_end = farthest
        return steps
