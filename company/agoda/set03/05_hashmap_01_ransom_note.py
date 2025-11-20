"""LeetCode 383. Ransom Note."""

from collections import Counter


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:  # noqa: N802
        ransom_counts = Counter(ransomNote)
        magazine_counts = Counter(magazine)
        return all(magazine_counts[c] >= count for c, count in ransom_counts.items())
