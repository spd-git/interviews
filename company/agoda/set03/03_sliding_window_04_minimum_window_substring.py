"""LeetCode 76. Minimum Window Substring."""

from collections import Counter


class Solution:
    def minWindow(self, s: str, t: str) -> str:  # noqa: N802
        if not t:
            return ""

        need = Counter(t)
        missing = len(t)
        left = 0
        best = (float("inf"), None, None)

        for right, ch in enumerate(s):
            if need[ch] > 0:
                missing -= 1
            need[ch] -= 1

            while missing == 0:
                if right - left + 1 < best[0]:
                    best = (right - left + 1, left, right)
                need[s[left]] += 1
                if need[s[left]] > 0:
                    missing += 1
                left += 1

        if best[1] is None:
            return ""
        return s[best[1] : best[2] + 1]
