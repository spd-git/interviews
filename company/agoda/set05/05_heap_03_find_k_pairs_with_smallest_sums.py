from typing import List, Tuple
import heapq


class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        """Use min-heap seeded with pairs from nums1 and first element of nums2."""
        if not nums1 or not nums2 or k <= 0:
            return []
        heap: List[Tuple[int, int, int]] = []  # sum, i, j
        for i in range(min(k, len(nums1))):
            heapq.heappush(heap, (nums1[i] + nums2[0], i, 0))
        result: List[List[int]] = []
        while heap and len(result) < k:
            _, i, j = heapq.heappop(heap)
            result.append([nums1[i], nums2[j]])
            if j + 1 < len(nums2):
                heapq.heappush(heap, (nums1[i] + nums2[j + 1], i, j + 1))
        return result
