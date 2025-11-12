"""House Robber problem implementation."""
from typing import List


def rob(nums: List[int]) -> int:
    """Return maximum amount that can be robbed without robbing adjacent houses."""
    prev, curr = 0, 0
    for num in nums:
        prev, curr = curr, max(curr, prev + num)
    return curr


if __name__ == "__main__":
    assert rob([1, 2, 3, 1]) == 4
