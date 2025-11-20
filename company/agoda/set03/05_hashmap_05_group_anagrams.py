"""LeetCode 49. Group Anagrams."""

from collections import defaultdict
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:  # noqa: N802
        groups = defaultdict(list)
        for word in strs:
            key = tuple(sorted(word))
            groups[key].append(word)
        return list(groups.values())
