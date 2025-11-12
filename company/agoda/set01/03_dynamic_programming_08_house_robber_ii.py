"""House Robber II problem implementation."""
from typing import List


def rob_linear(nums: List[int]) -> int:
    prev, curr = 0, 0
    for num in nums:
        prev, curr = curr, max(curr, prev + num)
    return curr


def rob(nums: List[int]) -> int:
    """Return maximum amount with circular street constraint."""
    if len(nums) == 1:
        return nums[0]
    return max(rob_linear(nums[:-1]), rob_linear(nums[1:]))


if __name__ == "__main__":
    assert rob([2, 3, 2]) == 3
