"""LeetCode 88. Merge Sorted Array.

This solution merges from the back to avoid extra space while respecting the
sorted property of both arrays.
"""

from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """Merge ``nums2`` into ``nums1`` in-place.

        Args:
            nums1: First sorted list with enough trailing space to hold ``nums2``.
            m: Number of valid elements in ``nums1``.
            nums2: Second sorted list.
            n: Number of elements in ``nums2``.
        """

        i, j, k = m - 1, n - 1, m + n - 1
        while j >= 0:
            if i >= 0 and nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1
            k -= 1
