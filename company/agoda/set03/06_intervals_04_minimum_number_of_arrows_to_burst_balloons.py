"""LeetCode 452. Minimum Number of Arrows to Burst Balloons."""

from typing import List


class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:  # noqa: N802
        if not points:
            return 0
        points.sort(key=lambda x: x[1])
        arrows = 1
        end = points[0][1]
        for start, stop in points[1:]:
            if start > end:
                arrows += 1
                end = stop
        return arrows
