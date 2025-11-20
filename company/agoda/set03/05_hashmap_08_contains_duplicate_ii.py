"""LeetCode 219. Contains Duplicate II."""

from typing import Dict, List


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:  # noqa: N802
        last_index: Dict[int, int] = {}
        for i, num in enumerate(nums):
            if num in last_index and i - last_index[num] <= k:
                return True
            last_index[num] = i
        return False
