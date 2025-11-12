"""Maximum Subarray problem implementation."""
from typing import List


def max_sub_array(nums: List[int]) -> int:
    """Kadane's algorithm to find maximum subarray sum."""
    best = current = nums[0]
    for num in nums[1:]:
        current = max(num, current + num)
        best = max(best, current)
    return best


if __name__ == "__main__":
    assert max_sub_array([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6
