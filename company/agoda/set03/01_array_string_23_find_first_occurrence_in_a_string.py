"""LeetCode 28. Find the Index of the First Occurrence in a String."""


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:  # noqa: N802 (LeetCode signature)
        if not needle:
            return 0
        return haystack.find(needle)
