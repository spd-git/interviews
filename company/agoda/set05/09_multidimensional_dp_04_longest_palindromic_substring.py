

class Solution:
    def longestPalindrome(self, s: str) -> str:
        """Expand around centers for O(n^2) time and O(1) space."""
        if len(s) < 2:
            return s

        def expand(left: int, right: int) -> str:
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left + 1:right]

        longest = ""
        for i in range(len(s)):
            longest = max(longest, expand(i, i), expand(i, i + 1), key=len)
        return longest
