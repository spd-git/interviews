from typing import List, Tuple
from collections import defaultdict
import math


class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        """Count normalized slopes from each anchor point."""
        if len(points) <= 2:
            return len(points)
        result = 0
        for i in range(len(points)):
            slopes = defaultdict(int)
            duplicates = 1
            x1, y1 = points[i]
            for j in range(i + 1, len(points)):
                x2, y2 = points[j]
                dx, dy = x2 - x1, y2 - y1
                if dx == 0 and dy == 0:
                    duplicates += 1
                    continue
                g = math.gcd(dx, dy)
                dx //= g
                dy //= g
                if dx < 0:
                    dx, dy = -dx, -dy
                elif dx == 0:
                    dy = 1
                slopes[(dx, dy)] += 1
            current_max = duplicates
            for count in slopes.values():
                current_max = max(current_max, count + duplicates)
            result = max(result, current_max)
        return result
