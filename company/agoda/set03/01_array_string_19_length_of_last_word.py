"""LeetCode 58. Length of Last Word."""


class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        length = 0
        for ch in reversed(s.strip()):
            if ch == " ":
                break
            length += 1
        return length
