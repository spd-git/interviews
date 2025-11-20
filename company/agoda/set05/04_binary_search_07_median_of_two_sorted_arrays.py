from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        """Binary search partition smaller array for O(log(min(n, m)))."""
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        m, n = len(nums1), len(nums2)
        total_left = (m + n + 1) // 2
        left, right = 0, m
        while left <= right:
            i = (left + right) // 2
            j = total_left - i
            left_max1 = float('-inf') if i == 0 else nums1[i - 1]
            right_min1 = float('inf') if i == m else nums1[i]
            left_max2 = float('-inf') if j == 0 else nums2[j - 1]
            right_min2 = float('inf') if j == n else nums2[j]
            if left_max1 <= right_min2 and left_max2 <= right_min1:
                if (m + n) % 2 == 0:
                    return (max(left_max1, left_max2) + min(right_min1, right_min2)) / 2
                return float(max(left_max1, left_max2))
            if left_max1 > right_min2:
                right = i - 1
            else:
                left = i + 1
        return 0.0
