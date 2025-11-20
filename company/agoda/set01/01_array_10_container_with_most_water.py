"""Container With Most Water problem implementation."""
from typing import List


def _max_area(height: List[int]) -> int:
    """Two pointer approach to compute the max contained water."""
    left, right = 0, len(height) - 1
    best = 0
    while left < right:
        width = right - left
        best = max(best, width * min(height[left], height[right]))
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1
    return best

class Solution:
    def maxArea(self, height: List[int]) -> int:
        best = 0
        left = 0
        right = len(height) - 1
        while left < right:
            best = max(best, (right - left) * min(height[left], height[right]))
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return best


if __name__ == "__main__":
    assert Solution().maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]) == 49
