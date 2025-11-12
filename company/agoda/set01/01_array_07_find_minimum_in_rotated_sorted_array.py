"""Find Minimum in Rotated Sorted Array implementation."""
from typing import List


def find_min(nums: List[int]) -> int:
    """Binary search for the minimum element in a rotated array."""
    left, right = 0, len(nums) - 1
    while left < right:
        mid = (left + right) // 2
        if nums[mid] > nums[right]:
            left = mid + 1
        else:
            right = mid
    return nums[left]


if __name__ == "__main__":
    assert find_min([3, 4, 5, 1, 2]) == 1
