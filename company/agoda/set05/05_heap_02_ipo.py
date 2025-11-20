from typing import List
import heapq


class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        """Greedy using two heaps: one for candidates by capital, one max-heap for profit."""
        projects = sorted(zip(capital, profits))
        max_profit_heap: List[int] = []
        idx = 0
        for _ in range(k):
            while idx < len(projects) and projects[idx][0] <= w:
                heapq.heappush(max_profit_heap, -projects[idx][1])
                idx += 1
            if not max_profit_heap:
                break
            w += -heapq.heappop(max_profit_heap)
        return w
