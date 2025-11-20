"""LeetCode 134. Gas Station."""

from typing import List


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        total = current = start = 0
        for i, (g, c) in enumerate(zip(gas, cost)):
            total += g - c
            current += g - c
            if current < 0:
                start = i + 1
                current = 0
        return start if total >= 0 else -1
