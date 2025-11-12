"""Two Sum problem implementation."""
from typing import List, Tuple, Optional


def two_sum(nums: List[int], target: int) -> Optional[Tuple[int, int]]:
    """Return indices of the two numbers such that they add up to target.

    Uses a hash map to store previously seen values for O(n) time complexity.
    Returns None if no such pair exists.
    """
    lookup = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in lookup:
            return lookup[complement], i
        lookup[num] = i
    return None


if __name__ == "__main__":
    assert two_sum([2, 7, 11, 15], 9) == (0, 1)
