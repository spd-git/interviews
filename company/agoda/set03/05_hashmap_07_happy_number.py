"""LeetCode 202. Happy Number."""


class Solution:
    def isHappy(self, n: int) -> bool:  # noqa: N802
        seen = set()
        while n != 1 and n not in seen:
            seen.add(n)
            n = sum(int(ch) ** 2 for ch in str(n))
        return n == 1
