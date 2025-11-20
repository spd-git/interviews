"""LeetCode 242. Valid Anagram."""

from collections import Counter


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:  # noqa: N802
        return Counter(s) == Counter(t)
