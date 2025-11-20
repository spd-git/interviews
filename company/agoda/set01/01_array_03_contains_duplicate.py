"""Contains Duplicate problem implementation."""
from typing import List


def contains_duplicate(nums: List[int]) -> bool:
    """Return True if any value appears at least twice."""
    seen = set()
    for num in nums:
        if num in seen:
            return True
        seen.add(num)
    return False


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(set(nums)) != len(nums)


if __name__ == "__main__":
    assert contains_duplicate([1, 2, 3, 1]) is True
    assert contains_duplicate([1, 2, 3, 4]) is False
